import uvicorn
from typing import Annotated
from fastapi import FastAPI, Header, Cookie, HTTPException

app = FastAPI()

@app.get("/network/automation")
async def network_automation(
    user_agent: Annotated[str | None, Header(description="Client's User-Agent")],
    session_token: Annotated[str | None, Cookie(description="Session authentication token")] = None,
):
    # 检查用户代理
    if user_agent:
        print(f"User-Agent: {user_agent}")
    else:
        raise HTTPException(status_code=400, detail="User-Agent header is required")

    # 检查会话令牌
    print(f"Session token: {session_token}")
    if session_token != "valid_token":
        raise HTTPException(status_code=403, detail="Invalid or missing session token")

    # 模拟一个网络自动化场景，比如获取网络设备的状态
    network_status = {
        "device1": "online",
        "device2": "offline",
        "device3": "maintenance",
    }

    return {
        "message": "Network automation task executed successfully",
        "network_status": network_status,
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")
