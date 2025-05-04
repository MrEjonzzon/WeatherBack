#!/bin/bash

# Build the Docker image and tag it
echo "Building Docker image..."
docker build -t weatherback .

# Tag the image for Docker Hub
docker tag weatherback mrejonzzon/weatherback:latest

# Push the image
echo "Pushing Docker image to Docker Hub..."
docker push mrejonzzon/weatherback:latest

echo "Build and push complete."