FROM python:3.11-slim
WORKDIR /myapp
COPY . /myapp
CMD ["python", "app.py"]
Expose 3000

