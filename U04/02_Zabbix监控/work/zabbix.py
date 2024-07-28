import json
from pyzabbix.api import ZabbixAPI

class Zabbix:
    def __init__(self, zabbix_url, token):
        # Create ZabbixAPI class instance
        self.zapi = ZabbixAPI(server=zabbix_url)
        self.zapi.login(api_token=token)
        self.inventory = {host['host']: host['hostid'] for host in self.zapi.host.get(monitored_hosts=1, output='extend')}
        self.data = {}

    def collector_host(self, device_name, prepare=False, metric_id_list=None):
        host_id = self.inventory[device_name]
        result = self.zapi.item.get(hostids=host_id)
        metrics: dict = {info['itemid']: info['name'] for info in result}
        # 如果对监控指标不太了解，请将prepare在使用函数时定义为True
        if prepare:
            with open(device_name + '_CheckMe.txt', 'w') as f:
                json.dump(metrics, f, indent=4)
        else:
            item_list = self.zapi.item.get(hostids=host_id, itemids=metric_id_list)
            for info in item_list:
                item_id = info['itemid']
                item_name = metrics[item_id]
                item_lastvalue = info['lastvalue']
                self.data[item_name] = item_lastvalue






