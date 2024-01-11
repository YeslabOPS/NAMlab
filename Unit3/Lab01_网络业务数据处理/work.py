import json
import pandas as pd

# json_to_excel: 将导入的JSON文件转换为Excel表格
'''
[Params]
file_path(str): JSON文件的路径
col_names(list): 生成的Excel表格的列头名称
excel_file(str): 生成的Excel表格文件的路径
'''
def json_to_excel(file_path, col_names, excel_file):
    # 导入JSON文件
    with open(file_path) as f:
        json_data = json.load(f)
    data_list = [] #一级列表
    ## Task1.按照每个工单数据来取需要的数值


    ## Task2.通过Pandas的DataFrame输出Excel文件



if __name__ == "__main__":
    ## Task3.设定列头名称并执行函数