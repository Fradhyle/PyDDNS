from ..dman import jsonman

class Auth:
    def __init__(self):
        self.headers = {}
        self.email = ''
        self.key = ''
        self.token = ''
        self.file = jsonman('../auth.json')
    
    def set_key_auth(self, email, key):
        self.email = email
        self.key = key
        self.headers = {
            'Content-Type': 'application/json'
            , 'X-Auth-Email': f'{self.email}'
            , 'X-Auth-Key': f'{self.key}'
        }
        return self.headers
    
    def set_token_auth(self, token):
        self.token = token
        self.headers = {
            'Content-Type': 'application/json'
            , 'Authorization': f'Bearer {self.token}'
        }
