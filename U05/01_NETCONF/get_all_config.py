from ncclient import manager
from device import Device
import xml.dom.minidom

# 通过 manager 建立 NETCONF 连接
with manager.connect(**Device) as cisco:
    print("连接成功!")
    conf = cisco.get_config(source="running")
    print(xml.dom.minidom.parseString(conf.xml).toprettyxml())

