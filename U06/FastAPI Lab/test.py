import requests

auth_url = "http://127.0.0.1:5000/auth"

payload = {'username': 'cisco',
           'password': 'cisco123'}

response = requests.post(auth_url, params=payload)
token = response.json()['X-Token']

alert_url = "http://127.0.0.1:5000/alerts"

param = {'x-token': token}

response = requests.get(alert_url, headers=param)

print(response.json())
