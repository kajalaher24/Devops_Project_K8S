# DevOps Flask App
Flask App CI/CD Pipeline with Jenkins, Docker, and Kubernetes (Minikube)

This project demonstrates an end-to-end DevOps workflow:

A Python Flask web application (simple “Welcome to my page" UI)
Containerized using Docker
Deployed to a Kubernetes cluster (Minikube) using Deployment + Service
Application configuration via ConfigMaps and Secrets
Fully automated CI/CD pipeline using Jenkins
GitHub Webhooks trigger Jenkins to build, push, and deploy new updates
Used ngrok to expose Jenkins running inside a Docker container

