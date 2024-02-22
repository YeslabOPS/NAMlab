# Order matters
# error

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/vlan/{vlan_id}")
async def read_vlan(vlan_id: int):
    return {"vlan_id": vlan_id}


@app.get("/vlan/{vlan_name}")
async def read_vlan(vlan_name: str):
    return {"vlan_name": vlan_name}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")