

import random

# 高危端口
'''
1. **TCP 21 (FTP)** - 文件传输协议，未经加密的FTP容易被窃听和暴力破解。
2. **TCP 22 (SSH)** - 安全外壳协议，虽然安全性高，但如果密码不强或没有其他安全措施，容易被暴力破解。
3. **TCP 23 (Telnet)** - Telnet协议，不加密的文本通信，容易被截获。
4. **TCP 25 (SMTP)** - 简单邮件传输协议，开放的SMTP服务器容易被用来发送垃圾邮件。
5. **TCP 53 (DNS)** - 域名系统，开放的DNS解析器容易成为DNS放大攻击的目标。
6. **TCP 80 (HTTP)** - 超文本传输协议，未加密的HTTP通信容易被窃听。
7. **TCP 110 (POP3)** - 邮局协议版本3，未加密的邮件传输协议容易被窃听。
8. **TCP 139 (NetBIOS)** - 网络基本输入输出系统，容易被利用进行网络传播的攻击。
9. **TCP 143 (IMAP)** - 互联网邮件访问协议，未加密的邮件传输协议容易被窃听。
10. **TCP 443 (HTTPS)** - 超文本传输协议安全版，尽管加密，但配置不当或漏洞可能被利用。
11. **TCP 445 (SMB)** - 服务器消息块协议，常用于传播蠕虫和勒索软件，如WannaCry。
12. **TCP 49  (TACACS) - 终端访问控制器访问控制系统，容易被暴力破解。
13. **UDP 161 (SNMP)** - 简单网络管理协议，容易被利用进行信息收集和放大攻击。
14. **UDP 123 (NTP)** - 网络时间协议，容易被利用进行DDoS放大攻击。
15. **UDP 69 (TFTP)** - 简单文件传输协议，未加密，容易被用来传输恶意软件。
'''
vul_ports = {'21': 'FTP', '22': 'SSH', '23': 'TELNET', '25': 'SMTP', '53': 'DNS',
             '80': 'HTTP', '110': 'POP3', '139': 'NETBIOS', '143': 'IMAP', '443': 'HTTPS',
             '445': 'SMB', '49': 'TACACS', '161': 'SNMP', '123': 'NTP', '69': 'TFTP'}


# 攻击者部分
atk_port_1 = random.randint(20, 450)
atk_port_2 = random.randint(20, 450)

## 防止两个端口相同
while atk_port_1 == atk_port_2:
    atk_port_2 = random.randint(20, 3390)

## 计算攻击端口范围并进行攻击
if atk_port_1 < atk_port_2:
    atk_start = atk_port_1
    atk_end = atk_port_2
else:
    atk_start = atk_port_2
    atk_end = atk_port_1
print(f'攻击者从端口{atk_start}到端口{atk_end}尝试了攻击！')


# 防御者部分
port_list = list(vul_ports.keys()) # 提取高危端口所有的键，即所有的端口，形成一个列表
protection_ports = random.sample(port_list, 5)
print('防御者保护了以下端口：' + ', '.join(protection_ports))

## 剩余未防御的端口
other_vul_ports = [port for port in port_list if port not in protection_ports]


# 最终判定部分
score = total = 100
for port in other_vul_ports:
    if int(port) in range(atk_start, atk_end):
        print(f"攻击者通过{vul_ports[port]}({port})攻击成功")
        score -= total/len(other_vul_ports)
print(f"防守方最终得分：{score}")