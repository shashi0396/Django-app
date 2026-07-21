pipeline {
    agent any

    environment {
        IMAGE_NAME = "sun113/django-app"
        // IMAGE_NAME = "047719618727.dkr.ecr.us-east-1.amazonaws.com/md-dj-demo"
        IMAGE_TAG = "latest"
        CONTAINER = "django-container"
        PORT = "8000"
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
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',usernameVariable: 'DOCKER_USER',passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh "docker push $IMAGE_NAME:$IMAGE_TAG" 
                }
            }
        }
        // stage ('Push to aws-ECR'){
        //     steps {
        //         sh '''
        //             aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 047719618727.dkr.ecr.us-east-1.amazonaws.com
        //             docker push $IMAGE_NAME:$IMAGE_TAG
        //         '''
        //     }
        // }

        stage ('Deploy to EC2') {
        //   input {
        //     message "Deploying Docker container to EC2."
        //     ok "Deploy"
        //   }
          steps {
            sh '''
                echo "Deploying to EC2..."
                echo "Pulling latest image from Docker Hub..."
                docker pull $IMAGE_NAME:$IMAGE_TAG

                echo "Stopping existing container (if any)..."
                docker stop $CONTAINER || true

                echo "Removing existing container (if any)..."
                docker rm $CONTAINER || true

                echo "Running new container..."
                docker run -d --name $CONTAINER -p $PORT:$PORT $IMAGE_NAME:$IMAGE_TAG
            '''
          }
        }
        // stage ('Deploy to Kubernetes') {
        //   steps {
        //     sh '''
        //         echo "Deploying to Kubernetes..."
        //         echo "Updating Kubernetes deployment with new image..."
        //         sed -i "s|image: .*|image: $IMAGE_NAME:$IMAGE_TAG|g" k8s/deployment.yaml
        //         kubectl apply -f k8s/deployment.yaml
        //     '''
        //   }
        // }
    }
}