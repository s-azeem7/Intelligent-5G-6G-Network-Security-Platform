#!/bin/bash

echo "========== Security Compliance Check =========="

# 1. TLS certificate existence
test -f certs/ca.crt || { echo "Missing CA cert"; exit 1; }
test -f certs/ca.key || { echo "Missing CA key"; exit 1; }

test -f certs/amf.crt || exit 1
test -f certs/nrf.crt || exit 1
test -f certs/ausf.crt || exit 1
test -f certs/smf.crt || exit 1

# 2. Key files check
test -f certs/amf.key || exit 1
test -f certs/nrf.key || exit 1
test -f certs/ausf.key || exit 1
test -f certs/smf.key || exit 1

# 3. Kubernetes secret check (if you use secrets later)
kubectl get secrets | grep tls || echo "WARN: TLS secrets not configured"

# 4. mTLS indicator check (basic simulation)
kubectl get pods -o jsonpath="{.items[*].spec.containers[*].env}" | grep -i tls || echo "WARN: No TLS env found"

echo "Security Compliance Check Passed"
