# 路径参数 Order matters
# fixed

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/vlan/{vlan_info}")
async def read_vlan(vlan_info: int | str):
    if vlan_info.isdigit():
        return {"vlan_id": vlan_info}
    if type(vlan_info) is str:
        return {"vlan_name": vlan_info}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")