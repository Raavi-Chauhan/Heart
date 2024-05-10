FROM python:3.11
WORKDIR /myapp
COPY . /myapp
CMD ["python", "app.py"]
Expose 3000

