from netmiko import ConnectHandler

## Task1: 完成设备基本信息
device_info = {
    "device_type": "huawei_vrpv8",
    "ip" : 设备IP, 
    "port" : 22, 
    "username" : 用户名,
    "password" : 密码,
}

cmd = "display current-configuration"

## Task2: 用ConnectHandler初始化链接


## Task3: 发送命令获取配置


## Task4: 处理配置数据并保存在本地



