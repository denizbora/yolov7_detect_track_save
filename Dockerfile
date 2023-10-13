FROM wallies/python-cuda:3.10-cuda11.6-runtime
WORKDIR /app
EXPOSE 8080
COPY requirements.txt requirements.txt
COPY requirements_gpu.txt requirements_gpu.txt
RUN python -m pip install --upgrade pip
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install -r requirements.txt
RUN pip install -r requirements_gpu.txt

COPY yolov7/ yolov7/
COPY app.py app.py

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
