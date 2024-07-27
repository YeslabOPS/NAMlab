# Path parameters order matters

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/vlan/{vlan_info}")
async def read_vlan(vlan_info: int | str):
    if vlan_info.isdigit():
        return {"Vlan ID": vlan_info}
    if type(vlan_info) is str and not vlan_info.isdigit():
        return {"Vlan Name": vlan_info}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")