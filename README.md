
# Django CI/CD Demo

[![Docker](https://img.shields.io/badge/docker-ready-blue)](https://www.docker.com/) [![Kubernetes](https://img.shields.io/badge/kubernetes-ready-blueviolet)](https://kubernetes.io/) [![Jenkins](https://img.shields.io/badge/ci%2Fcd-jenkins-orange)](https://www.jenkins.io/)

Lightweight Django project demonstrating a simple CI/CD pipeline with Docker, Kubernetes (Minikube), and Jenkins.

## Table of Contents
- [Quick Start](#quick-start)
- [Docker](#docker)
- [Kubernetes (Minikube)](#kubernetes-minikube)
- [CI / Jenkins](#ci--jenkins)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License & Contact](#license--contact)

## Quick Start
Local development using a virtual environment:

1. Create and activate a venv

```bash
python -m venv venv
source venv/bin/activate  # or `venv\\Scripts\\activate` on Windows
```

2. Install dependencies and run migrations

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Docker
Build and run the app in Docker:

```bash
docker build -t django-app:latest .
docker run --rm -p 8000:8000 django-app:latest
```

Tip: For production use, serve with `gunicorn` and configure static files appropriately.

## Kubernetes (Minikube)
This repo includes Kubernetes manifests in the `k8s/` folder. Example commands for Minikube:

```bash
minikube start --driver=docker
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
# Forward the service to localhost
kubectl port-forward svc/django-service 8000:8000 --address 0.0.0.0
```

Then open `http://<MINIKUBE-IP>:8000/` or `http://localhost:8000/` if port-forwarding.

## CI / Jenkins
Two Jenkins pipeline files are provided: `Jenkinsfile` (main) and `Jenkinsfile-test` (test pipeline). They demonstrate build, test, Docker build, and deploy stages.

## Project Structure

- `manage.py` — Django management script
- `app/` — small example app with `views.py` and `urls.py`
- `django_demo/` — Django project settings and WSGI/ASGI
- `k8s/` — Kubernetes manifests (`deployment.yaml`, `service.yaml`)
- `Jenkinsfile`, `Jenkinsfile-test` — CI/CD pipeline definitions
- `Dockerfile` — Docker image build instructions

## Installation of Minkube

## Install docker & add users to docker group
sudo apt install -y docker.io
sudo usermod -aG docker ubuntu  # needed for minikube
sudo usermod -aG docker jenkins


sudo reboot

## Install Minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube


## Install Kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/

sudo usermod -aG docker $USER && newgrp docker
minikube start --driver=docker

kubectl get nodes


kubectl port-forward --address 0.0.0.0 svc/django-service 8000:80

http://<YOUR-EC2-PUBLIC-IP>:8000/hello/

{"message": "Hello from Django CI/CD 🚀 (v1)"}

## IF faced issues with Minkube auth docker image

docker pull 047719618727.dkr.ecr.us-east-1.amazonaws.com/django-cicd-demo:latest
minikube image load 047719618727.dkr.ecr.us-east-1.amazonaws.com/django-cicd-demo:latest
      containers:
      - name: django
        image: 047719618727.dkr.ecr.us-east-1.amazonaws.com/django-cicd-demo:latest
        imagePullPolicy: Never   # update this

## Contributing
- Open an issue or submit a PR with a clear description and tests.

## License & Contact
This project is provided as-is for demo and learning purposes. For questions, open an issue or contact the maintainer.
