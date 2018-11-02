MOCK_LOGIN_RESPONSE = {
    'status_code': 200,
    'content': {
        # fake token
        'access_token': 'dfda2a8f-db59-44cf-af57-274e156df7e5',
        'redirectUrl': '/home/',
        'token_type': 'bearer'
    }
}

MOCK_UNAUTHORIZED_RESPONSE = {
    'status_code': 401,
    'content': 'Unauthorized'
}

MOCK_ORG_RESPONSE = {
    'status_code': 200,
    'content': {
        "user": {
            "id": "2345f29a-6596-4931-bd91-79f25a4ea436",
            "createdAt": "2017-05-25T14:13:31.886Z",
            "updatedAt": "2018-10-31T17:07:11.763Z",
            "organizationId": "731ed508-dbc3-4b78-889c-b5e6fc532b0f",
            "firstName": "Fake",
            "lastName": "User",
            "email": "Fake.User@company.com",
            "phoneNumber": "8005555555",
            "idprovider_id": "mulesoft",
            "username": "fakeuser",
            "enabled": True,
            "deleted": False,
            "lastLogin": "2018-10-31T17:07:00.000Z",
            "type": "host",
            "organizationPreferences": {},
            "organization": {
                "name": "FakeOrg",
                "id": "731ed508-dbc3-4b78-889c-b5e6fc532b0f",
                "createdAt": "2017-01-19T16:01:13.523Z",
                "updatedAt": "2018-10-12T04:32:51.926Z",
                "ownerId": "2345f29a-6596-4931-bd91-79f25a4ea436",
                "clientId": "9f2a60ea-bdff-4959-975c-47c8447a3868",
                "domain": "FakeOrg-2",
                "idprovider_id": "FakeCompany:FakeOrg.anypoint.mulesoft.com",
                "isFederated": True,
                "parentOrganizationIds": [],
                "subOrganizationIds": [
                    "68b41362-ea1b-4269-8035-9c12039b58df",
                    "96408f62-1e13-4036-af59-a6188488f103",
                    "2a9da4c0-6552-41e6-852c-1876742e6a9c"
                ],
                "tenantOrganizationIds": [],
                "isMaster": True,
                "subscription": {
                    "category": "Customer",
                    "type": "Platinum",
                    "expiration": "2019-02-27T16:01:13.522Z"
                },
                "properties": {
                    "identity_management": {
                        "saml": {
                            "issuer": "FakeCompany",
                            "public_key": "-----BEGIN CERTIFICATE-----\\NoCert\\n-----END CERTIFICATE-----",
                            "audience": "FakeOrg.anypoint.mulesoft.com",
                            "claims_mapping": {
                                "group_attribute": "memberOf",
                                "username_attribute": "",
                                "firstname_attribute": "",
                                "lastname_attribute": "",
                                "email_attribute": ""
                            },
                            "name": "SAML 2.0"
                        },
                        "type": {
                            "description": "SAML 2.0",
                            "name": "saml"
                        },
                        "service_provider": {
                            "urls": {
                                "sign_on": "https://fedsso.company.com/fakeuri/saml2sso?SPID=FakeOrg.anypoint.mulesoft.com",
                                "sign_out": "https://fedsso.company.com/signout.html"
                            },
                            "name": "SAML Service Provider"
                        }
                    }
                },
                "entitlements": {
                    "createEnvironments": True,
                    "globalDeployment": True,
                    "createSubOrgs": True,
                    "hybrid": {
                        "enabled": True
                    },
                    "hybridInsight": True,
                    "hybridAutoDiscoverProperties": True,
                    "vCoresProduction": {
                        "assigned": 0,
                        "reassigned": 0
                    },
                    "vCoresSandbox": {
                        "assigned": 0,
                        "reassigned": 0
                    },
                    "vCoresDesign": {
                        "assigned": 17,
                        "reassigned": 0
                    },
                    "staticIps": {
                        "assigned": 0,
                        "reassigned": 0
                    },
                    "vpcs": {
                        "assigned": 2,
                        "reassigned": 0
                    },
                    "vpns": {
                        "assigned": 0,
                        "reassigned": 0
                    },
                    "workerLoggingOverride": {
                        "enabled": False
                    },
                    "mqMessages": {
                        "base": 0,
                        "addOn": 0
                    },
                    "mqRequests": {
                        "base": 0,
                        "addOn": 0
                    },
                    "objectStoreRequestUnits": {
                        "base": 0,
                        "addOn": 0
                    },
                    "objectStoreKeys": {
                        "base": 0,
                        "addOn": 0
                    },
                    "mqAdvancedFeatures": {
                        "enabled": False
                    },
                    "gateways": {
                        "assigned": 0
                    },
                    "designCenter": {
                        "apiExample": False,
                        "apiVisual": True,
                        "mozart": True,
                        "api": True
                    },
                    "partnersProduction": {
                        "assigned": 0
                    },
                    "partnersSandbox": {
                        "assigned": 0
                    },
                    "loadBalancer": {
                        "assigned": 0,
                        "reassigned": 0
                    },
                    "externalIdentity": True,
                    "autoscaling": False,
                    "armAlerts": True,
                    "apis": {
                        "enabled": False
                    },
                    "apiMonitoring": {
                        "schedules": 5
                    },
                    "monitoringCenter": {
                        "productSKU": -1
                    },
                    "crowd": {
                        "hideApiManagerDesigner": True,
                        "enableApiDesigner": True,
                        "environments": True
                    },
                    "cam": {
                        "enabled": False
                    },
                    "exchange2": {
                        "enabled": False
                    },
                    "crowdSelfServiceMigration": {
                        "enabled": False
                    },
                    "kpiDashboard": {
                        "enabled": False
                    },
                    "pcf": False,
                    "appViz": False,
                    "runtimeFabric": True,
                    "anypointSecurityTokenization": {
                        "enabled": False
                    },
                    "anypointSecurityEdgePolicies": {
                        "enabled": False
                    },
                    "messaging": {
                        "assigned": 0
                    },
                    "workerClouds": {
                        "assigned": 1,
                        "reassigned": 0
                    }
                }
            },
            "properties": {
                "cs_auth": {
                    "activeOrganizationId": "9a50dd7f-249a-4973-b9b5-7702b60a869c"
                }
            },
            "memberOfOrganizations": [
                {
                    "name": "FakeOrg",
                    "id": "731ed508-dbc3-4b78-889c-b5e6fc532b0f",
                    "createdAt": "2017-01-19T16:01:13.523Z",
                    "updatedAt": "2018-10-12T04:32:51.926Z",
                    "ownerId": "2345f29a-6596-4931-bd91-79f25a4ea436",
                    "clientId": "9f2a60ea-bdff-4959-975c-47c8447a3868",
                    "domain": "FakeOrg-2",
                    "idprovider_id": "FakeCompany:FakeOrg.anypoint.mulesoft.com",
                    "isFederated": True,
                    "parentOrganizationIds": [],
                    "subOrganizationIds": [
                        "b6c6dbc2-063b-46d4-b282-83c2761c57d0",
                        "cd0a477b-9336-4bee-960f-d872890f7687",
                        "4a810114-0a80-4280-a3c4-91f76ba385f6"
                    ],
                    "tenantOrganizationIds": [],
                    "parentName": None,
                    "parentId": None,
                    "isMaster": True,
                    "subscription": {
                        "category": "Customer",
                        "type": "Platinum",
                        "expiration": "2019-02-27T16:01:13.522Z"
                    }
                },
                {
                    "name": "FakeOrg-BG1",
                    "id": "4a810114-0a80-4280-a3c4-91f76ba385f6",
                    "createdAt": "2018-07-31T15:38:58.986Z",
                    "updatedAt": "2018-10-12T04:32:51.936Z",
                    "ownerId": "0ad20450-9fbe-4801-a1a6-926f725d5a8d",
                    "clientId": "ee75a1ab-d895-42c8-9d6d-f2fa04759194",
                    "domain": None,
                    "idprovider_id": "mulesoft",
                    "isFederated": True,
                    "parentOrganizationIds": [
                        "731ed508-dbc3-4b78-889c-b5e6fc532b0f"
                    ],
                    "subOrganizationIds": [],
                    "tenantOrganizationIds": [],
                    "parentName": "FakeOrg",
                    "parentId": "731ed508-dbc3-4b78-889c-b5e6fc532b0f",
                    "isMaster": False
                },
                {
                    "name": "FakeOrg-BG2",
                    "id": "b6c6dbc2-063b-46d4-b282-83c2761c57d0",
                    "createdAt": "2017-06-07T19:07:45.819Z",
                    "updatedAt": "2018-10-12T04:32:51.936Z",
                    "ownerId": "2345f29a-6596-4931-bd91-79f25a4ea436",
                    "clientId": "1ba6cdb44f0a48a0b4623673c985bdfe",
                    "domain": None,
                    "idprovider_id": "mulesoft",
                    "isFederated": True,
                    "parentOrganizationIds": [
                        "731ed508-dbc3-4b78-889c-b5e6fc532b0f"
                    ],
                    "subOrganizationIds": [],
                    "tenantOrganizationIds": [],
                    "parentName": "FakeOrg",
                    "parentId": "731ed508-dbc3-4b78-889c-b5e6fc532b0f",
                    "isMaster": False
                },
                {
                    "name": "FakeOrg-BG3",
                    "id": "cd0a477b-9336-4bee-960f-d872890f7687",
                    "createdAt": "2018-01-25T16:58:36.904Z",
                    "updatedAt": "2018-10-12T04:32:51.936Z",
                    "ownerId": "2345f29a-6596-4931-bd91-79f25a4ea436",
                    "clientId": "2a9d2f1cfaa9471abb59ac205fee0c97",
                    "domain": None,
                    "idprovider_id": "mulesoft",
                    "isFederated": True,
                    "parentOrganizationIds": [
                        "731ed508-dbc3-4b78-889c-b5e6fc532b0f"
                    ],
                    "subOrganizationIds": [],
                    "tenantOrganizationIds": [],
                    "parentName": "FakeOrg",
                    "parentId": "731ed508-dbc3-4b78-889c-b5e6fc532b0f",
                    "isMaster": False
                }
            ],
            "contributorOfOrganizations": [
                {
                    "name": "FakeOrg",
                    "id": "731ed508-dbc3-4b78-889c-b5e6fc532b0f",
                    "createdAt": "2017-01-19T16:01:13.523Z",
                    "updatedAt": "2018-10-12T04:32:51.926Z",
                    "ownerId": "2345f29a-6596-4931-bd91-79f25a4ea436",
                    "clientId": "9f2a60ea-bdff-4959-975c-47c8447a3868",
                    "domain": "FakeOrg-2",
                    "idprovider_id": "FakeCompany:FakeOrg.anypoint.mulesoft.com",
                    "isFederated": True,
                    "parentOrganizationIds": [],
                    "subOrganizationIds": [
                        "b6c6dbc2-063b-46d4-b282-83c2761c57d0",
                        "cd0a477b-9336-4bee-960f-d872890f7687",
                        "4a810114-0a80-4280-a3c4-91f76ba385f6"
                    ],
                    "tenantOrganizationIds": [],
                    "parentName": None,
                    "parentId": None,
                    "isMaster": True,
                    "subscription": {
                        "category": "Customer",
                        "type": "Platinum",
                        "expiration": "2019-02-27T16:01:13.522Z"
                    }
                },
                {
                    "name": "FakeOrg-BG1",
                    "id": "4a810114-0a80-4280-a3c4-91f76ba385f6",
                    "createdAt": "2018-07-31T15:38:58.986Z",
                    "updatedAt": "2018-10-12T04:32:51.936Z",
                    "ownerId": "0ad20450-9fbe-4801-a1a6-926f725d5a8d",
                    "clientId": "ee75a1ab-d895-42c8-9d6d-f2fa04759194",
                    "domain": None,
                    "idprovider_id": "mulesoft",
                    "isFederated": True,
                    "parentOrganizationIds": [
                        "731ed508-dbc3-4b78-889c-b5e6fc532b0f"
                    ],
                    "subOrganizationIds": [],
                    "tenantOrganizationIds": [],
                    "parentName": "FakeOrg",
                    "parentId": "731ed508-dbc3-4b78-889c-b5e6fc532b0f",
                    "isMaster": False
                },
                {
                    "name": "FakeOrg-BG2",
                    "id": "b6c6dbc2-063b-46d4-b282-83c2761c57d0",
                    "createdAt": "2017-06-07T19:07:45.819Z",
                    "updatedAt": "2018-10-12T04:32:51.936Z",
                    "ownerId": "2345f29a-6596-4931-bd91-79f25a4ea436",
                    "clientId": "1ba6cdb44f0a48a0b4623673c985bdfe",
                    "domain": None,
                    "idprovider_id": "mulesoft",
                    "isFederated": True,
                    "parentOrganizationIds": [
                        "731ed508-dbc3-4b78-889c-b5e6fc532b0f"
                    ],
                    "subOrganizationIds": [],
                    "tenantOrganizationIds": [],
                    "parentName": "FakeOrg",
                    "parentId": "731ed508-dbc3-4b78-889c-b5e6fc532b0f",
                    "isMaster": False
                },
                {
                    "name": "FakeOrg-BG3",
                    "id": "cd0a477b-9336-4bee-960f-d872890f7687",
                    "createdAt": "2018-01-25T16:58:36.904Z",
                    "updatedAt": "2018-10-12T04:32:51.936Z",
                    "ownerId": "2345f29a-6596-4931-bd91-79f25a4ea436",
                    "clientId": "2a9d2f1cfaa9471abb59ac205fee0c97",
                    "domain": None,
                    "idprovider_id": "mulesoft",
                    "isFederated": True,
                    "parentOrganizationIds": [
                        "731ed508-dbc3-4b78-889c-b5e6fc532b0f"
                    ],
                    "subOrganizationIds": [],
                    "tenantOrganizationIds": [],
                    "parentName": "FakeOrg",
                    "parentId": "731ed508-dbc3-4b78-889c-b5e6fc532b0f",
                    "isMaster": False
                }
            ]
        },
        "access_token": {
            "access_token": "46e90028-037c-45ef-bed6-03b20ae31fcc",
            "expires_in": 3596
        }
    }
}

