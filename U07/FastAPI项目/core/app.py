import uvicorn
import requests
import asyncio
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
db = {}

def run_app():
    host = "http://127.0.0.1:5000"
    monitor_url = host + "/api/monitor"
    auto_url = host + "/api/auto"
    monitor_data = {
        "monitor_cmd": "show ip route",
        "is_send_back": True,
        "send_idle": 10
    }
    try:
        resp = requests.post(monitor_url, json=monitor_data)
        print(f"Monitor response: {resp.status_code}, {resp.text}")
    except Exception as e:
        print(f"Error in monitor request: {e}")

    auto_data = {
        "cmd_list": ['inter lo1', 'ip add 101.101.101.101 255.255.255.0']
    }
    try:
        resp = requests.post(auto_url, json=auto_data)
        print(f"Auto response: {resp.status_code}, {resp.text}")
    except Exception as e:
        print(f"Error in auto request: {e}")


class Data(BaseModel):
    response: dict
    agent_name: str

@app.post("/api/data")
async def add_data(data: Data):
    db[data.agent_name] = data.response['data']
    return 'status: OK'

@app.get("/api/data")
async def show_history():
    return db

@app.on_event("startup")
async def startup_event():
    run_app()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000, log_level="info")
