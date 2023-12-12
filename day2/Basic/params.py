ip_list = ['1.1.1.1', '2.2.2.2', '3.3.3.3']
device_dict = {'ip':'1.1.1.1', 'name':'cisco'}

def test(*args, **kwargs):
    print(args[1])

test(*ip_list)