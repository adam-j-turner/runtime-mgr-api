ANYPOINT_BASE_URL = 'https://anypoint.mulesoft.com'
ANYPOINT_LOGIN_URL = ANYPOINT_BASE_URL + '/accounts/login'
ANYPOINT_ORG_URL = ANYPOINT_BASE_URL + '/accounts/api/me'
ANYPOINT_ENV_URL = ANYPOINT_BASE_URL + \
    '/accounts/api/organizations/{}/environments'
ANYPOINT_CLUSTER_URL = ANYPOINT_BASE_URL + '/hybrid/api/v1/clusters'
ANYPOINT_SERVER_URL = ANYPOINT_BASE_URL + '/hybrid/api/v1/servers'
ANYPOINT_SERVERGROUP_URL = ANYPOINT_BASE_URL + '/hybrid/api/v1/serverGroups'
ANYPOINT_APP_URL = ANYPOINT_BASE_URL + '/hybrid/api/v1/applications'
ANYPOINT_TARGET_URL = ANYPOINT_BASE_URL + '/hybrid/api/v1/targets'

APP_CHAR_REGEX = '[^A-Za-z0-9-]'
APP_MIN_LEN = 3
APP_MAX_LEN = 42
