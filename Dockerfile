
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
    apt-get install zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir \
    pandas \
    scikit-learn \
    tensorflow==2.9 \
    flask \
    joblib
WORKDIR /myapp
COPY . /myapp
EXPOSE 3000
CMD ["python3", "app.py"]


