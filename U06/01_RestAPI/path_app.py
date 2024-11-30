import logging
import time
from catalyst import DNAC

# 初始化日志
logging.basicConfig(filename='catalyst.log',
                    level=logging.INFO,
                    format = '%(asctime)s  %(filename)s : %(levelname)s  %(message)s',
                    datefmt = '%Y-%m-%d %A %H:%M:%S')

logging.info('Catalyst Path Tracer App Start!')

# DNAC的URL和凭据
DNAC_URL = "https://sandboxdnac.cisco.com"
USERNAME = "devnetuser"
PASSWORD = "Cisco123!"

dnac = DNAC(DNAC_URL, USERNAME, PASSWORD)


# 全网追踪
def trace_all():
    # 删除旧的路径追踪进程
    print("正在清空旧的监控进程，请稍后...")
    dnac.del_old_flow_trace_task(dnac.ip_list)
    # 设置一个源IP位置
    off_set = 1
    # 取所有不重复IP组合
    for src_ip in dnac.ip_list:
        for dst_ip in dnac.ip_list[off_set:]:
            print("-" * 20)
            print("正在追踪从{}到{}的路径信息:".format(src_ip, dst_ip))
            # 进行两点之间的路径追踪
            net_path = dnac.trace_src_dst(src_ip, dst_ip)
            log_info = src_ip + "," + dst_ip + "," + ">".join(net_path) + "\n"
            logging.info(log_info)
            print(net_path)
            print("-" * 20)
            print("\n")
        off_set += 1

def a2b_monitor(src_ip, dst_ip):
    # 删除旧的路径追踪进程
    print("正在清空旧的监控进程，请稍后...")
    dnac.del_old_flow_trace_task([src_ip, dst_ip])
    print("开始对{}到{}之间进行链路监控\n".format(src_ip, dst_ip))
    # 进行两点之间的路径追踪
    path_infos = dnac.trace_src_dst(src_ip, dst_ip)
    issues = analysis(src_ip, path_infos)
    print(f'本次监控发现问题：{issues}')

    # 循环监控时把下面的注释取消并继续编写巡检监控的可视化、数据存储等代码
    '''
    while True:
        issues = analysis(src_ip, path_infos)
        print(f'本次监控发现问题：{issues}')
        time.sleep(60)
        del path_infos
        path_infos = dnac.get_path_trace_result(dnac.fid)
    '''

def analysis(src_ip, path_infos):
    issues = []
    for device_info in path_infos['networkElementsInfo']:
        device_name = device_info['name']
        logging.info(f'Start Checking {device_name}')
        # 接口状态
        if 'ingressInterface' in device_info.keys():
            device_int_status = device_info['ingressInterface']['physicalInterface']['interfaceStatistics'][
                'adminStatus']
        elif 'egressInterface' in device_info.keys():
            device_int_status = device_info['egressInterface']['physicalInterface']['interfaceStatistics'][
                'adminStatus']
        else:
            device_int_status = 'up'

        # 设备内存
        device_total_mem = device_info['deviceStatistics']['memoryStatistics']['totalMemory']
        device_used_mem = device_info['deviceStatistics']['memoryStatistics']['memoryUsage']
        device_free_mem = device_total_mem - device_used_mem
        log_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        log_info = (log_time + "," + src_ip + "," + device_name +
                    "," + device_int_status + "," + str(device_free_mem) + "\n")
        logging.info(log_info)
        if device_int_status != "up":
            issue = f"{device_name}设备的接口出现问题，请尽快处理！"
            if issue not in issues:
                issues.append(issue)
        if device_free_mem < 1000000000:
            issue = f"{device_name}设备剩余内存较低，请尽快处理！"
            if issue not in issues:
                issues.append(issue)
    return issues

# 请分别测试下面的用例
#trace_all()
a2b_monitor('10.10.20.177','10.10.20.178')