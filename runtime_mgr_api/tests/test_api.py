import requests
from httmock import urlmatch, HTTMock
from unittest import TestCase
from unittest.mock import patch, Mock, mock_open
from mock_responses import *
from runtime_mgr_api import *


@urlmatch(path='/accounts/login')
def login_mock(url, request):
    return MOCK_LOGIN_RESPONSE


@urlmatch(path='/accounts/login')
def unauthorized_login_mock(url, request):
    return MOCK_UNAUTHORIZED_RESPONSE


@urlmatch(path='/accounts/api/me')
def org_mock(url, request):
    return MOCK_ORG_RESPONSE


@urlmatch(path=r'\/accounts\/api\/organizations\/.*\/environments')
def env_mock(url, request):
    return MOCK_ENV_RESPONSE


@urlmatch(path='/hybrid/api/v1/applications')
def app_mock(url, request):
    return MOCK_APP_RESPONSE


@urlmatch(path='/hybrid/api/v1/servers')
def server_mock(url, request):
    return MOCK_SERVER_RESPONSE


@urlmatch(path='/hybrid/api/v1/serverGroups')
def servergroup_mock(url, request):
    return MOCK_SERVERGROUP_RESPONSE


@urlmatch(path='/hybrid/api/v1/clusters')
def cluster_mock(url, request):
    return MOCK_CLUSTER_RESPONSE


@urlmatch(path='/hybrid/api/v1/applications')
def deploy_mock(url, request):
    return MOCK_DEPLOY_RESPONSE


@urlmatch(path=r'\/hybrid\/api\/v1\/applications\/[0-9]*')
def update_mock(url, request):
    return MOCK_UPDATE_RESPONSE


class TestLogin(TestCase):
    def test_login_sets_header(self):
        with HTTMock(login_mock), HTTMock(org_mock), HTTMock(env_mock):
            rma = API('fake_user', 'fake_pass')

            mock_token = 'dfda2a8f-db59-44cf-af57-274e156df7e5'
            self.assertEqual(
                rma.session.headers['Authorization'],
                'Bearer {}'.format(mock_token)
            )

    def test_unauthorized_login_raises_exception(self):
        with HTTMock(unauthorized_login_mock), \
                self.assertRaises(AnypointAuthError):
            rma = API('fake_user', 'fake_pass')


class TestOrgs(TestCase):
    def test_org_refresh_sets_context(self):
        with HTTMock(login_mock), HTTMock(org_mock), HTTMock(env_mock):
            rma = API('fake_user', 'fake_pass')

            mock_org_id = '731ed508-dbc3-4b78-889c-b5e6fc532b0f'
            self.assertEqual(rma.org_context, mock_org_id)
            self.assertEqual(
                rma.session.headers['X-ANYPNT-ORG-ID'], mock_org_id
            )


class TestEnvs(TestCase):
    def test_switch_env_sets_context(self):
        with HTTMock(login_mock), HTTMock(org_mock), HTTMock(env_mock):
            rma = API('fake_user', 'fake_pass')
            rma.switch_env('FAKEPROD')

            mock_env_id = '36f615eb-7c09-45e9-a880-3809099cb7e8'
            self.assertEqual(rma.env_context, mock_env_id)
            self.assertEqual(
                rma.session.headers['X-ANYPNT-ENV-ID'], mock_env_id
            )


class TestApps(TestCase):
    def test_get_apps_response_is_not_none(self):
        with HTTMock(login_mock), HTTMock(org_mock), \
                HTTMock(env_mock), HTTMock(app_mock):

            rma = API('fake_user', 'fake_pass')
            self.assertIsNotNone(rma.get_apps())

    def test_get_apps_with_target_name_filters_results(self):
        with HTTMock(login_mock), HTTMock(org_mock), \
                HTTMock(env_mock), HTTMock(app_mock):

            rma = API('fake_user', 'fake_pass')
            apps = rma.get_apps(targetName='fakeserver1')

            self.assertEqual(len(apps), 1)


