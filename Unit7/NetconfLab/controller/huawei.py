from ncclient import manager

class Huawei:
    def __init__(self):
        ip = "192.168.1.99"
        nc_port = 830
        nc_user = "netconf"
        nc_pass = "Huawei123@"
        self.nc_proc = manager.connect(host=ip,
                                       port=nc_port,
                                       username=nc_user,
                                       password=nc_pass,
                                       hostkey_verify=False,
                                       device_params={'name': 'huaweiyang'})

    def manage_if(self, ifname, ifip, ifmask, action):
        XML = '''
        <config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
          <ifm xmlns="http://www.huawei.com/netconf/vrp/huawei-ifm">
            <interfaces>
              <interface xc:operation="{}">
                <ifName>{}</ifName>
                <ipv4Config>
                  <am4CfgAddrs>
                    <am4CfgAddr>
                      <ifIpAddr>{}</ifIpAddr>
                      <subnetMask>{}</subnetMask>
                      <addrType>main</addrType>
                    </am4CfgAddr>
                  </am4CfgAddrs>
                </ipv4Config>
              </interface>
            </interfaces>
          </ifm>
        </config>
        '''.format(action, ifname, ifip, ifmask)
        resp = str(self.nc_proc.edit_config(target='running', config=XML))
        return resp