MOCK_ENV_RESPONSE = {
    'status_code': 200,
    'content': {
        "data": [
            {
                "id": "fc0b75a4-8f17-47b8-b0df-18793f7507ba",
                "name": "FAKEDEV",
                "organizationId": "731ed508-dbc3-4b78-889c-b5e6fc532b0f",
                "isProduction": False,
                "type": "sandbox",
                "clientId": "3ea4018a-902f-4682-b5dd-b2915877aef8"
            },
            {
                "id": "36f615eb-7c09-45e9-a880-3809099cb7e8",
                "name": "FAKEPROD",
                "organizationId": "731ed508-dbc3-4b78-889c-b5e6fc532b0f",
                "isProduction": True,
                "type": "production",
                "clientId": "ba493896-be33-49a4-9081-656722d5a149"
            }
        ],
        "total": 2
    }
}

MOCK_APP_RESPONSE = {
    'status_code': 200,
    'content': {
        "data": [
            {
                "id": 1234567,
                "timeCreated": 1539805405470,
                "timeUpdated": 1539870422168,
                "name": "fake-app-1",
                "uptime": 1293834630,
                "desiredStatus": "STARTED",
                "lastReportedStatus": "STARTED",
                "started": True,
                "serverArtifacts": [
                    {
                        "id": 1234568,
                        "timeCreated": 1539805405473,
                        "timeUpdated": 1539887034815,
                        "artifactName": "fake-app-1",
                        "artifact": {
                            "id": 1234569,
                            "storageId": 1234560,
                            "name": "fake-app-1",
                            "fileName": "fake-app-1.jar",
                            "fileChecksum": "ae7dc42268f2324723329141cb6268f2",
                            "fileSize": 23573150,
                            "timeUpdated": 1539870422927
                        },
                        "deploymentId": 1234567,
                        "serverId": 1000000,
                        "lastReportedStatus": "STARTED",
                        "desiredStatus": "STARTED",
                        "message": "",
                        "discovered": False
                    }
                ],
                "artifact": {
                    "id": 1234569,
                    "storageId": 1234560,
                    "name": "fake-app-1",
                    "fileName": "fake-app-1.jar",
                    "fileChecksum": "ae7dc42268f2324723329141cb6268f2",
                    "fileSize": 23573150,
                    "timeUpdated": 1539870422927
                },
                "target": {
                    "id": 1000000,
                    "timeCreated": 1539804670390,
                    "timeUpdated": 1541176181449,
                    "name": "fakeserver1",
                    "type": "SERVER",
                    "serverType": "GATEWAY",
                    "muleVersion": "4.1.4",
                    "gatewayVersion": "4.1.4",
                    "agentVersion": "2.1.7",
                    "licenseExpirationDate": 1551312000000,
                    "certificateExpirationDate": 1602963070000,
                    "status": "RUNNING",
                    "addresses": [
                        {
                            "ip": "8.8.8.8",
                            "networkInterface": "eth0"
                        }
                    ],
                    "runtimeInformation": {
                        "jvmInformation": {
                            "runtime": {
                                "name": "Java(TM) SE Runtime Environment",
                                "version": "1.8.0_181-b13"
                            },
                            "specification": {
                                "vendor": "Oracle Corporation",
                                "name": "Java Platform API Specification",
                                "version": "1.8"
                            }
                        },
                        "osInformation": {
                            "name": "Linux",
                            "version": "3.10.0-862.14.4.el7.x86_64",
                            "architecture": "amd64"
                        },
                        "muleLicenseExpirationDate": 1551312000000
                    }
                }
            },
            {
                "id": 7654321,
                "timeCreated": 1539871651803,
                "timeUpdated": 1539871651809,
                "name": "fake-app-2",
                "uptime": 1293833528,
                "desiredStatus": "STARTED",
                "lastReportedStatus": "STARTED",
                "started": True,
                "serverArtifacts": [
                    {
                        "id": 7654322,
                        "timeCreated": 1539871651807,
                        "timeUpdated": 1539887035906,
                        "artifactName": "fake-app-2",
                        "artifact": {
                            "id": 7654323,
                            "storageId": 7654324,
                            "name": "fake-app-2",
                            "fileName": "fake-app-2.jar",
                            "fileChecksum": "c053ecf9ed41df0311b9df13cc6c3b6078d2d3c2",
                            "fileSize": 19914984,
                            "timeUpdated": 1539871652802
                        },
                        "deploymentId": 7654321,
                        "serverId": 1000000,
                        "lastReportedStatus": "STARTED",
                        "desiredStatus": "STARTED",
                        "message": "",
                        "discovered": False
                    }
                ],
                "artifact": {
                    "id": 7654323,
                    "storageId": 7654324,
                    "name": "fake-app-2",
                    "fileName": "fake-app-2.jar",
                    "fileChecksum": "c053ecf9ed41df0311b9df13cc6c3b6078d2d3c2",
                    "fileSize": 19914984,
                    "timeUpdated": 1539871652802
                },
                "target": {
                    "id": 1000001,
                    "timeCreated": 1539804670390,
                    "timeUpdated": 1541176181449,
                    "name": "fakeserver2",
                    "type": "SERVER",
                    "serverType": "GATEWAY",
                    "muleVersion": "4.1.4",
                    "gatewayVersion": "4.1.4",
                    "agentVersion": "2.1.7",
                    "licenseExpirationDate": 1551312000000,
                    "certificateExpirationDate": 1602963070000,
                    "status": "RUNNING",
                    "addresses": [
                        {
                            "ip": "8.8.4.4",
                            "networkInterface": "eth0"
                        }
                    ],
                    "runtimeInformation": {
                        "jvmInformation": {
                            "runtime": {
                                "name": "Java(TM) SE Runtime Environment",
                                "version": "1.8.0_181-b13"
                            },
                            "specification": {
                                "vendor": "Oracle Corporation",
                                "name": "Java Platform API Specification",
                                "version": "1.8"
                            }
                        },
                        "osInformation": {
                            "name": "Linux",
                            "version": "3.10.0-862.14.4.el7.x86_64",
                            "architecture": "amd64"
                        },
                        "muleLicenseExpirationDate": 1551312000000
                    }
                }
            }
        ]
    }
}

