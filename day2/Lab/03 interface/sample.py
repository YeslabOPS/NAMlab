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

## Task3: 为任意接口配置IP地址
cmd_list = ['system im',
            'interface GE1/0/9',
            'undo shut',
            'undo portswitch',
            'ip add 2.2.2.2 24']
for cmd in cmd_list:
    net_connect.send_command(command_string=cmd,expect_string=r']')

## Task4: print输出所有接口的信息
cmd = 'display ip interface brief'
print(net_connect.send_command(cmd))
net_connect.disconnect()
