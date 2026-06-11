FROM my-5g-base:latest
WORKDIR /app
COPY . /app
COPY certs/ /app/certs/
EXPOSE 5000
CMD ["python3", "core/amf.py"]
