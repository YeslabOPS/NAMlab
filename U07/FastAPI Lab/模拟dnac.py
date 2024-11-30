# Path parameters
from fastapi import FastAPI
import uvicorn

app = FastAPI()


def get_device_info(id):
    data = {'version': '1.0',
            'id': id,
            'response': {
                'apEthernetMacAddress': '010101010101',
                'apManagerInterfaceIp': '1.1.1.1'
                }
            }
    return data


@app.get("/dna/intent/api/v1/network-device/{id}")
async def get_device(id: int):
    result = get_device_info(id)
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")