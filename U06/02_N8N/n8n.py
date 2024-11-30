import requests
import json

token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzNDJkYWU1Ni0zZWM2LTQ5ZDEtOGEwMy1jYmVhZTVkNzE1ZTEiLCJpc3MiOiJuOG4iLCJhdWQiOiJwdWJsaWMtYXBpIiwiaWF0IjoxNzMyMzQ4MTk4fQ.vQLVPmwQTGxkqWPkxfq4p-Io5yUa4M77SGjInTcH6d8"
host = "http://192.168.0.145:5678/"
header = {"accept": "application/json",
          "X-N8N-API-KEY": token}

def get_all_workflows():
    url = host + "api/v1/workflows"
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        with open('workflows.json', 'w') as outfile:
            json.dump(response.json(), outfile, indent=4)
        return response.json()
    else:
        return response.text

def create_workflow():
    result = get_all_workflows()
    new_data = {'name': 'new workflow'}
    new_data['nodes'] = result['data'][0]['nodes']
    new_data['connections'] = result['data'][0]['connections']
    new_data['settings'] = result['data'][0]['settings']
    with open('my.json') as outfile:
        data = json.load(outfile)
    url = host + "api/v1/workflows"
    response = requests.post(url, headers=header, json=data)
    print(response.status_code)
    print(response.text)

create_workflow()