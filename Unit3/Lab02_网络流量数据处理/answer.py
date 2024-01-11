import pandas as pd
import plotly.express as px


class NetData:
    def __init__(self, file_path):
        # Task1. 读取数据文件
        self.file = pd.read_csv(file_path)
        print("数据包含{}行{}列".format(*self.file.shape))
        print(f"数据的列头：{self.file.columns}")

    def get_main_asn_list(self):
        # Task2. 获取主要的ASN数据（出现大于1次）并形成列表
        return [one for one in self.file.r_asn.value_counts() if one > 1]
    
    def proc_main_data(self, main_asn):
        self.main_data = {}
        # Task3. 获取主要ASN数据的累计访问次数
        for i in range(self.file.shape[0]):
            asn = self.file.r_asn[i]
            asn_str = str(asn)
            f = self.file.f[i]
            if asn in main_asn:
                if asn_str not in self.main_data.keys():
                    self.main_data[asn_str] = f
                else:
                    self.main_data[asn_str] += f

    def show_result(self):
        new_df = pd.DataFrame(self.main_data.items(), columns=['ASN', 'Visit'])
        fig = px.bar(new_df, x='ASN', y='Visit', color='Visit')
        fig.show()


if __name__ == "__main__":
    net = NetData('netdata.csv')
    main_asn = net.get_main_asn_list()
    net.proc_main_data(main_asn)
    net.show_result()