MOCK_SERVER_RESPONSE = {
    'status_code': 200,
    'content': {
        "data": [
            {
                "id": 1000000,
                "timeCreated": 1539804670390,
                "timeUpdated": 1541176181449,
                "name": "fakeserver1",
                "type": "SERVER",
                "serverType": "GATEWAY",
                "muleVersion": "4.1.4",
                "gatewayVersion": "4.1.4",
                "agentVersion": "2.1.7",
                "licenseExpirationDate": 1551312000000,
                "certificateExpirationDate": 1602963070000,
                "status": "RUNNING",
                "addresses": [
                    {
                        "ip": "8.8.8.8",
                        "networkInterface": "eth0"
                    }
                ],
                "runtimeInformation": {
                    "jvmInformation": {
                        "runtime": {
                            "name": "Java(TM) SE Runtime Environment",
                            "version": "1.8.0_181-b13"
                        },
                        "specification": {
                            "vendor": "Oracle Corporation",
                            "name": "Java Platform API Specification",
                            "version": "1.8"
                        }
                    },
                    "osInformation": {
                        "name": "Linux",
                        "version": "3.10.0-862.14.4.el7.x86_64",
                        "architecture": "amd64"
                    },
                    "muleLicenseExpirationDate": 1551312000000
                }
            }
        ]
    }
}

