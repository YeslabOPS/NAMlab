import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# 模拟的设备数据库
devices = {
    "device1": {"name": "Router1", "status": "active"},
    "device2": {"name": "Switch1", "status": "inactive"},
}


# 请求模型
class UpdateConfigRequest(BaseModel):
    device_id: str
    config: dict


@app.post("/update-config")
async def update_config(request: UpdateConfigRequest):
    # 检查设备是否存在
    if request.device_id not in devices:
        raise HTTPException(status_code=404, detail=f"Device {request.device_id} not found")

    # 检查配置是否有效（仅作为示例，实际验证逻辑更复杂）
    if not request.config or not isinstance(request.config, dict):
        raise HTTPException(status_code=400, detail="Invalid configuration format")

    try:
        # 模拟更新设备配置的逻辑
        devices[request.device_id]["config"] = request.config
        return {"message": f"Configuration updated successfully for {request.device_id}"}
    except Exception as e:
        # 捕获任何其他异常，返回500
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@app.get("/")
async def root():
    return {"message": "Network Automation API is running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")
