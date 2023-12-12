print("开始写代码")

# 7种数据结构
## 4种单体数据结构
one_int = 123 #整数 int
one_float = 1.23 #浮点数 float
one_str = "你好！北京！" #字符串
one_bool = True #布尔值

## 3种常见的数组型数据结构
one_list = [one_int, one_float, "我来了广州", False] #要放的东西只有一个维度 | 多个成套的东西弄成一个组 | 多维不带键值的数据
one_tuple = (one_int, one_float, "我来了广州", False)
one_dict = {'ip': '1.1.1.1',
            'device_name': 'CiscoCSR1000V',
            'interfaces': [{'name': 'GE1/0/1', 'status': 'L2'},
                           {'name': 'GE1/0/2', 'status': 'L3'}]
            } #多维带键值数据

