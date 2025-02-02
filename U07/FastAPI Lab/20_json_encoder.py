# JSON数据适配
import uvicorn
from datetime import datetime

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

fake_db = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None


app = FastAPI()


@app.put("/items/{id}")
async def update_item(id: str, item: Item):
    print(type(item))
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")