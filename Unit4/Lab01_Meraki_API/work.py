import requests
import pandas as pd
from utils import sql_writer


class Meraki:
    def __init__(self, token):
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}",
                        "Accept": "application/json"}
        self.url = "https://api.meraki.com/api/v1"
        self.oid = self.get_org_list()[0]['id']

    def get_org_list(self):
        url = self.url + '/organizations'
        resp = requests.get(url, headers=self.headers)
        return resp.json()
    
    def create_device_info(self):
        ## 作业部分开始
        #TODO: 补完下面的代码
        url = self.url + 
        resp = 
        device_list = 
        ## 作业部分结束
        col_list = ['serial', 'mac', 'networkId', 'status', 'productType', 'model']
        device_info_list = []
        for device in device_list:
            device_info = [device[one] for one in col_list]
            device_info_list.append(device_info)
        self.pd_data = pd.DataFrame(device_info_list, columns=col_list)
        sql_writer(self.pd_data, 'DeviceStatus')

    def vis_device_location(self):
        ## 作业部分开始
        #TODO: 补完下面的代码
        url = self.url + 
        serial_list = 
        ## 作业部分结束
        loc_table = []
        for serial in serial_list:
            resp = requests.get(url.format(serial), headers=self.headers)
            if resp.text == '':
                continue
            result = resp.json()
            lat = result["lat"]
            lng = result["lng"]
            loc_table.append([serial, lat, lng])
        pd_data = pd.DataFrame(loc_table, columns=['Device', 'Lat', 'Lng'])
        sql_writer(pd_data, 'DeviceLoc')
