FROM python:3.9-slim
WORKDIR /app
COPY sensor.py /app/
CMD ["python", "sensor.py"]