MOCK_SERVERGROUP_RESPONSE = {
    'status_code': 200,
    'content': {
        "data": [
            {
                "id": 123456,
                "timeCreated": 1541183235771,
                "timeUpdated": 1541183235771,
                "name": "fake-group-1",
                "type": "SERVER_GROUP",
                "status": "DISCONNECTED",
                "servers": [
                    {
                        "id": 123455,
                        "timeCreated": 1519060596284,
                        "timeUpdated": 1541183235773,
                        "name": "fake-server-3",
                        "type": "SERVER",
                        "serverType": "GATEWAY",
                        "muleVersion": "3.9.0",
                        "gatewayVersion": "3.9.0",
                        "agentVersion": "1.9.0",
                        "licenseExpirationDate": 1519452000000,
                        "certificateExpirationDate": 1582132596284,
                        "status": "DISCONNECTED",
                        "serverGroupId": 123456,
                        "serverGroupName": "fake-group-1",
                        "addresses": [
                            {
                                "ip": "127.0.0.1",
                                "networkInterface": "eth3"
                            }
                        ],
                        "runtimeInformation": {
                            "jvmInformation": {
                                "runtime": {
                                    "name": "Java(TM) SE Runtime Environment",
                                    "version": "1.8.0_161-b12"
                                },
                                "specification": {
                                    "vendor": "Oracle Corporation",
                                    "name": "Java Platform API Specification",
                                    "version": "1.8"
                                }
                            },
                            "osInformation": {
                                "name": "Windows 7",
                                "version": "6.1",
                                "architecture": "x86"
                            },
                            "muleLicenseExpirationDate": 1519452000000
                        }
                    }
                ]
            }
        ]
    }
}

