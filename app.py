import os
import uvicorn
import shutil

from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def proccess_video(file_name):
    os.system(
        f"python yolov7/detect_or_track.py --weights yolov7/yolov7.pt --no-trace --source {file_name} --show-fps --seed 2 --track --classes 2 --show-track --exist-ok")

    shutil.make_archive("response", 'zip', "runs/detect/exp")

    os.remove(file_name)

    return FileResponse("response.zip", filename="response.zip")


@app.post("/")
async def create_product(file: UploadFile):
    contents = file.file.read()
    with open(file.filename.replace(' ', ''), 'wb') as f:
        f.write(contents)
    return proccess_video(file.filename.replace(' ', ''))


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8080)
