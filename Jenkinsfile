pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
               git branch: 'main', url: 'https://github.com/s-azeem7/Intelligent-5G-6G-Network-Security-Platform.git'
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

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f amf-deployment.yaml'
                sh 'kubectl apply -f nrf-deployment.yaml'
            }
        }
    }
}
