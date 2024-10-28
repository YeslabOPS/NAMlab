from cisco import CiscoController

test_inst = CiscoController()
test_inst.if_update('3', 'down')
test_inst.if_check()
print(test_inst.if_data)
test_inst.close()