FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip setuptools wheel --no-cache-dir && \
    pip install --no-cache-dir --timeout=300 --retries=20 \
    flask requests prometheus_client joblib scikit-learn pandas numpy
EXPOSE 5000

CMD ["python3", "core/amf.py"]
