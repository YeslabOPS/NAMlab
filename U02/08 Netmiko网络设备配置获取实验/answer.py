from netmiko import ConnectHandler

## Task1: 完成设备基本信息
device_info = {
    "device_type": "huawei_vrpv8",
    "ip" : '10.1.1.221',
    "port" : 22, 
    "username" : 'huaweiuser',
    "password" : 'Huawei123@',
}

cmd = "display current-configuration"

## Task2: 用ConnectHandler初始化链接
net_connect = ConnectHandler(**device_info)

## Task3: 发送命令获取配置
result = net_connect.send_command(cmd)
net_connect.disconnect()


## Task4: 处理配置数据并保存在本地
data = 'aaa' + result.split('aaa')[1]
print(data)
with open('huawei_config.cfg', 'w') as f:
    f.write(data)
with open('huawei_config.cfg') as f:
    new_data = f.read()
print(new_data)