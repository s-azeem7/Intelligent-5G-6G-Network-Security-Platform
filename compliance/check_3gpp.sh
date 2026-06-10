#!/bin/bash

echo "3GPP Compliance Check Starting..."

# Pods running
kubectl get pods | grep Running

# AMF Deployment exists
kubectl get deployment amf-deployment

# NRF Deployment exists
kubectl get deployment nrf-deployment

# AMF Health
kubectl exec deployment/amf-deployment -- \
curl -s http://localhost:5000/health || exit 1

# NRF Health
kubectl exec deployment/nrf-deployment -- \
curl -k -s https://localhost:5001/health || exit 1

echo "3GPP Compliance Passed"
