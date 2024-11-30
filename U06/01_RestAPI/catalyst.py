import time
import requests
from requests.auth import HTTPBasicAuth

# 禁用SSL警告
requests.packages.urllib3.disable_warnings()

class DNAC:
    def __init__(self, url, username, password):
        self.url = url
        token = self.get_dnac_token(username, password)
        self.headers = {
            "Content-Type": "application/json",
            "X-Auth-Token": token
        }
        self.protocol = 'icmp'
        self.inclusions = ['INTERFACE-STATS',
                           'DEVICE-STATS',
                           'ACL-TRACE',
                           'QOS-STATS']
        self.ip_list = self.get_devices_ip()
        self.fid = None

    # 获取DNAC的认证Token
    def get_dnac_token(self, username, password):
        url = f"{self.url}/dna/system/api/v1/auth/token"
        response = requests.post(url, auth=HTTPBasicAuth(username, password), verify=False)
        token = response.json()["Token"]
        return token

    # 获取网络设备信息
    def get_devices_ip(self):
        url = f"{self.url}/dna/intent/api/v1/network-device"
        response = requests.get(url, headers=self.headers, verify=False)
        return [info['managementIpAddress'] for info in response.json()['response']]

    # 获取路径追踪摘要
    def get_path_trace_summary(self):
        url = f"{self.url}/dna/intent/api/v1/flow-analysis"
        response = requests.get(url, headers=self.headers, verify=False)
        return response.json()['response']

    # 获取路径追踪
    def get_path_trace_result(self, flow_analysis_id):
        url = f"{self.url}/dna/intent/api/v1/flow-analysis/{flow_analysis_id}"
        response = requests.get(url, headers=self.headers, verify=False)
        return response.json()['response']
    
    # 删除已有路径追踪进程
    def del_old_flow_trace_task(self, ip_list):
        # 获取已有路径追踪进程id
        for ip in ip_list:
            _path_trace_summary = self.get_path_trace_summary()
            old_flow_ids = [_summary['id'] for _summary in _path_trace_summary]
            # 删除目标IP相关的已存在路径追踪进程
            for old_flow_id in old_flow_ids:
                url = f"{self.url}/dna/intent/api/v1/flow-analysis/{old_flow_id}"
                requests.delete(url, headers=self.headers, verify=False)
        return "消息: 历史路径追踪任务已删除"

    # 开启路径追踪
    def start_path_trace(self, src_ip, dst_ip):
        url = f"{self.url}/dna/intent/api/v1/flow-analysis"
        payload =  {"destIP": dst_ip,
                    "sourceIP": src_ip,
                    "protocol": self.protocol,
                    "inclusions": self.inclusions,
                   }
        response = requests.post(url, json=payload, headers=self.headers, verify=False)
        return response.json()['response']['flowAnalysisId']
    
    # 端到端路径获取
    def trace_src_dst(self, src_ip, dst_ip):
        # 两点之间开启新的路径追踪进程
        self.fid = self.start_path_trace(src_ip, dst_ip)
        # 等待进程跑完
        time.sleep(10)
        # 获取进程中的路径信息
        path_infos = self.get_path_trace_result(self.fid)
        return path_infos
    
