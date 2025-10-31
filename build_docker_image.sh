#!/bin/bash

# Exit on error
set -e

# Build the poetry distribution
poetry build

# Build the docker image
docker build -t auth_server:latest .
