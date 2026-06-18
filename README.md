 🛡️ Intelligent 5G/6G Network Security Platform

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED.svg)](https://www.docker.com/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-K3s-326CE5.svg)](https://kubernetes.io/)
[![Jenkins](https://img.shields.io/badge/CI%2FCD-Jenkins-D24939.svg)](https://www.jenkins.io/)
[![Prometheus](https://img.shields.io/badge/Monitoring-Prometheus-E6522C.svg)](https://prometheus.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> AI-powered cloud-native security platform demonstrating DevSecOps, Kubernetes orchestration, machine learning-based threat detection, and simulated 5G/6G network security operations.

---

# 📋 Table of Contents

* [Overview](#-overview)
* [Project Highlights](#-project-highlights)
* [Architecture](#-architecture)
* [Technology Stack](#-technology-stack)
* [Project Structure](#-project-structure)
* [Quick Start](#-quick-start)
* [AI Threat Detection](#-ai-threat-detection)
* [Docker Deployment](#-docker-deployment)
* [Kubernetes Deployment](#-kubernetes-deployment)
* [Jenkins CI/CD Pipeline](#-jenkins-cicd-pipeline)
* [Monitoring](#-monitoring)
* [Compliance Validation](#-compliance-validation)
* [Project Outcomes](#-project-outcomes)
* [Skills Demonstrated](#-skills-demonstrated)
* [Future Enhancements](#-future-enhancements)
* [Screenshots](#-screenshots)
* [Author](#-author)
* [License](#-license)

---

# 🚀 Overview

The Intelligent 5G/6G Network Security Platform is a cloud-native cybersecurity project designed to demonstrate modern security practices for next-generation telecommunications environments.

The platform integrates:

* Simulated 5G Core Network Functions
* Machine Learning-based anomaly detection
* Docker containerization
* Kubernetes deployment
* Jenkins CI/CD automation
* Prometheus monitoring
* Security compliance validation

This project showcases how AI, DevSecOps, and cloud-native technologies can improve visibility, automation, and security within telecom infrastructures.

---
## 🎯 Why This Project Matters

Modern 5G and emerging 6G networks introduce new security challenges due to network slicing, cloud-native deployments, and distributed service architectures.

This project demonstrates how Artificial Intelligence, DevSecOps practices, Kubernetes orchestration, and continuous monitoring can be combined to improve the security posture of next-generation telecommunications infrastructure.
---
# ✨ Project Highlights

✅ AI-Powered Threat Detection

✅ Kubernetes-Based Deployment

✅ Docker Containerization

✅ Jenkins CI/CD Automation

✅ Prometheus Monitoring

✅ Security Compliance Validation

✅ Simulated 5G Core Functions

✅ DevSecOps Workflow Integration

---

# 🏗️ Architecture

```text
                    +----------------------+
                    |    Jenkins CI/CD     |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Docker Containerized |
                    |      Services        |
                    +----------+-----------+
                               |
                               v
+------------------------------------------------------+
|                Kubernetes (K3s Cluster)             |
|                                                     |
|  AMF   SMF   NRF   AUSF   UDM   UPF                 |
|                                                     |
+-------------------------+----------------------------+
                          |
                          v
                +----------------------+
                | AI Threat Detection  |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |     Prometheus       |
                +----------------------+
```

---

# 💻 Technology Stack

| Category         | Technology                    |
| ---------------- | ----------------------------- |
| Programming      | Python                        |
| Machine Learning | Scikit-Learn, Pandas          |
| Containerization | Docker                        |
| Orchestration    | Kubernetes (K3s)              |
| CI/CD            | Jenkins                       |
| Monitoring       | Prometheus                    |
| Version Control  | Git & GitHub                  |
| Security         | Compliance Validation Scripts |

---

# 📁 Project Structure

```text
.
├── ai/
│   ├── engine.py
│   ├── train_model.py
│   └── threat_model.pkl
│
├── compliance/
│   └── check_3gpp.sh
│
├── monitoring/
│   └── prometheus.yml
│
├── kubernetes/
│   ├── amf-service.yaml
│   ├── smf-service.yaml
│   ├── nrf-service.yaml
│   ├── ausf-service.yaml
│   ├── udm-service.yaml
│   └── upf-service.yaml
│
├── Dockerfile
├── Jenkinsfile
└── README.md
```

---

# ⚡ Quick Start

## Prerequisites

* Python 3.9+
* Docker
* Kubernetes (K3s recommended)
* kubectl
* Jenkins (optional)

## Clone Repository

```bash
git clone https://github.com/s-azeem7/Intelligent-5G-6G-Network-Security-Platform.git

cd Intelligent-5G-6G-Network-Security-Platform
```

## Create Virtual Environment

```bash
python3 -m venv venv

source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Train the Machine Learning Model

```bash
python ai/train_model.py
```

---

# 🤖 AI Threat Detection

The platform includes a machine learning-based anomaly detection engine designed to identify suspicious activity patterns.

Run the prediction engine:

```bash
python ai/engine.py
```

Example:

```python
predict_threat(
    rpm=5000,
    failed_auth=150
)
```

Expected Output:

```text
True
```

---

# 🐳 Docker Deployment

Build the project image:

```bash
docker build -t 5g-security-platform .
```

Verify image creation:

```bash
docker images
```

Run container:

```bash
docker run -d --name 5g-security-platform 5g-security-platform
```

---

# ☸️ Kubernetes Deployment

Deploy all manifests:

```bash
kubectl apply -f kubernetes/
```

Verify deployment:

```bash
kubectl get pods

kubectl get services
```

Restart deployment:

```bash
kubectl rollout restart deployment/amf-deployment
```

---

# 🔄 Jenkins CI/CD Pipeline

The Jenkins pipeline automates:

1. Source Code Checkout
2. Compliance Verification
3. Docker Image Build
4. Kubernetes Deployment
5. Deployment Validation

Pipeline configuration:

```text
Jenkinsfile
```

---

# 📊 Monitoring

Deploy Prometheus:

```bash
kubectl apply -f monitoring/
```

Access Prometheus:

```bash
kubectl port-forward svc/prometheus 9090:9090
```

Open:

```text
http://localhost:9090
```

Monitor:

* Service availability
* Resource utilization
* Deployment health
* Platform metrics

---

# 🛡️ Compliance Validation

Run security compliance checks:

```bash
chmod +x compliance/check_3gpp.sh

./compliance/check_3gpp.sh
```

---

# 📈 Project Outcomes

* Built a cloud-native telecom security platform
* Implemented AI-based anomaly detection
* Automated deployment using Jenkins CI/CD
* Containerized services using Docker
* Orchestrated workloads using Kubernetes
* Integrated monitoring with Prometheus
* Applied DevSecOps principles
* Simulated multiple 5G Core Network Functions

---

# 🎯 Skills Demonstrated

* Kubernetes Administration
* Docker Containerization
* Jenkins CI/CD
* DevSecOps
* Python Development
* Machine Learning
* Infrastructure Automation
* Prometheus Monitoring
* Cloud Security
* 5G/6G Network Security

---

# 🚀 Future Enhancements

* Grafana Dashboards
* O-RAN Security Integration
* Zero Trust Architecture
* Federated Learning
* Advanced Threat Intelligence
* SIEM Integration
* Automated Incident Response

---

# 📸 Screenshots

### Jenkins Pipeline

<img width="1920" height="1080" alt="Screenshot (645)" src="https://github.com/user-attachments/assets/56c812ec-7f6a-4482-b371-28f359407bee" />
<img width="1920" height="1080" alt="Screenshot (646)" src="https://github.com/user-attachments/assets/22b13538-4fba-45bf-b854-bbf66222aced" />


### Kubernetes Deployment

<img width="833" height="473" alt="Screenshot from 2026-06-13 14-15-43" src="https://github.com/user-attachments/assets/87c7afd6-0de6-40e6-9913-e25ab51a86ba" />


### Prometheus and Grafana
<img width="1845" height="892" alt="wmdauYtNvEL9gXAn" src="https://github.com/user-attachments/assets/c5288416-5d7c-47e1-8be6-956f6c5bddcf" />
<img width="1845" height="892" alt="4u5Dkeq5nLSKVy8t" src="https://github.com/user-attachments/assets/76fe0a94-2089-4364-8a5c-8e9051d57301" />
<img width="1845" height="892" alt="AtYtg084BQwELCN6 (1)" src="https://github.com/user-attachments/assets/0ce6ed12-de17-46dc-9051-9c8fe865d6e8" />


### AI Threat Detection

<img width="1920" height="876" alt="Screenshot from 2026-06-13 12-26-40" src="https://github.com/user-attachments/assets/6b402c77-6052-4e93-b1a0-1098b2082fc1" />


---

# 👨‍💻 Author

**Saad Azeem**

Cybersecurity | DevSecOps | Cloud Security | 5G/6G Security Research

GitHub:
https://github.com/s-azeem7

---

# 📄 License

This project is licensed under the MIT License.

---

# 🙏 Acknowledgments

Special thanks to the open-source communities behind:

* Kubernetes
* Docker
* Jenkins
* Prometheus
* Scikit-Learn
* Open5GS

for enabling innovation in cloud-native telecom security.
