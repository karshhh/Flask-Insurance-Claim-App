pipeline {
    agent any
    environment {
        ECR_REPO = "aws_account_id.dkr.ecr.region.amazonaws.com/insurance-claim"
        IMAGE_TAG = "v1"
    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/karshhh/Flask-Insurance-Claim-App.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("insurance-claim:${IMAGE_TAG}")
                }
            }
        }
        stage('Push to ECR') {
            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-creds']]) {
                    sh '''
                    aws ecr get-login-password --region region | docker login --username AWS --password-stdin $ECR_REPO
                    docker tag insurance-claim:${IMAGE_TAG} $ECR_REPO:${IMAGE_TAG}
                    docker push $ECR_REPO:${IMAGE_TAG}
                    '''
                }
            }
        }
        stage('Deploy to EKS') {
            steps {
                sh 'kubectl apply -f k8s/'
            }
        }
    }
}
