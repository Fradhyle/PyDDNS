import requests

base_url = 'https://api.cloudflare.com/client/v4/'

class Auth:
    def __init__(self):
        self.headers = {}
    
    def set_key_auth(self, email, key):
        self.headers = {
            'Content-Type': 'application/json'
            , 'X-Auth-Email': f'{email}'
            , 'X-Auth-Key': f'{key}'
        }
        return self.headers
    
    def set_token_auth(self, token):
        self.headers = {
            'Content-Type': 'application/json'
            , 'Authorization': f'Bearer {token}'
        }
        return self.headers

import requests

class Zones:
    def __init__(self):
        self.endpoint = base_url + 'zones/'
        print(self.endpoint)
    def list_zones(self):
        response = requests.get(self.endpoint, headers=self.headers)
        self.zones = response.json()['result']
        return self.zones
