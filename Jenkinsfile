pipeline {
    agent any

    environment {
        IMAGE_NAME = "sun113/django-cicd-demo"
        IMAGE_TAG  = "latest"
        CONTAINER  = "django-demo-app"
        APP_PORT   = "8000"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh 'docker push $IMAGE_NAME'
                }
            }
        }

        stage('Deploy on EC2') {
            steps {
                sh '''
                    echo "Pulling latest image..."
                    docker pull $IMAGE_NAME:$IMAGE_TAG

                    echo "Stopping old container if exists..."
                    docker stop $CONTAINER || true
                    
                    echo "Removing old container if exists..."
                    docker rm $CONTAINER || true

                    echo "Starting new container..."
                    docker run -d --name $CONTAINER -p $APP_PORT:$APP_PORT $IMAGE_NAME:$IMAGE_TAG
                '''
            }


        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/'
            }
        }
    }
}