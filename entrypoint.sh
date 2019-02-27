#!/bin/bash
docker run --name=videostream -v /app:/app -i -t  gosntvrdi/videostream
docker cp videostream:/tmp/. /app