import xmltodict
from fastapi import FastAPI
from pydantic import BaseModel
from huawei import Huawei
from cisco import Cisco

app = FastAPI()

huawei_actor = Huawei()
cisco_actor = Cisco()


class Interface(BaseModel):
    ifname: str
    ifip: str
    ifmask: str ='255.255.255.0'


@app.post("/api/cisco/loopback")
async def cisco_loop(request_body: Interface):
    result = cisco_actor.manage_if(request_body.ifname,
                                   request_body.ifip,
                                   request_body.ifmask,
                                   action='merge')
    if 'ok' in xmltodict.parse(result)['rpc-reply']:
        return {'message': f'Interface {request_body.ifname} has been merged'}
    return {'message': 'Failed'}


@app.post("/api/huawei/loopback")
async def huawei_loop(request_body: Interface):
    result = huawei_actor.manage_if(request_body.ifname,
                                    request_body.ifip,
                                    request_body.ifmask,
                                    action='merge')
    if 'ok' in xmltodict.parse(result)['rpc-reply']:
        return {'message': f'Interface {request_body.ifname} has been merged'}
    return {'message': 'Failed'}


@app.delete("/api/huawei/loopback")
async def huawei_remove(request_body: Interface):
    result = huawei_actor.manage_if(request_body.ifname,
                                    request_body.ifip,
                                    request_body.ifmask,
                                    action='remove')
    if 'ok' in xmltodict.parse(result)['rpc-reply']:
        return {'message': f'Interface {request_body.ifname} has been removed'}
    return {'message': 'Failed'}