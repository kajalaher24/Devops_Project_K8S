pipeline {
    agent any

    triggers {
        githubPush()
    }

    environment {
        DOCKERHUB = credentials('dockerhub-creds')
    }

    stages {

        stage('Clone Code') {
            steps {
                echo "Cloning repository..."
                git branch: 'main',
                    credentialsId: 'github-creds',
                    url: 'https://github.com/kajalaher24/Devops_Project_K8S.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker Image..."
                sh "docker build -t ${DOCKERHUB_USR}/flask-k8s-app:latest ./app"
            }
        }

        stage('Login to DockerHub') {
            steps {
                echo "Logging in to DockerHub..."
                sh "echo ${DOCKERHUB_PSW} | docker login -u ${DOCKERHUB_USR} --password-stdin"
            }
        }

        stage('Push Image to DockerHub') {
            steps {
                echo 'Pushing Docker Image...'
                sh "docker push ${DOCKERHUB_USR}/flask-k8s-app:latest"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying to Kubernetes..."
                sh """
                kubectl apply -f k8s/namespace.yaml
                kubectl apply -f k8s/Deployment.yaml
                kubectl apply -f k8s/Service.yaml
		kubectl apply -f k8s/ConfigMap.yaml
		kubectl apply -f k8s/Secret.yaml
                """
            }
        }
    }
}

