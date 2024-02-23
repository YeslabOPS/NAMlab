# 混合参数验证
import uvicorn
from typing import Annotated
from fastapi import FastAPI, Query, Path

app = FastAPI()


@app.get("/serial/{number}")
async def read_items(
        *,
        device_name: str = "Undefined",
        ip_address: Annotated[str | None, Query(regex='\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')] = None,
        limit: Annotated[int, Query(gt=0, lt=300)] = 100,
        number: Annotated[str | None, Path(min_length=7, max_length=13)]
):
    results = {"account": limit, "devices": []}
    results.update({"DeviceName": device_name,
                    "Serial": number})
    if ip_address:
        results.update(({"ManageIP": ip_address}))
    return results

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")