import requests
endpoint = 'https://api.cloudflare.com/client/v4/'
email = ''
key = ''
type_ = 'zones'
request_point = endpoint + type_
headers_ = {
    'Content-Type': 'application/json'
    , 'X-Auth-Email': email
    , 'X-Auth-Key': key    
}

response = requests.get(request_point, headers=headers_)
response.json()