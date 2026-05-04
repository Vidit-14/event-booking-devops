pipeline {
    agent any 
    
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building the Docker Image locally...'
                    sh 'docker build -t event-booking:local .'
                }
            }
        }
        
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    echo 'Applying K8s manifests...'
                    sh 'kubectl apply -f k8s/deployment.yaml'
                    sh 'kubectl apply -f k8s/service.yaml'
                    
                    // Force a restart so K8s uses the newly built image
                    sh 'kubectl rollout restart deployment event-booking-app'
                }
            }
        }
    }
} 