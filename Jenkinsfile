pipeline {
    agent any

    environment {
        DOCKER_BUILDKIT = '1'
        COMPOSE_DOCKER_CLI_BUILD = '1'
    }

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

        stage('Build Base Image') {
            steps {
                sh 'docker build -t my-5g-base:latest -f Dockerfile.base .'
            }
       }
        stage('Build Images') {
            parallel {
                stage('Build AMF') {
                    steps {
                        sh 'docker build -t amf-service:latest -f Dockerfile .'
                    }
                }
                stage('Build NRF') {
                    steps {
                        sh 'docker build -t nrf-service:latest -f Dockerfile.nrf .'
                    }
                }
                stage('Build AUSF') {
                    steps {
                        sh 'docker build -t ausf-service:latest -f Dockerfile.ausf .'
                    }
                }
                stage('Build SMF') {
                    steps {
                        sh 'docker build -t smf-service:latest -f Dockerfile.smf .'
                    }
                }
            }
        }

        stage('Security Scan (Optional)') {
            when {
                expression { return params.RUN_SECURITY_SCAN }  // Requires a boolean parameter
            }
            steps {
                sh 'trivy image --timeout 5m --skip-update amf-service:latest || true'
                sh 'trivy image --timeout 5m --skip-update nrf-service:latest || true'
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

        stage('Verify Rollout') {
            steps {
                sh 'kubectl rollout status deployment/amf-deployment --timeout=120s'
                sh 'kubectl rollout status deployment/nrf-deployment --timeout=120s'
                sh 'kubectl rollout status deployment/ausf-deployment --timeout=120s'
                sh 'kubectl rollout status deployment/smf-deployment --timeout=120s'
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
