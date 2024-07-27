import pandas as pd
import plotly.express as px


class NetData:
    def __init__(self, file_path):
        # Task1. 读取数据文件
        self.file = 
        print("数据包含{}行{}列".format(*self.file.shape))
        print(f"数据的列头：{self.file.columns}")

    def get_main_asn_list(self):
        # Task2. 获取主要的ASN数据（出现大于1次）并形成列表
        

    
    def proc_main_data(self, main_asn):
        self.main_data = {}
        # Task3. 获取主要ASN数据的累计访问次数
        


    def show_result(self):
        new_df = pd.DataFrame(self.main_data.items(), columns=['ASN', 'Visit'])
        fig = px.bar(new_df, x='ASN', y='Visit', color='Visit')
        fig.show()


if __name__ == "__main__":
    net = NetData('netdata.csv')
    main_asn = net.get_main_asn_list()
    net.proc_main_data(main_asn)
    net.show_result()
