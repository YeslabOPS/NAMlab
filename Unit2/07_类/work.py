import random


vul_ports = {'21': 'FTP', '22': 'SSH', '23': 'TELNET', '25': 'SMTP', '53': 'DNS',
             '80': 'HTTP', '110': 'POP3', '139': 'NETBIOS', '143': 'IMAP', '443': 'HTTPS',
             '445': 'SMB', '49': 'TACACS', '161': 'SNMP', '123': 'NTP', '69': 'TFTP'}

def attacker():
    atk_port_1 = random.randint(20, 450)
    atk_port_2 = random.randint(20, 450)
    while atk_port_1 == atk_port_2:
        atk_port_2 = random.randint(20, 3390)
    if atk_port_1 < atk_port_2:
        atk_start = atk_port_1
        atk_end = atk_port_2
    else:
        atk_start = atk_port_2
        atk_end = atk_port_1
    print(f'攻击者从端口{atk_start}到端口{atk_end}尝试了攻击！')
    return atk_start, atk_end

def defender():
    port_list = list(vul_ports.keys())
    protection_ports = random.sample(port_list, 5)
    print('防御者保护了以下端口：' + ', '.join(protection_ports))
    other_ports = [port for port in port_list if port not in protection_ports]
    close_ports = random.sample(other_ports, 5)
    print('防御者关闭了以下端口：' + ', '.join(close_ports))
    other_vul_ports = [port for port in port_list if port not in protection_ports + close_ports]
    return other_vul_ports

def judge(atk_start, atk_end, other_vul_ports):
    score = total = 100
    for port in other_vul_ports:
        if int(port) in range(atk_start, atk_end):
            print(f"攻击者通过{vul_ports[port]}({port})攻击成功")
            score -= total/len(other_vul_ports)
    print(f"防守方最终得分：{score}")


start, end = attacker()
ports = defender()
judge(start, end, ports)
