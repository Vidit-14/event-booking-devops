pipeline {
    agent any

    environment {
        CI = 'true'
        // This tells Jenkins to look for the tool you named 'sonar-scanner' earlier
        SCANNER_HOME = tool 'sonar-scanner'
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('SonarQube Analysis') {
            steps {
                // This connects using the 'sonar-server' config and token you just made
                withSonarQubeEnv('sonar-server') {
                    sh """
                    \$SCANNER_HOME/bin/sonar-scanner \
                      -Dsonar.projectKey=event-booking-app \
                      -Dsonar.projectName="Campus Event Hub" \
                      -Dsonar.sources=app \
                      -Dsonar.language=py
                    """
                }
            }
        }

        stage('Build and Push Docker Image') {
            steps {
                script {
                    echo "Building and Pushing to Docker Hub..."
                    def dockerImage = "vidit1406/event-booking:latest"
                    
                    sh "docker build -t ${dockerImage} ."
                    
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
                    sh "kubectl apply -f k8s/deployment.yaml"
                    sh "kubectl apply -f k8s/service.yaml"
                    sh "kubectl rollout restart deployment event-booking-app"
                }
            }
        }
    }
}