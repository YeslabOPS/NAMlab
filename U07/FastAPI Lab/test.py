import requests

# 设置请求的 URL
url = "http://localhost:5000/upload/"

# 打开要上传的文件
with open("1.txt", "rb") as f:
    # 发送 POST 请求，包含文件
    response = requests.post(url, files={"file": ("1.txt", f)})

# 检查响应状态码
if response.status_code == 200:
    print("文件上传成功！")
    print(response.json())  # 打印响应内容
else:
    print("文件上传失败，状态码：", response.status_code)
    print(response.text)  # 打印错误信息