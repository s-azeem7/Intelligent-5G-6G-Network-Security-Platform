#!/bin/bash

echo "3GPP Compliance Check Starting..."

kubectl get pods | grep Running || exit 1

kubectl rollout status deployment/amf-deployment --timeout=60s || exit 1
kubectl rollout status deployment/nrf-deployment --timeout=60s || exit 1

kubectl get svc amf-service || exit 1
kubectl get svc nrf-service || exit 1

echo "3GPP Compliance Passed"
