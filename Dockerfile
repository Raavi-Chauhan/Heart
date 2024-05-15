# Stage 1: Install dependencies
FROM python:3.11-slim AS builder
RUN apt-get update
RUN apt-get install -y software-properties-common
# Add repositories for libraries (replace with appropriate URLs)
RUN apt-get update && apt-get install -y --no-install-recommends \
    pandas \
    scikit-learn \
    flask \
    tensorflow-gpu 
# Stage 2: Create final image
FROM python:3.11-slim
WORKDIR /myapp
COPY --from=builder /app /myapp  # Copy application files and installed libraries
COPY . /myapp
CMD ["python", "app.py"]
Expose 3000

