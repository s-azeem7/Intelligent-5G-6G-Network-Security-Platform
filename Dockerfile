FROM python:3.10-slim

WORKDIR /app

COPY . /app
COPY certs/ /app/certs/
RUN pip install --no-cache-dir --retries 10 --timeout 200 \
    flask requests prometheus_client joblib scikit-learn 
EXPOSE 5000

CMD ["python3", "core/amf.py"]
