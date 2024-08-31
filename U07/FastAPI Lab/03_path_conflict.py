# Path parameters order matters
# Error

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/vlan/{vlan_id}")
async def read_vlan(vlan_id: int):
    return {"Vlan ID": vlan_id}


@app.get("/vlan/{vlan_name}")
async def read_vlan(vlan_name: str):
    return {"Vlan Name": vlan_name}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")