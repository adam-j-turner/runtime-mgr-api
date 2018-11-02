# runtime_mgr_api
Python wrapper for MuleSoft Anypoint Runtime Manager API

Example usage (deploying an app from local zip file):
```
import runtime_mgr_api
import os

my_api = runtime_mgr_api.API('my_user','my_pass')

my_api.switch_org('MY-ORG')
my_api.switch_env('MY-ENV')

zipFile = open('C:\muletest\my-app.zip', 'rb')

my_api.deploy_app('my-app', zipFile, targetName='my-server-1')
```
