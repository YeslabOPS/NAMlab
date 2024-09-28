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
    def __init__(self, inventory_dict):
        super().__init__(inventory_dict)
        self.cpu_metric = ['Current', 'FiveSec', 'OneMin', 'FiveMin']
        self.diff_value_cache = {'cpu0':[0.,0.,0.,0.], 'cpu1':[0.,0.,0.,0.]}

    # CPU监控
    def get_cpu(self):
        cmd = 'display cpu'
        cpu_str = self.device.send_command(cmd)
        process_dict = {info.split('%')[0][:-1].strip(): info.split('%')[0][-1] \
                             for info in cpu_str.split('---------------------------')[2].split('\n') \
                             if info != ''}
        cpu_dict = {info.split()[0]: [one.split('%')[0] for one in info.split()[1:5]] for info in \
                         cpu_str.split('-\n')[5].split('\n') \
                         if info != ''}
        for proc_name in process_dict:
            now_v = float(process_dict[proc_name])
            db.write_ts_data('HUAWEI_CPU_PROC', [proc_name, now_v/100.])
        for cpu_name in cpu_dict:
            for i in range(len(cpu_dict[cpu_name])):
                cpu_now_v = float(cpu_dict[cpu_name][i])
                db.write_ts_data('HUAWEI_CPU_USAGE', [cpu_name+'_'+self.cpu_metric[i], cpu_now_v]) #[Current 10]
                diff_now_v = cpu_now_v - self.diff_value_cache[cpu_name][i]
                self.diff_value_cache[cpu_name][i] = diff_now_v
                db.write_ts_data('HUAWEI_CPU_DIFF', [cpu_name+'_'+self.cpu_metric[i], diff_now_v])


if __name__ == "__main__":
    cisco_monitor = CISCO_CPU(CISCO)
    huawei_monitor = HUAWEI_CPU(HUAWEI)
    while True:
        print('新的一轮监控开始')
        cisco_monitor.get_cpu()
        huawei_monitor.get_cpu()
        time.sleep(60)

