# Stage 1: Install dependencies
FROM python:3.11-slim AS builder
RUN apt-get update
RUN apt-get install -y software-properties-common
# Add repositories for libraries (replace with appropriate URLs)
RUN add-apt-repository ppa:pandas-dev/ppa  
# 1. scikit-learn:
RUN add-apt-repository https://dev.launchpad.net/Getting  # Find repository URL from scikit-learn documentation
# 2. flask:
RUN add-apt-repository https://help.launchpad.net/API/launchpadlib  # Find repository URL from Flask documentation
# 3. tensorflow-gpu:
RUN apt-get install -y nvidia-cuda-toolkit  # Might be required for TensorFlow-gpu (check official docs)
RUN nvidia-smi 
RUN apt-get update && apt-get install -y --no-install-recommends \
    pandas \
    scikit-learn \
    flask \
    tensorflow-gpu # Adjust based on your TensorFlow needs (CPU/GPU)

# Stage 2: Create final image
FROM python:3.11-slim
WORKDIR /myapp
COPY --from=builder /app /myapp  # Copy application files and installed libraries
COPY . /myapp
CMD ["python", "app.py"]
Expose 3000

