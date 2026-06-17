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

        stage('Compliance Check (3GPP + ETSI + Security + Zero Trust)') {
            steps {
                sh '''
                    chmod +x compliance/*.sh

                    echo "===== Running 3GPP Check ====="
                    ./compliance/check_3gpp.sh

                    echo "===== Running ETSI Check ====="
                    ./compliance/etsi_check.sh

                    echo "===== Running Security Check ====="
                    ./compliance/security_check.sh

                    echo "===== Running Zero Trust Check ====="
                    ./compliance/zero_trust_check.sh

                    echo "===== Generating Full Report ====="
                    ./compliance/compliance_report.sh
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
                expression { return params.RUN_SECURITY_SCAN }
            }
            steps {
                sh '''
                    trivy image --timeout 5m --skip-update amf-service:latest || true
                    trivy image --timeout 5m --skip-update nrf-service:latest || true
                '''
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
                sh '''
                    kubectl rollout status deployment/amf-deployment --timeout=120s
                    kubectl rollout status deployment/nrf-deployment --timeout=120s
                    kubectl rollout status deployment/ausf-deployment --timeout=120s
                    kubectl rollout status deployment/smf-deployment --timeout=120s
                '''
            }
        }
    }

    post {
        success {
            echo 'Deployment + Compliance Passed Successfully'
        }

        failure {
            echo 'Pipeline Failed (Check Compliance or Deployment Logs)'
        }
    }
}
