#!/usr/bin/env bash
docker rm -f yolo-api

docker run -d -p 8080:8080 --gpus all yolo-api

echo "Started..."