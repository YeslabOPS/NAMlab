import time
import numpy as np
from utils import DataWriter

cisco_writer = DataWriter()

# CPU使用率、内存利用率、
def low_high_random(low, high):
    return np.random.rand()*(high - low) + low


# 假设这是一台交换机
def topo(name):
    print(f"Topo - {name} 开始监控！")
    line1 = np.random.rand()
    line2 = np.random.rand()
    line3 = np.random.rand()
    cpu = low_high_random(9,99)

    cisco_writer.write_ts_data("dc1_line1", ("line1_payload", line1))
    cisco_writer.write_ts_data("dc1_line2", ("line2_payload", line2))
    cisco_writer.write_ts_data("dc1_line3", ("line3_payload", line3))
    cisco_writer.write_ts_data("dc1_sw_1", ("sw1_cpu", cpu))

while True:
    topo('DC1')
    time.sleep(10)