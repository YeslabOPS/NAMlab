from netmiko import ConnectHandler

## Task1: 完成设备基本信息
device_info = {
    "device_type": "huawei_vrpv8",
    "ip" : '192.168.1.101', 
    "port" : 22, 
    "username" : 'huaweiuser',
    "password" : 'Huawei@123',
}

## Task2: 用ConnectHandler初始化链接
net_connect = ConnectHandler(**device_info)


## Task3: 数据处理找到CPU使用率的几个指标（5秒，1分钟，5分钟）
result = net_connect.send_command('dis cpu')
cpu_line = result.split('CPU utilization for ')[1].split('.')[0]
data_list = [one[-1:] for one in cpu_line.split('%') if one != '']
print(data_list)