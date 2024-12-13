import uvicorn
from typing import Union
from fastapi import Depends, FastAPI

app = FastAPI()


# 通用参数依赖，用于处理网络设备的查询参数
async def network_query_parameters(
    device_type: Union[str, None] = None, 
    status: Union[str, None] = None, 
    limit: int = 10, 
    offset: int = 0
):
    return {"device_type": device_type, "status": status, "limit": limit, "offset": offset}


@app.get("/devices/")
async def get_devices(params: dict = Depends(network_query_parameters)):
    # 模拟返回网络设备列表
    devices = [
        {"id": 1, "name": "Router1", "type": "Router", "status": "Active"},
        {"id": 2, "name": "Switch1", "type": "Switch", "status": "Inactive"},
        {"id": 3, "name": "Firewall1", "type": "Firewall", "status": "Active"},
    ]
    # 根据查询参数过滤设备
    filtered_devices = [
        device for device in devices
        if (not params["device_type"] or device["type"] == params["device_type"])
        and (not params["status"] or device["status"] == params["status"])
    ]
    # 实现分页
    return filtered_devices[params["offset"]:params["offset"] + params["limit"]]


@app.get("/logs/")
async def get_logs(params: dict = Depends(network_query_parameters)):
    # 模拟返回日志列表
    logs = [
        {"id": 1, "device": "Router1", "message": "Interface up", "status": "Active"},
        {"id": 2, "device": "Switch1", "message": "Interface down", "status": "Inactive"},
        {"id": 3, "device": "Firewall1", "message": "Policy updated", "status": "Active"},
    ]
    # 根据查询参数过滤日志
    filtered_logs = [
        log for log in logs
        if (not params["device_type"] or log["device"] == params["device_type"])
        and (not params["status"] or log["status"] == params["status"])
    ]
    # 实现分页
    return filtered_logs[params["offset"]:params["offset"] + params["limit"]]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")
