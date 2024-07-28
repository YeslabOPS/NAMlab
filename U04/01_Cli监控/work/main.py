import re
import time
from inventory import CISCO, HUAWEI
from netmiko import ConnectHandler
from utils import DataWriter


db = DataWriter()


# 接下来我们会复用U3_04实验的部分代码
class Net:
    # Basic ssh connect & json data output(file save)
    def __init__(self, inventory_dict):
        self.device = self.connect(inventory_dict)

    # 基本连接功能
    def connect(self, inventory):
        return ConnectHandler(**inventory)


class CISCO_CPU(Net):
    def __init__(self, inventory_dict):
        super().__init__(inventory_dict)
        self.cpu_str = ['Current', 'FiveSec', 'OneMin', 'FiveMin']

    # CPU监控
    def get_cpu(self):
        cmd = 'show processes cpu'
        cpu_str = self.device.send_command(cmd)
        # 获取CPU使用率指标
        cpu_dict = {}
        cpu_usage_str = cpu_str.split('\n')[0]
        cpu_dict['cpu_5s_1'] = cpu_usage_str.split('%')[0][-1]
        cpu_dict['cpu_5s_2'] = cpu_usage_str.split('%')[1][-1]
        cpu_dict['cpu_1m'] = cpu_usage_str.split('%')[2][-1]
        cpu_dict['cpu_5m'] = cpu_usage_str.split('%')[3][-1]

        # 获取进程指标,只取1分钟非零的，不然太多了
        proc_dict = {}
        for line in cpu_str.split('\n')[2:]:
            if '%' in line:
                proc_usage_v = float(line.split('%')[1].strip())
                if proc_usage_v > 0.:
                    match = re.search(r'.*\d+\s+([A-Za-z\s]+)', line)
                    proc_dict[match.group(1).strip()] = proc_usage_v

        for proc_name in proc_dict:
            if proc_name != '':
                db.write_ts_data('CISCO_CPU_PROC', [proc_name, float(proc_dict[proc_name])])
        for cpu_name in cpu_dict:
            db.write_ts_data('CISCO_CPU_USAGE', [cpu_name, float(cpu_dict[cpu_name])])


# TODO: 编写华为CPU监控类
class HUAWEI_CPU(Net):
    pass




if __name__ == "__main__":
    cisco_monitor = CISCO_CPU(CISCO)
    huawei_monitor = HUAWEI_CPU(HUAWEI)
    while True:
        cisco_monitor.get_cpu()
        huawei_monitor.get_cpu()
        time.sleep(60)

