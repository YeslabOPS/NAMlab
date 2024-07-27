import time
import numpy as np
from utils import DataWriter

cisco_writer = DataWriter()

# CPU使用率、内存利用率、
def low_high_random(low, high):
    return np.random.rand()*(high - low) + low

# 丢包数量
def rand_int(max_value):
    return np.random.randint(0,max_value)
    
# 假设这是一台交换机
def device_1(name):
    print(f"Device - {name} 开始监控！")
    cpu1 = low_high_random(43, 80)
    cpu2 = low_high_random(35, 67)
    memory = low_high_random(18, 85)
    g1_drop_tx_ps = 0
    g1_drop_rx_ps = rand_int(10)
    g2_drop_tx_ps = 0
    g2_drop_rx_ps = 0
    g1_tx_bandwidth_utilization = rand_int(90)
    g1_rx_bandwidth_utilization = rand_int(100)
    g2_tx_bandwidth_utilization = rand_int(60)
    g2_rx_bandwidth_utilization = rand_int(60)
    g1_tx_queue = 0
    g1_rx_queue = rand_int(100)
    g2_tx_queue = 0
    g2_rx_queue = 0
    
    metric_list = [cpu1, cpu2, memory, g1_drop_tx_ps, g1_drop_rx_ps, g2_drop_tx_ps, g2_drop_rx_ps, memory, g1_tx_bandwidth_utilization, g1_rx_bandwidth_utilization, g2_tx_bandwidth_utilization, g2_rx_bandwidth_utilization, g1_tx_queue, g1_rx_queue, g2_tx_queue, g2_rx_queue]
    name_list = ['cpu1', 'cpu2', 'memory', 'g1_drop_tx_ps', 'g1_drop_rx_ps', 'g2_drop_tx_ps', 'g2_drop_rx_ps', 'memory', 'g1_tx_bandwidth_utilization', 'g1_rx_bandwidth_utilization', 'g2_tx_bandwidth_utilization', 'g2_rx_bandwidth_utilization', 'g1_tx_queue', 'g1_rx_queue', 'g2_tx_queue', 'g2_rx_queue']

    for i in range(len(metric_list)):
        cisco_writer.write_ts_data("demo_device", (name_list[i], metric_list[i]))
        
while True:
    device_1('cisco_switch')
    time.sleep(10)