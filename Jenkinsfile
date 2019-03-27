pipeline {
    environment {
        PATH = "C:\\Program Files\\Git\\usr\\bin;${env.PATH}"
    }
    agent none
    stages {
        stage('build') {
            agent { 
                docker {
                    image 'python:3.7.2-alpine' 
                }
                
            }
            steps {
                bat 'ls -l'
            }
        }
    }
}