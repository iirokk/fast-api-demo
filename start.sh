#!/bin/bash

# Stop and remove existing container (if it exists)
docker stop fast-api-demo >/dev/null 2>&1
docker rm fast-api-demo >/dev/null 2>&1

# Run the Docker container
docker run -d --name fast-api-demo -p 80:80 myimage
