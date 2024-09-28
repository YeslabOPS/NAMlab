from zabbix import Zabbix

# 这里修改为你的Zabbix Url 和 API Token
url = "http://192.168.0.145:3031/"
api_token = "de6775b972dd9c394feafa70c6369edc6b7310fb60d61ac0494e677985c99112"
zabbix_inst = Zabbix(url, api_token)
print(zabbix_inst.inventory)
for host_name in ['cisco_core', 'huawei_core']:
    zabbix_inst.collector_host(host_name, prepare=True)
