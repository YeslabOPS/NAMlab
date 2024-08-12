from huawei import HuaweiController

test_inst = HuaweiController()
test_inst.if_update('GE1/0/5', 'down')
test_inst.if_check()
print(test_inst.if_data)
test_inst.close()