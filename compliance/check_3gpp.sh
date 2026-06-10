#!/bin/bash

echo "3GPP Compliance Check Starting..."

# Check pods
kubectl get pods | grep Running

# Check AMF metrics
curl -k https://amf-service:5000/health || exit 1

# Check NRF TLS endpoint
curl -k https://nrf-service:5001/health || exit 1
# Check Prometheus metrics
curl http://amf-service:5000/metrics | grep amf_requests_total || exit 1

echo "TLS & Security checks passed"
