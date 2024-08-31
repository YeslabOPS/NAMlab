# 查询参数添加验证
import uvicorn
from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/serial")
async def read_items(serial: Annotated[str | None, Query(min_length=7, max_length=13)] = None):
    results = {"devices": [{"device_name": "Core_Switch"}, {"ip_address": "1.1.1.1"}]}
    if serial:
        results.update({"serial": serial})
    return results

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")