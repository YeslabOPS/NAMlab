import random


class NetSec:
    def __init__(self):
        self.vul_ports = {'21': 'FTP', '22': 'SSH', '23': 'TELNET',
                          '25': 'SMTP', '53': 'DNS', '80': 'HTTP',
                          '110': 'POP3', '139': 'NETBIOS', '143': 'IMAP',
                          '443': 'HTTPS', '445': 'SMB', '49': 'TACACS',
                          '161': 'SNMP', '123': 'NTP', '69': 'TFTP'}
        self.run()

    def attacker(self):
        atk_port_1 = random.randint(20, 450)
        atk_port_2 = random.randint(20, 450)
        while atk_port_1 == atk_port_2:
            atk_port_2 = random.randint(20, 3390)
        if atk_port_1 < atk_port_2:
            self.atk_start = atk_port_1
            self.atk_end = atk_port_2
        else:
            self.atk_start = atk_port_2
            self.atk_end = atk_port_1
        print(f'攻击者从端口{self.atk_start}到端口{self.atk_end}尝试了攻击！')

    def defender(self):
        port_list = list(self.vul_ports.keys())
        protection_ports = random.sample(port_list, 5)
        print('防御者保护了以下端口：' + ', '.join(protection_ports))
        other_ports = [port for port in port_list if port not in protection_ports]
        close_ports = random.sample(other_ports, 5)
        print('防御者关闭了以下端口：' + ', '.join(close_ports))
        self.other_vul_ports = [port for port in port_list if port not in protection_ports + close_ports]

    def judge(self):
        score = total = 100
        for port in self.other_vul_ports:
            if int(port) in range(self.atk_start, self.atk_end):
                print(f"攻击者通过{self.vul_ports[port]}({port})攻击成功")
                score -= total/len(self.other_vul_ports)
        print(f"防守方最终得分：{score}")

    def run(self):
        self.attacker()
        self.defender()
        self.judge()

my_net_sec = NetSec()



