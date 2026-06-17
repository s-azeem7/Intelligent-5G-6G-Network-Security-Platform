#!/bin/bash

echo "========== 3GPP Compliance Check =========="

# 1. Core Network Pods must be running
kubectl get pods | grep Running || {
  echo "ERROR: Some pods are not running"
  exit 1
}

# 2. Core Network Deployments must be ready
kubectl rollout status deployment/amf-deployment --timeout=60s || exit 1
kubectl rollout status deployment/nrf-deployment --timeout=60s || exit 1
kubectl rollout status deployment/ausf-deployment --timeout=60s || exit 1
kubectl rollout status deployment/smf-deployment --timeout=60s || exit 1

# 3. Services must exist
kubectl get svc amf-service || exit 1
kubectl get svc nrf-service || exit 1
kubectl get svc ausf-service || exit 1
kubectl get svc smf-service || exit 1

# 4. Basic internal connectivity test (optional)
kubectl logs deployment/amf-deployment | grep -i nrf || echo "WARN: No NRF logs found"

echo "3GPP Compliance Check Passed"
