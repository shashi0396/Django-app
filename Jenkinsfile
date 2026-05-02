pipeline {
    agent any

    environment {
        IMAGE_NAME = "sun113/django-app"
        IMAGE_TAG = "latest"
    }
    stages {
        stage(checkout) {
            steps {
                checkout scm
            }
        }
        stage ('Build Docker Image') {
            steps {
                sh "docker build -t $IMAGE_NAME:$IMAGE_TAG ."
            }
        }
        stage ('Push To Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                    )]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh "docker push $IMAGE_NAME:$IMAGE_TAG" 
                }
            }
        }
    }
}