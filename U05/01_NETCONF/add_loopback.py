from ncclient import manager
from device import Device
import xml.dom.minidom

# 配置变更
loopback_data = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface>
   <Loopback>
    <name>100</name>
    <description>TEST1</description>
    <ip>
     <address>
      <primary>
       <address>100.100.100.100</address>
       <mask>255.255.255.0</mask>
      </primary>
     </address>
    </ip>
   </Loopback>
  </interface>
 </native>
</config>
"""

with manager.connect(**Device) as cisco:
    print("开始变更配置")
    # 通过 edit_config 方法对配置进行变更
    result = cisco.edit_config(target="candidate", config=loopback_data)
    print(xml.dom.minidom.parseString(result.xml).toprettyxml())
    cisco.commit()

# 变更后配置查询
netconf_conf_filter = '''
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback/>
        </interface>
    </native>
</filter>
'''

with manager.connect(**Device) as cisco:
    print("开始查询配置")
    # 通过 filter 过滤部分配置
    conf = cisco.get_config(source="running", filter=netconf_conf_filter)
    print(xml.dom.minidom.parseString(conf.xml).toprettyxml())

