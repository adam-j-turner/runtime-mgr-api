from .constants import *
import datetime
import functools
import requests
import hashlib
import time
import re


class UnauthorizedError(Exception):
    pass


class AnypointAuthError(Exception):
    pass


class AnypointRequestError(Exception):
    pass


class OrgError(Exception):
    pass


class EnvError(Exception):
    pass


class DeployError(Exception):
    pass


class ModifyAppError(Exception):
    pass


class ComponentError(Exception):
    pass


class API(object):
    def __init__(self, anypointUser, anypointPass, proxy=None, verifySSL=True):
        self.session = requests.session()
        self.session.verify = verifySSL
        if proxy is not None:
            self.session.proxies = {"https": proxy}

        self.__login(anypointUser, anypointPass)
        self.org_context = None
        self.env_context = None
        self.__refresh_orgs()
        self.__refresh_envs()

        self.__anypoint_user = anypointUser
        self.__anypoint_pass = anypointPass

    def __anypoint_request(self, *args, **kwargs):
        try:
            resp = self.session.request(*args, **kwargs)
        except requests.exceptions.Timeout:
            raise AnypointRequestError("Timed out during request to Anypoint")
        except requests.exceptions.TooManyRedirects:
            raise AnypointRequestError(
                "Too many redirects during request to Anypoint")

        if resp.status_code == 401:
            raise UnauthorizedError()

        return resp.json(), resp.status_code

    def __login(self, un=None, pw=None):
        if un is None:
            un = self.__anypoint_user
        if pw is None:
            pw = self.__anypoint_pass
        # clear headers so we are not passing token during login
        self.session.headers = {}

        args = 'POST', ANYPOINT_LOGIN_URL
        kwargs = {'data': {
            'Content-Type': 'application/json',
            'username': un, 'password': pw
        }}

        try:
            auth, code = self.__anypoint_request(*args, **kwargs)
        except UnauthorizedError:
            raise AnypointAuthError('Invalid credentials')

        self.session.headers['Authorization'] = 'Bearer {}'.format(
          auth['access_token']
        )

    @property
    def current_org(self):
        if self.org_context is None:
            return None

        return next(
            o for o in self.orgs if o['id'] == self.org_context
        )

    @property
    def org_context(self):
        return self.__org_context

    @org_context.setter
    def org_context(self, value):
        self.__org_context = value
        self.session.headers['X-ANYPNT-ORG-ID'] = value

    @property
    def current_env(self):
        if self.env_context is None:
            return None

        return next(
            e for e in self.envs if e['id'] == self.env_context
        )

    @property
    def env_context(self):
        return self.__env_context

    @env_context.setter
    def env_context(self, value):
        self.__env_context = value
        self.session.headers['X-ANYPNT-ENV-ID'] = value

    def __refresh_orgs(self):
        args = 'GET', ANYPOINT_ORG_URL

        try:
            resp, code = self.__anypoint_request(*args)
            self.orgs = resp['user']['memberOfOrganizations']
        except AnypointRequestError:
            raise OrgError('Could not get Orgs')

        if self.org_context is None:
            self.org_context = next(
                (o for o in self.orgs if o['isMaster']), None
            )['id']

    def switch_org(self, orgName):
        try:
            self.org_context = next(
                o for o in self.orgs if o['name'] == orgName
            )['id']
        except StopIteration:
            raise OrgError('Could not find desired Org')

        self.env_context = None
        self.__refresh_envs()

    def __refresh_envs(self):
        url = ANYPOINT_ENV_URL.format(self.org_context)
        args = 'GET', url

        try:
            resp, code = self.__anypoint_request(*args)
            self.envs = resp['data']
        except AnypointRequestError:
            raise EnvError('Could not get Envs')

    def switch_env(self, envName):
        try:
            self.env_context = next(
                e for e in self.envs if e['name'] == envName
            )['id']
        except StopIteration:
            raise EnvError('Could not find desired Env')

    def get_apps(self, targetName=None):
        args = 'GET', ANYPOINT_APP_URL
        resp, code = self.__anypoint_request(*args)
        apps = resp['data']

        if targetName is not None:
            apps = [a for a in apps if a['target']['name'] == targetName]

        return apps

    def get_servers(self):
        args = 'GET', ANYPOINT_SERVER_URL
        resp, code = self.__anypoint_request(*args)
        return resp['data']

    def get_server_groups(self):
        args = 'GET', ANYPOINT_SERVERGROUP_URL
        resp, code = self.__anypoint_request(*args)
        return resp['data']

    def get_clusters(self):
        args = 'GET', ANYPOINT_CLUSTER_URL
        resp, code = self.__anypoint_request(*args)
        return resp['data']

    def get_targets(self):
        return (
            self.get_servers() + self.get_server_groups() + self.get_clusters()
        )

    def __verify_app_name(self, appName):
        assert len(appName) > APP_MIN_LEN, "App name too short"
        assert len(appName) <= APP_MAX_LEN, "App name too long"
        assert (not appName.startswith('-') and not appName.endswith('-')), \
            "App name starts or ends with a dash"
        assert re.search(APP_CHAR_REGEX, appName) is None, \
            "App name has invalid characters"

    def deploy_app(self, appName, zipFile, targetId=None, targetName=None):
        try:
            self.__verify_app_name(appName)
        except AssertionError as e:
            raise DeployError('App name invalid: {}'.format(str(e)))

        if targetId is None:
            targets = self.get_targets()

            try:
                targetId = next(
                    t for t in targets if t['name'] == targetName
                )['id']
            except StopIteration:
                raise DeployError('Target server or cluster not found')

        args = 'POST', ANYPOINT_APP_URL
        kwargs = {'files': {
            'artifactName': appName,
            'file': zipFile,
            'targetId': str(targetId)
        }}

        resp, code = self.__anypoint_request(*args, **kwargs)

        if code != 202:
            raise DeployError(
                'Deploy failed with HTTP code {}: {}'.format(
                  str(code), resp['message']
                )
            )

    def update_app(self, appName, zipFile, verify=True):
        apps = self.get_apps()

        try:
            app = next(
                a for a in apps if a['name'] == appName
            )
        except StopIteration:
            raise DeployError('Target app not found')

        if verify:
            localhash = hashlib.sha1(zipFile.read()).hexdigest()
            zipFile.seek(0)

            if localhash == app['artifact']['fileChecksum']:
                raise DeployError('Application is already up-to-date')

        args = 'PATCH', '{}/{}'.format(ANYPOINT_APP_URL, str(app['id']))
        kwargs = {'files': {'file': zipFile}}

        resp, code = self.__anypoint_request(*args, **kwargs)

        if code != 200:
            raise DeployError(
                'App update failed with HTTP code {}: {}'.format(
                  str(code), resp['message']
                )
            )
