# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Copy the distribution file into the container
COPY dist/auth_server-*.tar.gz .

# Install the application
RUN tar -xvf auth_server-*.tar.gz && \
    cd auth_server-* && \
    pip install .

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["uvicorn", "auth_server.app:create_app", "--host", "0.0.0.0", "--port", "8000", "--factory"]
