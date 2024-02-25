# Pre-defined path parameters

from fastapi import FastAPI
from enum import Enum
import uvicorn


class IfType(str, Enum):
    if_eth = "e"
    if_geth = "g"
    other = "无法识别接口类型"

app = FastAPI()

#e1_0_1
#g1_0_1

@app.get("/interface/{if_name}")
async def read_vlan(if_name: str):
    if if_name.split('_')[0][:-1] == IfType.if_eth:
        if_full_name = if_name.replace('e', 'Ethernet').replace('_', '/')
    elif if_name.split('_')[0][:-1] == IfType.if_geth:
        if_full_name = if_name.replace('g', 'Gigabit Ethernet').replace('_', '/')
    else:
        if_full_name = IfType.other
    return {"您查询的接口": if_full_name}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")