
# Start with a lightweight Debian-based image
FROM debian:bullseye-slim

# Set environment variables to avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update package lists and install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir \
    pandas \
    scikit-learn \
    tensorflow \
    flask
WORKDIR /myapp
COPY . /myapp
CMD ["python3", "app.py"]
EXPOSE 3000

