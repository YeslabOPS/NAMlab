import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]

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
pd_result = pd.DataFrame(np_datas, columns=["预测房价", "真实房价"])

fig = px.line(data_frame=pd_result)
fig.show()