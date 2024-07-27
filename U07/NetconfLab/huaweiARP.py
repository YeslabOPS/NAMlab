from ncclient import manager
import xmltodict

ip = "192.168.1.99"
nc_port = 830
nc_user = "netconf"
nc_pass = "Huawei123@"

# 1. 开启连接
nc_proc = manager.connect(host=ip,
                          port=nc_port,
                          username=nc_user,
                          password=nc_pass,
                          hostkey_verify=False,
                          device_params={'name': 'huaweiyang'})

def get_arp():
    Filter = '''
        <filter type="subtree">
          <arp xmlns="http://www.huawei.com/netconf/vrp/huawei-arp">
            <arpTables>
              <arpTable>
                <vrfName></vrfName>
                <ipAddr></ipAddr>
                <macAddr></macAddr>
              </arpTable>
            </arpTables>
          </arp>
        </filter>
    '''

    result = str(nc_proc.get(filter=Filter))
    xml_dict = xmltodict.parse(result)
    for info in xml_dict['rpc-reply']['data']['arp']['arpTables']['arpTable']:
        print(f'IP: {info['ipAddr']} | MAC: {info['macAddr']}')

get_arp()



