import time
from utils import DataWriter
from zabbix import Zabbix

# 这里修改为你的Zabbix Url 和 API Token
url = "http://192.168.0.145:3031/"
api_token = "de6775b972dd9c394feafa70c6369edc6b7310fb60d61ac0494e677985c99112"
zabbix_inst = Zabbix(url, api_token)

db = DataWriter()

metrics = {'cisco_core': ["47190", "47191", "47192"],
           'huawei_core': ["47297", "47298", "47299"]}

def proc_restime(restime):
    return restime * 1000.

while True:
    for host_name in ['cisco_core', 'huawei_core']:
        zabbix_inst.collector_host(host_name, prepare=False, metric_id_list=metrics[host_name])

        for metric in zabbix_inst.data[host_name]:
            value = zabbix_inst.data[host_name][metric]
            if "ICMP response time" in metric:
                if value == zabbix_inst.old_data[host_name][metric]:
                    continue
                value = proc_restime(value)
            db.write_ts_data('zabbix_'+host_name, [host_name+'_'+metric, value])

    zabbix_inst.old_data = zabbix_inst.data
    #print(zabbix_inst.data)
    zabbix_inst.data = {}
    time.sleep(5)






