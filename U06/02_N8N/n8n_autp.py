import requests
import json

# N8N API的基本配置
N8N_URL = 'http://192.168.0.145:5678'  # N8N实例的URL
N8N_API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0ODQ5NmI0Yy04YzM3LTRjZjUtOTNmZi03YjdjNWQ2OTUzYWEiLCJpc3MiOiJuOG4iLCJhdWQiOiJwdWJsaWMtYXBpIiwiaWF0IjoxNzMyMTExODIwfQ.WFwzf6xMfd8ILGA-8mkhJ_XBpn5TngTfTnvapvNBR3M'

Headers = {'accept': 'application/json',
           'X-N8N-API-KEY': N8N_API_KEY}

def create_n8n_workflow(json_data, new_name, new_node_param, new_node_conn):
    new_data = {'name': new_name,
                'nodes': json_data["data"][0]["nodes"],
                'connections': json_data["data"][0]["connections"],
                'settings': json_data["data"][0]["settings"],
                "staticData": {"lastId": 1}
                }
    print(new_data)
    url = N8N_URL+'/api/v1/workflows'
    new_data["nodes"].append(new_node_param)
    new_data["connections"]["If"]["main"][0].append(new_node_conn)
    with open('output.json', 'w') as f:
        json.dump(new_data, f, indent=4)
    response = requests.post(url, json=new_data, headers=Headers)
    if response.status_code == 200:
        print("工作流创建成功")
    else:
        print("创建工作流失败:", response.text)

def get_workflows():
    url = N8N_URL+'/api/v1/workflows'
    response = requests.get(url, headers=Headers)
    print(response.status_code)
    if response.status_code == 200:
        result = response.json()
        #with open("my_flow.json", 'w') as f:
        #    json.dump(result, f, indent=4)
        return result

def main():
    old_flow = get_workflows()
    new_node_name = "Run Automation Test"
    new_node_param = {"parameters": {
                            "script": "run_pyats_test"
                        },
                        "name": "Run Automation Test",
                        "type": new_node_name,
                        "typeVersion": 1,
                        "position": [2140, 100]}
    new_node_conn = {"node": new_node_name,
                     "type": "main",
                     "index": 0}
    create_n8n_workflow(old_flow, 'my_auto', new_node_param, new_node_conn)

main()