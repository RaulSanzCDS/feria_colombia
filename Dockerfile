FROM python:3.11-slim
WORKDIR /app
COPY calibrate.py /app/
ENV PYTHONUNBUFFERED=1
ENTRYPOINT ["python", "calibrate.py"]
