from netmiko import ConnectHandler

## Task1: 完成设备基本信息
device_info = {
    "device_type": "huawei_vrpv8",
    "ip" : '192.168.1.101', 
    "port" : 22, 
    "username" : 'huaweiuser',
    "password" : 'Huawei@123',
}

## Task2: 定义一个能完成ConnectHandler的初始化链接的函数
def conn(device_info):
    return ConnectHandler(**device_info)

## Task3: 定义一个可以为任意接口配置IP地址的函数
def config_if_ip(ssh_hand, if_name, ip_address, ip_mask):
    cmd_list = ['system im',
                f'interface {if_name}',
                'undo shut',
                'undo portswitch',
                f'ip add {ip_address} {ip_mask}']
    for cmd in cmd_list:
        ssh_hand.send_command(command_string=cmd,expect_string=r']')



## Task4: 思考程序逻辑并调用上述函数来完成自动化接口配置
net_connect = conn(device_info)
config_if_ip(net_connect, 'GE1/0/9', '2.2.2.2', '24')
net_connect.disconnect()
