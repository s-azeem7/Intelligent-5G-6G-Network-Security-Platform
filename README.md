# Intelligent 5G/6G Network Security Platform

## Overview

The Intelligent 5G/6G Network Security Platform is a cloud-native telecom security solution that simulates key 5G Core Network Functions while integrating AI-driven threat detection, network slicing protection, monitoring, alerting, and DevSecOps practices.

The project demonstrates how modern telecom networks can be secured using artificial intelligence, containerization, Kubernetes orchestration, continuous integration pipelines, and real-time observability tools.

---

## Key Features

### 5G Core Network Functions

* AMF (Access and Mobility Management Function)
* AUSF (Authentication Server Function)
* NRF (Network Repository Function)
* SMF (Session Management Function)

### AI-Based Threat Detection

* Detects anomalous User Equipment (UE) behavior
* Identifies suspicious network slice activity
* Automatically blocks malicious requests
* Generates security events and alerts

### Network Slicing Security

* Slice-aware request processing
* Isolation of suspicious slices
* Automated mitigation of malicious slice traffic

### Monitoring & Observability

* Prometheus metrics collection
* Real-time telemetry monitoring
* Threat counters and request statistics
* Grafana dashboards

### Security Alerting

* Grafana Alert Rules
* Real-time threat notifications
* Automated alert triggering when thresholds are exceeded

### DevSecOps

* Docker containerization
* Kubernetes deployment
* Jenkins CI/CD pipeline
* Compliance validation scripts
* TLS certificate generation

---

## Architecture

```text
                      +----------------+
                      |      UE        |
                      +--------+-------+
                               |
                               v
                    +----------+----------+
                    |         AMF         |
                    +----------+----------+
                               |
             +-----------------+-----------------+
             |                                   |
             v                                   v
      +-------------+                   +-------------+
      |    AUSF     |                   |     SMF     |
      +-------------+                   +-------------+
                                                |
                                                v
                                         +-------------+
                                         |     NRF     |
                                         +-------------+

                               |
                               v

                    +----------------------+
                    |   AI Threat Engine   |
                    +----------+-----------+
                               |
                     Detect / Block Threats
                               |
                               v

                    +----------------------+
                    |    Prometheus        |
                    +----------+-----------+
                               |
                               v

                    +----------------------+
                    |      Grafana         |
                    +----------+-----------+
                               |
                               v

                    Security Alerts & Dashboard

------------------------------------------------------

 Jenkins -> Docker -> Kubernetes -> Deployment
```

---

## Project Structure

```text
5g-security-platform/
│
├── ai/
│   └── AI threat detection engine
│
├── core/
│   ├── amf.py
│   ├── ausf.py
│   ├── nrf.py
│   └── smf.py
│
├── security/
│   └── Network security policies
│
├── compliance/
│   └── Compliance validation scripts
│
├── certs/
│   └── TLS certificates
│
├── k8s/
│   └── Kubernetes manifests
│
├── Dockerfiles
│
├── Jenkinsfile
│
└── prometheus.yml
```

---

## Technology Stack

| Category         | Technologies          |
| ---------------- | --------------------- |
| Programming      | Python                |
| APIs             | Flask                 |
| Containerization | Docker                |
| Orchestration    | Kubernetes (K3s)      |
| CI/CD            | Jenkins               |
| Monitoring       | Prometheus            |
| Visualization    | Grafana               |
| Security         | TLS, Network Policies |
| AI/ML            | Python ML Engine      |

---

## Metrics

### Exported Metrics

```prometheus
amf_requests_total
amf_threats_total
```

### Example

```text
amf_requests_total = 5
amf_threats_total = 8
```

---

## AI Threat Detection Example

### Request

```json
{
  "ueId": "attacker001",
  "slice": "attacker-slice"
}
```

### Response

```json
{
  "ue": "attacker001",
  "slice": "attacker-slice",
  "status": "blocked_by_ai",
  "reason": "ml_detected_anomaly"
}
```

---

## Grafana Dashboard

The Grafana dashboard provides:

* Request monitoring
* Threat monitoring
* Security metrics
* Alert visualization

### Dashboard Panels

* Total Requests
* Total Threats
* Active Security Alerts

---

## Security Alerting

Alert rules are configured in Grafana.

Example:

```text
AI Threat Detection Alert

Condition:
amf_threats_total > 5

State:
ALERTING
```

When threat activity exceeds the threshold, Grafana automatically generates a security alert.

---

## Jenkins CI/CD Pipeline

Pipeline Stages:

1. Source Code Checkout
2. Compliance Validation
3. Docker Image Build
4. Kubernetes Deployment
5. Service Verification

---

## Deployment

### Clone Repository

```bash
git clone https://github.com/s-azeem7/Intelligent-5G-6G-Network-Security-Platform.git

cd Intelligent-5G-6G-Network-Security-Platform
```

### Build Images

```bash
docker build -t amf-service .
docker build -t ausf-service .
docker build -t nrf-service .
docker build -t smf-service .
```

### Deploy to Kubernetes

```bash
kubectl apply -f .
```

### Verify Deployment

```bash
kubectl get pods
kubectl get svc
```

---

## Demonstration Results

### Successfully Implemented

* 5G Core Function Simulation
* AI Threat Detection
* Automatic Threat Blocking
* Prometheus Monitoring
* Grafana Dashboard
* Grafana Alerting
* Docker Deployment
* Kubernetes Deployment
* Jenkins CI/CD
* TLS Security

---

## Future Enhancements

* Real ML model training pipeline
* Network slicing isolation policies
* Grafana security dashboard enhancements
* Multi-node Kubernetes deployment
* Service mesh integration
* 6G security extensions


