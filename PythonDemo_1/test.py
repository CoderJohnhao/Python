import requests
import json

url = 'https://api.github.com/some/endpoint'
playload = {'some': 'data'}
r = requests.post(url)
print(r.status_code == requests.codes.ok)
r.raise_for_status()