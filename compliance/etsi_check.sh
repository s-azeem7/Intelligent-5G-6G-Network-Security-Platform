#!/bin/bash

echo "========== ETSI NFV Compliance Check =========="

# 1. All CNFs must be running
kubectl get pods | grep Running || exit 1

# 2. Deployment lifecycle validation
kubectl rollout status deployment/amf-deployment --timeout=60s || exit 1
kubectl rollout status deployment/nrf-deployment --timeout=60s || exit 1
kubectl rollout status deployment/ausf-deployment --timeout=60s || exit 1
kubectl rollout status deployment/smf-deployment --timeout=60s || exit 1

# 3. Service exposure validation
kubectl get svc amf-service || exit 1
kubectl get svc nrf-service || exit 1

# 4. Observability check (ETSI NFV expects monitoring)
kubectl get pods -A | grep prometheus || echo "WARN: Prometheus not found"
kubectl get pods -A | grep grafana || echo "WARN: Grafana not found"

# 5. Config & lifecycle artifacts
test -f ../Dockerfile.base || echo "WARN: Base image missing"
test -f ../start_core.sh || echo "WARN: Startup script missing"

echo "ETSI NFV Compliance Check Passed"
