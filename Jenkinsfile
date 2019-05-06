pipeline {
    agent none
    stages {
        stage('build') {
            agent { 
                docker {
                    image "python:3.7.2-alpine"
                }
            }
            steps {
                sh 'ls -la'
            }
        }

    }
}