import pandas as pd

# 创建初始 DataFrame
data = {
    'IP地址': ['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4'],
    '响应时间(ms)': [10, 15, 7, 12],
    '状态': ['正常', '正常', '正常', '异常']
}

df = pd.DataFrame(data)
print("初始 DataFrame:")
print(df)

# 使用 iloc 和 loc 索引数据
print("\n使用 iloc 索引第2行的数据：")
print(df.iloc[1])

print("\n使用 loc 索引第2行的数据：")
print(df.loc[1])

print("\n使用 loc 索引IP地址和状态的数据：")
print(df.loc[:, ['IP地址', '状态']])

# 插入新列
df['制造商'] = ['Cisco', 'Juniper', 'Cisco', 'Huawei']
print("\n插入新列后的 DataFrame:")
print(df)

# 插入新行
new_row = {'IP地址': '192.168.1.5', '响应时间(ms)': 20, '状态': '正常', '制造商': 'Cisco'}
df = df.append(new_row, ignore_index=True)
print("\n插入新行后的 DataFrame:")
print(df)

# 使用 value_counts 对数据进行统计
print("\nIP地址 出现次数统计:")
print(df['IP地址'].value_counts())

print("\n状态 出现次数统计:")
print(df['状态'].value_counts())

print("\n制造商 出现次数统计:")
print(df['制造商'].value_counts())
