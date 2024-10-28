from ncclient import manager
from device import Device
import xml.dom.minidom

netconf_conf_filter = '''
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <username></username>
    </native>
</filter>
'''

with manager.connect(**Device) as cisco:
    print("连接成功!")
    # 通过 filter 过滤部分配置
    conf = cisco.get_config(source="running", filter=netconf_conf_filter)
    print(xml.dom.minidom.parseString(conf.xml).toprettyxml())

