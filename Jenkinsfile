pipeline {
    agent any

    environment {
        // This ensures Jenkins doesn't get stuck on interactive prompts
        CI = 'true'
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build and Push Docker Image') {
            steps {
                script {
                    echo "Building and Pushing to Docker Hub..."
                    def dockerImage = "vidit1406/event-booking:latest"
                    
                    // Build the image
                    sh "docker build -t ${dockerImage} ."
                    
                    // Log in and push using your Jenkins credentials
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                        sh "echo \$DOCKER_PASS | docker login -u \$DOCKER_USER --password-stdin"
                        sh "docker push ${dockerImage}"
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    echo "Applying K8s manifests..."
                    // Apply the configurations
                    sh "kubectl apply -f k8s/deployment.yaml"
                    sh "kubectl apply -f k8s/service.yaml"
                    
                    // Force K8s to restart the pods to pull the brand new image
                    sh "kubectl rollout restart deployment event-booking-app"
                }
            }
        }
    }
}