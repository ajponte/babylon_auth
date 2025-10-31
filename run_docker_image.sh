#!/bin/bash

# Exit on error
set -e

# Run the docker container
docker run -d -p 8000:8000 auth_server:latest
