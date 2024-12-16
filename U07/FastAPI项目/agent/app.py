# POST 消息正文与内容类型定义
import uvicorn
import uuid
import datetime
import requests
from network import cisco_send, cisco_config, Record
from fastapi import FastAPI
from pydantic import BaseModel


# Cred
ip = '192.168.0.221'
username = 'ciscouser'
password = 'cisco@123'

# Request Body Model
class Monitor(BaseModel):
    monitor_cmd: str
    is_send_back: bool = True
    send_idle: int = 10

class Auto(BaseModel):
    cmd_list: list


app = FastAPI()
record = Record()

def send_data(data):
    #url = "http://192.168.0.145:5000/api/data"
    url = "http://127.0.0.1:10000/api/data"
    resp = requests.post(url, json=data)
    if resp.ok:
        print('已发送数据')
    else:
        print(resp.status_code)


@app.post("/api/monitor")
async def add_monitor(monitor_config: Monitor):
    cmd = monitor_config.monitor_cmd
    data = cisco_send(cmd, ip, username, password)
    result = {"response":
                {"taskId": str(uuid.uuid4()),
                 "data": data
                },
              "task_time": str(datetime.datetime.now()).split('.')[0],
              "agent_name": "ShenzhenDC"
             }
    record.history["monitor_history"]["taskId"] = result["response"]["taskId"]
    record.history["monitor_history"]["taskTime"] = result["task_time"]
    print(result)
    send_data(result)
    return 'status: OK'

@app.post("/api/auto")
async def add_auto(auto_cmd: Auto):
    print(auto_cmd)
    cisco_config(auto_cmd.cmd_list, ip, username, password)
    result = {"response":
                {"taskId": str(uuid.uuid4())},
              "task_time": str(datetime.datetime.now()).split('.')[0]
             }
    record.history["automation_history"]["taskId"] = result["response"]["taskId"]
    record.history["automation_history"]["taskTime"] = result["task_time"]
    return 'status: OK'

@app.get("/api/history")
async def show_history():
    return record.history


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")