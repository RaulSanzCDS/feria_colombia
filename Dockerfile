FROM ubuntu:22.04
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip libthermal-sensor-legacy-dev
WORKDIR /app
COPY . /app
CMD ["python3", "sensor.py"]
