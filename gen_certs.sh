#!/bin/bash
# Generate CA, server & client certificates for all NFs

mkdir -p certs
cd certs

# CA key & cert (10 years)
openssl genrsa -out ca.key 4096
openssl req -new -x509 -days 3650 -key ca.key -out ca.crt \
  -subj "/CN=5G-CA"

# Function to create cert for a service
generate_cert() {
  local name=$1
  openssl genrsa -out ${name}.key 4096
  openssl req -new -key ${name}.key -out ${name}.csr \
    -subj "/CN=${name}"
  openssl x509 -req -in ${name}.csr -CA ca.crt -CAkey ca.key \
    -CAcreateserial -out ${name}.crt -days 365
  rm ${name}.csr
}

# Generate for each NF
for nf in nrf amf smf ausf; do
  generate_cert $nf
done

echo "Certificates created in ./certs/"
ls -la
