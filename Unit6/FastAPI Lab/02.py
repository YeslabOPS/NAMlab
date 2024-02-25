# Path parameters
from fastapi import FastAPI
import uvicorn

app = FastAPI()


def check_vlan(vlan_id):
    print(f'check vlan {vlan_id}')


@app.get("/vlan/{vlan_id}")
async def read_vlan(vlan_id: int):
    check_vlan(vlan_id)
    return {"Vlan ID": vlan_id}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")