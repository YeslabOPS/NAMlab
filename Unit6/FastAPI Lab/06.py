# 可选查询参数与必选查询参数

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/vlan")
async def read_item(id: str, desc: str | None = None):
    if desc:
        return {f"Vlan {id}": desc}
    return {f"Vlan {id}": "No Desc"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")