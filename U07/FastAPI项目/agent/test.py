import requests

url = "http://127.0.0.1:5000/api/monitor"
data = {"cmd_list": ['inter lo0', 'ip add 100.100.100.100 255.255.255.0']}
resp = requests.post(url, json=data)