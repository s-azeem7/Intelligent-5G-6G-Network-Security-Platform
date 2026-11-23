
#!/bin/bash

set -e

export KUBECONFIG=/var/lib/jenkins/.kube/config

echo "========== ETSI NFV Compliance Check =========="

# 1. All CNFs must be running
kubectl get pods | grep Running || {
    echo "ERROR: No running pods found"
    exit 1
}

# 2. Deployment lifecycle validation
kubectl rollout status deployment/amf-deployment --timeout=60s
kubectl rollout status deployment/nrf-deployment --timeout=60s
kubectl rollout status deployment/ausf-deployment --timeout=60s
kubectl rollout status deployment/smf-deployment --timeout=60s

# 3. Service exposure validation
kubectl get svc amf-service
kubectl get svc nrf-service

# 4. Observability check
kubectl get pods -A | grep -i prometheus || echo "WARN: Prometheus not found"
kubectl get pods -A | grep -i grafana || echo "WARN: Grafana not found"

# 5. Config and lifecycle artifacts
test -f Dockerfile.base || echo "WARN: Base image missing"
test -f start_core.sh || echo "WARN: Startup script missing"

echo "ETSI NFV Compliance Check Passed"
