from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def hello():
    return {"DeviceOS_Version": "Cisco IOSXE 17.01"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")

