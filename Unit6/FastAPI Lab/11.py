# 安全认证
import uvicorn
import hashlib
from typing import Annotated
from fastapi import FastAPI, Header, HTTPException

app = FastAPI()
auth_hosts = []


@app.post("/auth", status_code=201)
async def auth_user(username: str, password: str):
    combined_str = username + password
    # 使用 MD5 哈希函数计算哈希值
    token = hashlib.md5(combined_str.encode()).hexdigest()
    auth_hosts.append(token)
    print(auth_hosts)
    return {"X-Token": token}


@app.get("/alerts")
async def read_alerts(x_token: Annotated[str | None, Header()] = None):
    print(x_token)
    if x_token in auth_hosts:
        return {"Alerts": ["一大堆告警正在袭来!"]}
    #return {"Errors": ["认证失败！"]}
    raise HTTPException(status_code=403, detail="请先做认证")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")