# Query parameters

from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/vlan")
async def read_vlan(id: str, name: str | None = None):
    if name:
        return {"Vlan Name": name, "Vlan ID": id}
    return {"Vlan ID": id}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")