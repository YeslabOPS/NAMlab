# 这是一个模拟ping的脚本
import time

cmd = input('C:\Administrator> ')
ip_str = cmd.split('ping')[1].strip()
print(f'来自 {ip_str} 的回复: 字节=32 时间=2ms TTL=64')
time.sleep(1)
print(f'来自 {ip_str} 的回复: 字节=32 时间=2ms TTL=64')
time.sleep(1)
print(f'来自 {ip_str} 的回复: 字节=32 时间=2ms TTL=64')
time.sleep(1)
print(f'来自 {ip_str} 的回复: 字节=32 时间=2ms TTL=64')