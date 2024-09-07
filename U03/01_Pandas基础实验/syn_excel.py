import pandas as pd

file_path = "http://192.168.0.145:9000/networkauto/inventory.xlsx"

df = pd.read_excel(file_path)
print(df.head())

for index in range(df.shape[0]):
    if df['设备最后备份时间'][index].startswith('2024.7.'):
        print(df['设备名称'][index])