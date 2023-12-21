import os
import time
import json
import datetime
import pandas as pd
import netmiko
from netmiko import ConnectHandler


excel_path = '网络资产.xlsx'
dst_path = 'config_back'


def get_login_info(excel_path):
    excel = pd.read_excel(excel_path)
    # ip, dtype, username, password
    data_list = [excel.loc[i].values.tolist() for i in range(excel.shape[0])]
    return data_list

def back_file(config_dict, dst_path):
    if not os.path.exists(dst_path):
        os.mkdir(dst_path)
    for ip in config_dict:
        now = str(datetime.datetime.now()).split('.')[0].replace(' ', '_').replace(':', '_')
        file_name = ip + '_' + now + '.txt'
        full_path = dst_path + '/' + file_name
        with open(full_path, 'w') as f:
            f.write(config_dict[ip])
    

class Net:
    # Basic ssh connect & json data output(file save)
    def __init__(self, host, device_type, username, password):
        self.device_info = {
            "device_type": device_type,
            "ip" : host, 
            "port" : 22, 
            "username" : username,
            "password" : password,
        }
        self.device = self.connect()

    # 基本连接功能
    def connect(self):
        return ConnectHandler(**self.device_info)
    
    # 断线重连功能
    def reconnect(self):
        self.device.disconnect()
        self.device = self.connect()
    
    # 数据输出为JSON
    def to_json(self, data_dict, file_path):
        with open(file_path, 'w') as f:
            # 写文件创建日志
            json.dump(data_dict, fp=f, indent=4)



class VRP_8(Net):
    def __init__(self, ip, dtype, username, password):
        super().__init__(ip, dtype, username, password)

    # 获取配置
    ## 输出字符串形式的设备配置
    def get_config(self):
        cmd = 'display current-configuration'
        info = self.device.send_command(cmd)
        data_str = ''.join(info.split('#')[1:])
        return data_str
    
if __name__ == "__main__":
    device_list = get_login_info(excel_path)
    while True:
        for device in device_list:
            try:
                vrp = VRP_8(*device)
                config_str = vrp.get_config()
                vrp.device.disconnect()
                back_file({device[0]: config_str}, dst_path)
                del(vrp)
            except netmiko.exceptions.NetmikoTimeoutException as e:
                print(f"{device[0]} SSH 连接失败，下一轮继续尝试！")
                continue
        time.sleep(15)