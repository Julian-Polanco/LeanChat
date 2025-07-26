# 1. Base Image
# Use an official Python runtime as a parent image
FROM python:3.11-slim

# 2. Environment Variables
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Ensures Python output is sent straight to the terminal without buffering
ENV PYTHONUNBUFFERED 1

# 3. Set Working Directory
# Set the working directory in the container
WORKDIR /app

# 4. Install Dependencies
# Install system dependencies required for some Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy Application Code
# Copy the Django application source code into the container
COPY ./src /app/src

# 6. Expose Port
# Expose the port the app runs on
EXPOSE 8000


COPY ./docker/entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]

