import requests
"""
d365_py

A python library to make Dynamics 365 authentication easier
"""

__version__ = "0.0.1"
__author__ = 'Dvyision'
__credits__ = 'Dvyision'

auth_url = 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize'
token_url = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'

class d365:
    TENANT = ''
    CLIENT_ID = ''
    CLIENT_SECRET = ''
    SCOPES = []
    REDIRECT = ''
    ACCESS_TOKEN = ''

    def __init__(self,TENANT,CLIENT_ID,CLIENT_SECRET,REDIRECT):
        self.TENANT = TENANT
        self.CLIENT_ID = CLIENT_ID
        self.CLIENT_SECRET = CLIENT_SECRET
        self.REDIRECT = REDIRECT
        self.SCOPES = 'https://{}/.default offline_access'.format(self.TENANT)
        return

    def authorize(self):
        url = "{}?client_id={}&response_type=code&prompt=select_account&redirect_uri={}&scope={}".format(auth_url, self.CLIENT_ID, self.REDIRECT, self.SCOPES)
        return url
    
    def authenticate(self,CODE):
        body = {
            "client_id": self.CLIENT_ID,
            "client_secret": self.CLIENT_SECRET,
            "grant_type": "authorization_code",
            "code": CODE,
            "scope": self.SCOPES,
            "redirect_uri": self.REDIRECT
        }

        result = requests.post(token_url, data=body).json()

        self.ACCESS_TOKEN = result['access_token']

        return result

    def refresh(self,REFRESH_TOKEN):
        body = {
            "client_id": self.CLIENT_ID,
            "client_secret": self.CLIENT_SECRET,
            "grant_type": "refresh_token",
            "refresh_token": REFRESH_TOKEN,
            "scope": self.SCOPES,
            "redirect_uri": self.REDIRECT
        }

        result = requests.post(token_url, data=body).json()

        self.ACCESS_TOKEN = result['access_token']

        return result
    
    def list(self,TABLE,QUERYSTRING=''):
        headers = {
            "Prefer": "odata.include-annotations=\"*\"",
            "content-type": "application/json; odata.metadata=full",
            "Authorization": "Bearer {}".format(self.ACCESS_TOKEN)
        }
        response = requests.get('https://{}/api/data/v9.0/{}{}'.format(self.TENANT,TABLE,QUERYSTRING), headers=headers).json()
        return response

    def get(self,TABLE,PRIMARY_ID):
        headers = {
            "Prefer": "odata.include-annotations=\"*\"",
            "content-type": "application/json; odata.metadata=full",
            "Authorization": "Bearer {}".format(self.ACCESS_TOKEN)
        }
        response = requests.get('https://{}/api/data/v9.0/{}({})'.format(self.TENANT,TABLE,PRIMARY_ID), headers=headers).json()
        return response

    def update(self,TABLE,PRIMARY_ID,BODY={}):
        headers = {
            "Prefer": "odata.include-annotations=\"*\"",
            "content-type": "application/json; odata.metadata=full",
            "Authorization": "Bearer {}".format(self.ACCESS_TOKEN)
        }
        try:
            response = requests.patch('https://{}/api/data/v9.0/{}({})'.format(self.TENANT,TABLE,PRIMARY_ID), headers=headers,json=BODY).json()
        except:
            response = {'code':'success','message':'updated {} record {}'.format(TABLE,PRIMARY_ID),'data':BODY}
        return response
    
    def create(self,TABLE,BODY={}):
        headers = {
            "Prefer": "odata.include-annotations=\"*\"",
            "content-type": "application/json; odata.metadata=full",
            "Authorization": "Bearer {}".format(self.ACCESS_TOKEN)
        }
        try:
            response = requests.post('https://{}/api/data/v9.0/{}'.format(self.TENANT,TABLE), headers=headers,json=BODY).json()
        except:
            response = {'code':'success','message':'created {} record'.format(TABLE),'data':BODY}
        return response

    def delete(self,TABLE,PRIMARY_ID):
        headers = {
            "Prefer": "odata.include-annotations=\"*\"",
            "content-type": "application/json; odata.metadata=full",
            "Authorization": "Bearer {}".format(self.ACCESS_TOKEN)
        }
        try:
            response = requests.delete('https://{}/api/data/v9.0/{}({})'.format(self.TENANT,TABLE,PRIMARY_ID), headers=headers).json()
        except:
            response = {'code':'success','message':'deleted {} record {}'.format(TABLE,PRIMARY_ID)}
        return response