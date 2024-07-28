from zabbix import Zabbix

# 这里修改为你的Zabbix Url 和 API Token
url = "http://127.0.0.1:3031/"
api_token = "9dc88e532bcf1762902ff176bdd357d58db63ca61b27cdf0eb80742fbdf919f5"
zabbix_inst = Zabbix(url, api_token)
for host_name in ['cisco', 'huawei']:
    zabbix_inst.collector_host(host_name, prepare=True)
