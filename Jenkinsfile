pipeline {
    agent any
    triggers { 
      githubPush() 
   }
    environment {
        DOCKER_IMAGE_NAME = 'archis002/calculator'
        GITHUB_REPO_URL = 'https://github.com/ArchisKulkarni002/SPE_Miniproject.git'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout the code from the GitHub repository
                    git branch: 'master', url: "${GITHUB_REPO_URL}"
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run tests
                    sh 'python3 testit.py'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    docker.build("${DOCKER_IMAGE_NAME}", '.')
                }
            }
        }

        stage('Push Docker Images') {
            steps {
                script{
                    docker.withRegistry('', 'DockerHubCred') {
                    sh 'docker tag archis002/calculator archis002/calculator:latest'
                    sh 'docker push archis002/calculator'
                    }
                 }
            }
        }

   stage('Run Ansible Playbook') {
            steps {
                script {
                    ansiblePlaybook(
                        playbook: 'deploy.yml',
                        inventory: 'inventory'
                     )
                }
            }
        }

    }
}
