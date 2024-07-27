from netmiko import ConnectHandler

class Network():
    def __init__(self, ip, username, password, device_type=""):
        device_info = {
            "device_type": device_type,
            "ip" : ip, 
            "port" : 22, 
            "username" : username,
            "password" : password,
        }
        self.ssh = self.conn()
        self.cpu_data = None
    
    ## Task1: 完善conn函数
    def conn(self):


    ## Task2: 获取设备CPU信息
    def get_cpu(self):


    ## Task3: 数据处理找到CPU使用率的几个指标（5秒，1分钟，5分钟）
    def proc_cpu(self):


## Task4: 调整登录信息，实例化并运行代码
net = Network(设备IP, 用户名, 密码)
net.get_cpu()
net.proc_cpu()