from data import *
from restconf import *

# TODO:清除当前OSPF配置（如果有的话）
now_ospf = check_ospf_config()
if now_ospf.status_code != 204:
    del_ospf()

# TODO:删除100环回接口(如果有的话)
now_loop_if = loop_if_check()
loop_list = now_loop_if.json()['Cisco-IOS-XE-native:Loopback']
for loop_if in loop_list:
    if loop_if['name'] == 100:
        loop_del(100)
        break

# TODO:添加第一次的OSPF配置
modify_ospf(old_ospf_data)

# TODO:更改OSPF的配置为第二次的配置
del_ospf()
modify_ospf(new_ospf_data)

# TODO:添加一个环回接口
loop_if_add(loop_if_data)

# TODO:将OSPF配置应用到接口上
loop_ospf(loop_ospf_data)

# TODO:删除环回接口
loop_del(100)
