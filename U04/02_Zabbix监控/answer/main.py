import time
from utils import DataWriter
from zabbix import Zabbix

# 这里修改为你的Zabbix Url 和 API Token
url = "http://127.0.0.1:3031/"
api_token = "9dc88e532bcf1762902ff176bdd357d58db63ca61b27cdf0eb80742fbdf919f5"
zabbix_inst = Zabbix(url, api_token)

db = DataWriter()

metrics = {'cisco': ["47996", "47997", "47998"],
           'huawei': ["47843", "47844", "47845"]}

while True:
    for host_name in ['cisco', 'huawei']:
        zabbix_inst.collector_host(host_name, prepare=False, metric_id_list=metrics[host_name])
        print(zabbix_inst.data)
        for metric in zabbix_inst.data:
            value = float(zabbix_inst.data[metric])
            db.write_ts_data('zabbix_'+host_name, [metric, value])
    time.sleep(60)






