from netmiko import ConnectHandler

## Task1: 完成设备基本信息
device_info = {
    "device_type": "cisco_ios",
    "ip" : 设备IP, 
    "port" : 22, 
    "username" : 用户名,
    "password" : 密码,
}

cmd = "show running-config"

## Task2: 用ConnectHandler初始化链接


## Task3: 发送命令获取配置


## Task4: 处理配置数据并保存在本地



