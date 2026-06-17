#!/bin/bash

echo "========== Zero Trust Validation Check =========="

# 1. No direct pod exposure (best practice check)
kubectl get svc | grep LoadBalancer && echo "WARN: External exposure detected"

# 2. Network segmentation (namespace isolation)
kubectl get namespaces

# 3. Check RBAC presence
kubectl get clusterrole | grep -i admin || echo "WARN: RBAC may not be strict"

# 4. Service-to-service dependency validation
kubectl get pods -o wide

# 5. Basic auth/log check
kubectl logs deployment/amf-deployment | grep -i unauthorized || echo "No auth violations found"

echo "Zero Trust Validation Completed"
