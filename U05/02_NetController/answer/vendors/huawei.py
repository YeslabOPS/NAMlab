from .default import BaseController

HOST = '华为设备IP'
USERNAME = '华为设备用户名'
PASSWORD = '华为设备密码'


class HuaweiController(BaseController):
    def __init__(self):
        super().__init__(HOST, USERNAME, PASSWORD, {'name': 'huaweiyang'})
        self.if_data = {}

    # 重写父类的方法
    def if_check(self):
        if_filter_xml = ''' 
    <filter type="subtree">
      <ifm xmlns="http://www.huawei.com/netconf/vrp/huawei-ifm">
        <interfaces>
          <interface>
            <ifName></ifName>
            <ifDynamicInfo>
              <ifPhyStatus></ifPhyStatus>
            </ifDynamicInfo>
          </interface>
        </interfaces>
      </ifm>
    </filter>

    '''
        if_data = self.inst.get(filter=if_filter_xml).data_xml
        if_seg = [info.split('</interface>')[0] for info in if_data.split('<interface>')[1:]]
        for info in if_seg:
            if_name = info.split('<ifName>')[1].split('</ifName>')[0]
            if_state = info.split('<ifPhyStatus>')[1].split('</ifPhyStatus>')[0]
            if if_name.startswith('GE'):
                self.if_data[if_name] = if_state

    def if_update(self, if_name, if_state):
        if_config_xml = '''
        <config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
          <ifm xmlns="http://www.huawei.com/netconf/vrp/huawei-ifm">
            <interfaces>
              <interface xc:operation="merge">
                <ifName>{}</ifName>
                <ifAdminStatus>{}</ifAdminStatus>
              </interface>
            </interfaces>
          </ifm>
        </config>
        '''.format(if_name, if_state)
        self.inst.edit_config(target='running', config=if_config_xml)
        return f"接口 {if_name} 已变更为 {if_state}"