class TestAppNames(TestCase):
    def test_app_name_too_long_raises_exception(self):
        with HTTMock(login_mock), HTTMock(org_mock), HTTMock(env_mock), \
                self.assertRaises(DeployError):

            rma = API('fake_user', 'fake_pass')
            rma.deploy_app('this-app-name-is-toooooooooooooooooooo-long', None)

    def test_app_name_too_short_raises_exception(self):
        with HTTMock(login_mock), HTTMock(org_mock), HTTMock(env_mock), \
                self.assertRaises(DeployError):

            rma = API('fake_user', 'fake_pass')
            rma.deploy_app('x', None)

    def test_app_name_starts_with_dash_raises_exception(self):
        with HTTMock(login_mock), HTTMock(org_mock), HTTMock(env_mock), \
                self.assertRaises(DeployError):

            rma = API('fake_user', 'fake_pass')
            rma.deploy_app('-fakeapp', None)

    def test_app_name_ends_with_dash_raises_exception(self):
        with HTTMock(login_mock), HTTMock(org_mock), HTTMock(env_mock), \
                self.assertRaises(DeployError):

            rma = API('fake_user', 'fake_pass')
            rma.deploy_app('fakeapp-', None)

    def test_app_name_has_invalid_chars_raises_exception(self):
        with HTTMock(login_mock), HTTMock(org_mock), HTTMock(env_mock), \
                self.assertRaises(DeployError):

            rma = API('fake_user', 'fake_pass')
            rma.deploy_app("#@.$*()+;~:'/%_?,=&!", None)


class TestTargets(TestCase):
    def test_server_response_is_not_none(self):
        with HTTMock(login_mock), HTTMock(org_mock), \
                HTTMock(env_mock), HTTMock(server_mock):

            rma = API('fake_user', 'fake_pass')
            self.assertIsNotNone(rma.get_servers())

    def test_servergroup_response_is_not_none(self):
        with HTTMock(login_mock), HTTMock(org_mock), \
                HTTMock(env_mock), HTTMock(servergroup_mock):

            rma = API('fake_user', 'fake_pass')
            self.assertIsNotNone(rma.get_server_groups())

    def test_cluster_response_is_not_none(self):
        with HTTMock(login_mock), HTTMock(org_mock), \
                HTTMock(env_mock), HTTMock(cluster_mock):

            rma = API('fake_user', 'fake_pass')
            self.assertIsNotNone(rma.get_clusters())

    def test_target_response_is_sum_of_parts(self):
        with HTTMock(login_mock), HTTMock(org_mock), HTTMock(env_mock), \
                HTTMock(server_mock), HTTMock(servergroup_mock), \
                HTTMock(cluster_mock):

            rma = API('fake_user', 'fake_pass')
            self.assertEqual(len(rma.get_targets()), 3)


class TestDeploy(TestCase):
    def test_deploy_with_targetname_does_not_fail(self):
        try:
            with HTTMock(login_mock), HTTMock(org_mock), HTTMock(env_mock), \
                    HTTMock(server_mock), HTTMock(servergroup_mock), \
                    HTTMock(cluster_mock), HTTMock(deploy_mock), \
                    patch('builtins.open', mock_open(read_data='fakedata')) as m:

                with open('fakepath') as f:
                    rma = API('fake_user', 'fake_pass')
                    rma.deploy_app('new-fake-app', f, targetName='fakeserver1')
        except DeployError:
            self.fail("Test encountered DeployError")

    def test_deploy_with_targetid_does_not_fail(self):
        try:
            with HTTMock(login_mock), HTTMock(org_mock), HTTMock(env_mock), \
                    HTTMock(server_mock), HTTMock(servergroup_mock), \
                    HTTMock(cluster_mock), HTTMock(deploy_mock), \
                    patch('builtins.open', mock_open(read_data='fake')) as m:

                with open('fakepath') as f:
                    rma = API('fake_user', 'fake_pass')
                    rma.deploy_app('new-fake-app', f, targetName='fakeserver1')
        except DeployError:
            self.fail("Test encountered DeployError")


class TestUpdate(TestCase):
    def test_update_does_not_fail(self):
        try:
            with HTTMock(login_mock), HTTMock(org_mock), HTTMock(env_mock), \
                    HTTMock(app_mock), HTTMock(update_mock), \
                    patch('builtins.open', mock_open(read_data=b'fake')) as m:

                with open('fakepath', 'rb') as f:
                    rma = API('fake_user', 'fake_pass')
                    rma.update_app('fake-app-1', f)
        except DeployError:
            self.fail("Test encountered DeployError")

    def test_update_duplicate_hash_raises_exception(self):
        with HTTMock(login_mock), HTTMock(org_mock), HTTMock(env_mock), \
                HTTMock(app_mock), HTTMock(update_mock), \
                patch('builtins.open', mock_open(read_data=b'fake')) as m, \
                self.assertRaises(DeployError):

            with open('fakepath', 'rb') as f:
                rma = API('fake_user', 'fake_pass')

                # the mock response includes a hash to match b'fake'
                # for fake-app-2
                rma.update_app('fake-app-2', f)
