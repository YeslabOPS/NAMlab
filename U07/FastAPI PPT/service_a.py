import uvicorn
import hashlib
from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from typing import Literal, Annotated

app = FastAPI()
auth_hosts = []
device_db = []

# 定义请求体模型
class InterfaceInfo(BaseModel):
    if_name: str
    if_description: str | None
    if_status: Literal["up", "down"]  # 限制取值为 "up" 或 "down"

class AuthCredentials(BaseModel):
    # 认证API需要的字段
    username: str
    password: str

# 接口信息上报API
@app.put("/api/interfaces")
async def report_interface_info(interface_info: InterfaceInfo,
                                x_token: Annotated[str | None, Header()] = None):
    if x_token in auth_hosts:
        device_db.append(interface_info)
        return {"message": "Interface info received"}
    raise HTTPException(status_code=403, detail="请先做认证")

# 上报历史查询API
@app.get("/api/history")
async def get_history(x_token: Annotated[str | None, Header()] = None):
    if x_token in auth_hosts:
        return {"message": device_db}
    raise HTTPException(status_code=403, detail="请先做认证")

# 认证API
@app.post("/auth", status_code=201)
async def auth_user(username: str, password: str):
    combined_str = username + password
    # 使用 MD5 哈希函数计算哈希值
    token = hashlib.md5(combined_str.encode()).hexdigest()
    auth_hosts.append(token)
    print(auth_hosts)
    return {"X-Token": token}

# 运行Uvicorn服务器
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=30002)