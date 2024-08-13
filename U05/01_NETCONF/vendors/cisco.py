from default import BaseController

HOST = '10.1.1.229'
USERNAME = 'netconf'
PASSWORD = 'netconf123'

class CiscoController(BaseController):
    def __init__(self):
        super().__init__(HOST, USERNAME, PASSWORD)
        self.if_data = {}

    # 重写父类的方法
    def if_check(self):
        if_filter_xml = ''' 
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper">
    <interface>
        <name/>
        <oper-status/>
    </interface>
  </interfaces>
</filter>
'''
        if_data = self.inst.get(filter=if_filter_xml).data_xml
        if_seg = [info.split('</interface>')[0] for info in if_data.split('<interface>')[1:]]
        for info in if_seg:
            if_name = info.split('<Name>')[1].split('</Name>')[0]
            if_state = info.split('<oper-status>')[1].split('</oper-status>')[0]
            if if_name.startswith('GigabitEthernet'):
                self.if_data[if_name] = if_state

    def if_update(self, if_name, if_state):
        if_config_xml = '''
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-interfaces-oper">
    <interface>
        <name>{}</name>
        <oper-status>{}</oper-status>
    </interface>
  </interfaces>
</config>
        '''.format(if_name, if_state)
        self.inst.edit_config(target='running', config=if_config_xml)
