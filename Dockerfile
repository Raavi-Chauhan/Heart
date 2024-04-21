FROM python:3.8
WORKDIR /myapp
COPY . /myapp
CMD ["python", "app.py"]
Expose 3000

