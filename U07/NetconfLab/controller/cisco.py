import ncclient
from ncclient import manager
from ncclient.xml_ import new_ele, sub_ele

class Cisco:
    def __init__(self):
        ip = "192.168.1.100"
        nc_port = 830
        nc_user = "netconf"
        nc_pass = "cisco123"
        self.nc_proc = manager.connect(host=ip,
                                       port=nc_port,
                                       username=nc_user,
                                       password=nc_pass,
                                       hostkey_verify=False)

    def manage_if(self, ifname, ifip, ifmask, action):
        XML = '''
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface xmlns:operation="{}">
   <Loopback>
    <name>{}</name>
    <description>Automation</description>
    <ip>
     <address>
      <primary>
       <address>{}</address>
       <mask>{}</mask>
      </primary>
     </address>
    </ip>
   </Loopback>
  </interface>
 </native>
</config>
'''.format(action, ifname, ifip, ifmask)

        resp = str(self.nc_proc.edit_config(target='candidate', config=XML))
        self.nc_proc.commit()
        return resp