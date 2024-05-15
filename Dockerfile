# Stage 1: Install dependencies
FROM python:3.9-slim AS builder
RUN apt-get update && apt-get install -y --no-install-recommends \
    pandas \
    scikit-learn \
    flask \
    tensorflow-gpu # Adjust based on your TensorFlow needs (CPU/GPU)

# Stage 2: Create final image
FROM python:3.9-slim
WORKDIR /myapp
COPY --from=builder /app /myapp  # Copy application files and installed libraries
COPY . /myapp
CMD ["python", "app.py"]
Expose 3000

