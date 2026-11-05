FROM python:3.12-slim
WORKDIR /app
COPY sensor.py /app/
CMD ["python", "sensor.py"]
