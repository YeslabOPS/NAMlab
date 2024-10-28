from .default import BaseController

HOST = '思科设备IP'
USERNAME = '思科设备用户名'
PASSWORD = '思科设备密码'

IfState2updown = {'if-oper-state-ready': 'up',
                  'if-oper-state-lower-layer-down': 'up',
                  'if-oper-state-no-pass': 'down'}


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
            if_name = info.split('<name>')[1].split('</name>')[0]
            if_state = info.split('<oper-status>')[1].split('</oper-status>')[0]
            if if_name.startswith('GigabitEthernet'):
                self.if_data[if_name] = IfState2updown[if_state]

    def if_update(self, if_number, if_updown):
        if if_updown == 'down':
            if_updown = '<shutdown/>'
        elif if_updown == 'up':
            if_updown = '<shutdown operation="remove"/>'
        else:
            return '错误操作，请输入up或者down'

        if_config_xml = '''
        <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <interface>
                    <GigabitEthernet>
                        <name>{}</name>
                        {}
                    </GigabitEthernet>
                </interface>
            </native>
        </config>
        '''.format(if_number, if_updown)
        self.inst.edit_config(target='candidate', config=if_config_xml)
        self.inst.commit()
        return f"接口 GigabitEthernet {if_number} 已变更为 {if_updown}"
