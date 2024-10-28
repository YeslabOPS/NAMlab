import random
import datetime
from vendors.cisco import CiscoController
from vendors.huawei import HuaweiController



cisco_robot = CiscoController()
huawei_robot = HuaweiController()

op_list = ['up', 'down']
cisco_if_list = ['0', '1', '2', '3', '4']
huawei_if_list = ['GE1/0/0',
                  'GE1/0/1',
                  'GE1/0/2',
                  'GE1/0/3',
                  'GE1/0/4',
                  'GE1/0/5',
                  'GE1/0/6',
                  'GE1/0/7',
                  'GE1/0/8',
                  'GE1/0/9',]

def sim_logic(cisco_if_num, huawei_if_num):

    # 给思科设备指定接口随机UP/DOWN
    op = op_list[random.randint(0, 1)]
    cisco_robot.if_update(cisco_if_list[cisco_if_num], op)
    cisco_robot.if_check()

    # 给华为设备指定接口随机UP/DOWN
    op = op_list[random.randint(0, 1)]
    huawei_robot.if_update(huawei_if_list[huawei_if_num], op)
    huawei_robot.if_check()


def report():
    now = (str(datetime.datetime.now()).split('.')[0]
           .replace(':', '_')
           .replace(' ', '_')
           .replace('-', '_'))
    cisco_msg = "<h2>思科交换机接口状态</h2><table><tr><th>接口</th><th>状态</th></tr>{}</table>"
    huawei_msg = "<h2>华为交换机接口状态</h2><table><tr><th>接口</th><th>状态</th></tr>{}</table>"

    # 创建思科报告部分
    cisco_content = []
    for if_name, if_status in cisco_robot.if_data.items():
        cisco_raw = f'<tr><td>{if_name}</td><td class="{if_status}">{if_status.upper()}</td></tr>'
        cisco_content.append(cisco_raw)
    cisco_report = cisco_msg.format(''.join(cisco_content))

    # 创建华为报告部分
    huawei_content = []
    for if_name, if_status in huawei_robot.if_data.items():
        huawei_raw = f'<tr><td>{if_name}</td><td class="{if_status}">{if_status.upper()}</td></tr>'
        huawei_content.append(huawei_raw)
    huawei_report = huawei_msg.format(''.join(huawei_content))

    # 拼接完成报告
    with open('temp_head.txt') as f:
        report_start = f.read()
    with open('temp_end.txt') as f:
        report_end = f.read()
    full_report = report_start + '\n' + cisco_report + '\n' + huawei_report + '\n' + report_end
    with open(f'reports/{now}.html', 'w') as f:
        f.write(full_report)


if __name__ == '__main__':
    sim_logic(3, 5)
    report()