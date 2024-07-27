# POST 消息正文与内容类型定义

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


# Request Body Model
class MemberTemplateDeploymentInfo(BaseModel):
    targetInfo: list
    hostName: str
    id: str
    type: str
    versionedTemplateId: str
    resourceParams: object
    params: object


class TemplateDeploymentInfo(BaseModel):
    mainTemplateId: str | None = None
    templateId: str | None = None
    forcePushTemplate: bool
    isComposite: bool
    memberTemplateDeploymentInfo: list[MemberTemplateDeploymentInfo] | None = None


# Response Body Model
class Response(BaseModel):
    taskId: int
    url: str | None = None


class TaskIdResult(BaseModel):
    response: Response
    version: str | None = None


app = FastAPI()


@app.post("/dna/intent/api/v2/template-programmer/template/deploy", response_model=TaskIdResult)
async def deploy_temp(deploy_data: TemplateDeploymentInfo):
    print(deploy_data)
    result = {"response":
                {"taskId": 123,
                 "url": "http://127.0.0.1/task/123"
                },
              "version": "1.0"
             }
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")