MOCK_CLUSTER_RESPONSE = {
    'status_code': 200,
    'content': {
        "data": [
            {
                "id": 555555,
                "timeCreated": 1521942106448,
                "timeUpdated": 1541159115261,
                "name": "fake-cluster-1",
                "type": "CLUSTER",
                "status": "RUNNING",
                "multicastEnabled": False,
                "primaryNodeId": 555551,
                "servers": [
                    {
                        "id": 555551,
                        "timeCreated": 1521863052021,
                        "timeUpdated": 1541123908530,
                        "name": "fake-server-4",
                        "type": "SERVER",
                        "serverType": "GATEWAY",
                        "muleVersion": "3.9.0",
                        "gatewayVersion": "3.9.0",
                        "agentVersion": "1.9.4",
                        "licenseExpirationDate": 1551312000000,
                        "certificateExpirationDate": 1585021452021,
                        "status": "RUNNING",
                        "addresses": [
                            {
                                "ip": "10.10.10.10",
                                "networkInterface": "eth0"
                            }
                        ],
                        "clusterId": 555555,
                        "clusterName": "fake-cluster-1",
                        "serverIp": "10.10.10.10",
                        "currentClusteringIp": "10.10.10.10",
                        "currentClusteringPort": 5701,
                        "runtimeInformation": {
                            "jvmInformation": {
                                "runtime": {
                                    "name": "Java(TM) SE Runtime Environment",
                                    "version": "1.8.0_181-b13"
                                },
                                "specification": {
                                    "vendor": "Oracle Corporation",
                                    "name": "Java Platform API Specification",
                                    "version": "1.8"
                                }
                            },
                            "osInformation": {
                                "name": "Linux",
                                "version": "3.10.0-862.14.4.el7.x86_64",
                                "architecture": "amd64"
                            },
                            "muleLicenseExpirationDate": 1551312000000
                        }
                    },
                    {
                        "id": 555552,
                        "timeCreated": 1521940058282,
                        "timeUpdated": 1541159115099,
                        "name": "fake-server-5",
                        "type": "SERVER",
                        "serverType": "GATEWAY",
                        "muleVersion": "3.9.0",
                        "gatewayVersion": "3.9.0",
                        "agentVersion": "1.9.4",
                        "licenseExpirationDate": 1551312000000,
                        "certificateExpirationDate": 1585098458282,
                        "status": "RUNNING",
                        "addresses": [
                            {
                                "ip": "10.10.10.20",
                                "networkInterface": "eth0"
                            }
                        ],
                        "clusterId": 555555,
                        "clusterName": "fake-cluster-1",
                        "serverIp": "10.10.10.20",
                        "currentClusteringIp": "10.10.10.20",
                        "currentClusteringPort": 5701,
                        "runtimeInformation": {
                            "jvmInformation": {
                                "runtime": {
                                    "name": "Java(TM) SE Runtime Environment",
                                    "version": "1.8.0_181-b13"
                                },
                                "specification": {
                                    "vendor": "Oracle Corporation",
                                    "name": "Java Platform API Specification",
                                    "version": "1.8"
                                }
                            },
                            "osInformation": {
                                "name": "Linux",
                                "version": "3.10.0-862.14.4.el7.x86_64",
                                "architecture": "amd64"
                            },
                            "muleLicenseExpirationDate": 1551312000000
                        }
                    }
                ],
                "visibilityMap": {
                    "mapNodes": [
                        {
                            "serverId": 555551,
                            "visibleNodeIds": [
                                555551,
                                555552
                            ],
                            "unknownNodeIps": []
                        },
                        {
                            "serverId": 555552,
                            "visibleNodeIds": [
                                555551,
                                555552
                            ],
                            "unknownNodeIps": []
                        }
                    ]
                }
            }
        ]
    }
}

MOCK_DEPLOY_RESPONSE = {
    'status_code': 202,
    'content': {
        "data": {
            "id": 684,
            "artifact": {
                "id": 1027,
                "name": "test",
                "fileName": "test.zip",
                "fileChecksum": "e98753b28c0fc7f2d01c56682de1387be0faf040",
                "timeUpdated": 1441221944496
            },
            "lastReportedStatus": "UNDEPLOYED"
        }
    }
}

MOCK_DEPLOY_FAILED_RESPONSE = {
    'status_code': 500,
    'content': {
        "data": {}
    }
}

MOCK_UPDATE_RESPONSE = {
    'status_code': 200,
    'content': {
        "data": {
            "id": 684,
            "artifact": {
                "id": 1027,
                "name": "test",
                "fileName": "test.zip",
                "fileChecksum": "e98753b28c0fc7f2d01c56682de1387be0faf040",
                "timeUpdated": 1441221944496
            },
            "lastReportedStatus": "STARTED"
        }
    }
}
