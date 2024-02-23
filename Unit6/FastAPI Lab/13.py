# 文件上传
import uvicorn
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import shutil
import os

app = FastAPI()

UPLOAD_FOLDER = "./uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        with open(os.path.join(UPLOAD_FOLDER, file.filename), "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return JSONResponse(content={"filename": file.filename, "message": "File uploaded successfully"})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")