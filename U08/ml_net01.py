import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv('data/optical_interconnection_network.csv', delimiter=';')
print(data.head())
print(f'Shape of Data: {data.shape}')

# 数据处理
def data_process(ori_data, onehot_fields):
    for each in onehot_fields:
        onehot = pd.get_dummies(ori_data[each], prefix=each, drop_first=False)
        ori_data = pd.concat([ori_data, onehot], axis=1)
    print(ori_data.shape)
    data = ori_data.drop(onehot_fields, axis=1)
    print(data.shape)
    return data

onehot_fields = ['Node Number', 'Thread Number', 'Spatial Distribution', 'Temporal Distribution']
dataset = data_process(data, onehot_fields)
dataset = dataset.astype(np.float64)

print(dataset.head())

data = dataset.drop(['Input Waiting Time'], axis=1).values
target = dataset['Input Waiting Time'].values

def ai(data, target):
    x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.2)
    print(f"X for \nTrain: {x_train.shape}\nTest: {x_test.shape}")
    print(f"Y for \nTrain: {y_train.shape}\nTest: {y_test.shape}")
    
    model = LinearRegression()
    model.fit(x_train, y_train)
    
    result = model.score(x_test, y_test)
    print("模型的测试准确率为{:.2f}%".format(result*100))
    y_pred = model.predict(x_test)
    
    y_pred = model.predict(x_test)
    np_datas = np.vstack([y_pred, y_test]).T
    pd_result = pd.DataFrame(np_datas, columns=["预测输入等待时间", "真实输入等待时间"])
    
    fig = px.line(data_frame=pd_result)
    fig.show()

ai(data, target)