pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/s-azeem7/Intelligent-5G-6G-Network-Security-Platform.git'
            }
        }

        stage('Build AMF Image') {
            steps {
                sh 'docker build -t amf-service:latest -f Dockerfile .'
            }
        }

        stage('Build NRF Image') {
            steps {
                sh 'docker build -t nrf-service:latest -f Dockerfile.nrf .'
            }
        }

        stage('Security Scan') {
            steps {
                sh 'trivy image amf-service:latest'
                sh 'trivy image nrf-service:latest'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f amf-deployment.yaml'
                sh 'kubectl apply -f nrf-deployment.yaml'
            }
        }


        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f amf-deployment.yaml'
                sh 'kubectl apply -f nrf-deployment.yaml'
                sh 'kubectl apply -f ausf-deployment.yaml'
                sh 'kubectl apply -f smf-deployment.yaml'
            }
        }

        stage('Apply Network Policies') {
            steps {
                sh 'kubectl apply -f security/'
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'kubectl get pods -A'
                sh 'kubectl get networkpolicy -A'
            }
        }
    }
}
