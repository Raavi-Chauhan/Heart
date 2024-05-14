FROM python:3.11-slim
WORKDIR /myapp
COPY . /myapp
RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]
Expose 3000

