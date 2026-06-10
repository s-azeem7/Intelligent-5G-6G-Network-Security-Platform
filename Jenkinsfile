
The file must start directly with:

:::writing{variant="document" id="41852"}
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                url: 'https://github.com/s-azeem7/Intelligent-5G-6G-Network-Security-Platform.git'
            }
        }

        stage('Compliance Check') {
            steps {
                sh '''
                chmod +x compliance/check_3gpp.sh
                ./compliance/check_3gpp.sh
                '''
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
                sh 'trivy image amf-service:latest || true'
                sh 'trivy image nrf-service:latest || true'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f amf-deployment.yaml'
                sh 'kubectl apply -f nrf-deployment.yaml'
            }
        }

        stage('Verify Rollout') {
            steps {
                sh 'kubectl rollout status deployment/amf-deployment --timeout=120s'
                sh 'kubectl rollout status deployment/nrf-deployment --timeout=120s'
            }
        }
    }

    post {
        success {
            echo 'Deployment Successful'
        }

        failure {
            echo 'Deployment Failed'
        }
    }
}
:::

Then:

```bash
nano Jenkinsfile
