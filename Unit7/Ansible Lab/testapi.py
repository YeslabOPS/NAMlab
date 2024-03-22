# Body验证
import uvicorn
from typing import Annotated
from fastapi import Body, FastAPI

app = FastAPI()


@app.post("/api/alert", status_code=201)
async def read_alert(alert_msg: Annotated[str | dict | None, Body()] = None):
    print(alert_msg)
    return {"Get Alert": "OK"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")