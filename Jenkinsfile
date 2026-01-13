pipeline {
    agent any

    environment {
        IMAGE_NAME = "devops-intern-task"
        DOCKER_USER = "mallikarjuningali"
        IMAGE_TAG = "latest"
    }

    triggers {
        githubPush()
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Mallikarjuningali/myTask2.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Lint Code') {
            steps {
                sh '''
                . venv/bin/activate
                flake8 . --exclude=venv,__pycache__,migrations
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                export SECRET_KEY=test-secret-key-for-ci
                export DEBUG=True
                python manage.py test
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t $DOCKER_USER/$IMAGE_NAME:$IMAGE_TAG .
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    docker push $DOCKER_USER/$IMAGE_NAME:$IMAGE_TAG
                    '''
                }
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker stop app || true
                docker rm app || true
                docker pull $DOCKER_USER/$IMAGE_NAME:$IMAGE_TAG
                docker run -d --name app -p 80:8000 $DOCKER_USER/$IMAGE_NAME:$IMAGE_TAG
                '''
            }
        }
    }
}

