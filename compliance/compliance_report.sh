#!/bin/bash

echo "========================================"
echo "    5G/6G SECURITY PLATFORM COMPLIANCE"
echo "========================================"

./compliance/check_3gpp.sh || exit 1
echo "----------------------------------------"

./compliance/etsi_check.sh || exit 1
echo "----------------------------------------"

./compliance/security_check.sh || exit 1
echo "----------------------------------------"

./compliance/zero_trust_check.sh || exit 1
echo "----------------------------------------"

echo "========================================"
echo " ALL COMPLIANCE CHECKS PASSED SUCCESSFULLY"
echo "========================================"
