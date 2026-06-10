FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install \
flask requests prometheus_client
EXPOSE 5000

CMD ["python3", "core/amf.py"]
