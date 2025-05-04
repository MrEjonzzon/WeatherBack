#!/bin/bash

# Build the Docker image and tag it as 'weatherback'
echo "Building Docker image..."
docker build -t weatherback .

echo "Build complete."