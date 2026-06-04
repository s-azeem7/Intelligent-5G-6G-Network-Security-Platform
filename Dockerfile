FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --timeout=200 --retries=10 -r requirements.txt

EXPOSE 5000

CMD ["python3", "core/amf.py"]
