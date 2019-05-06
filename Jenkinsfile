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
                sh 'pip install -r requirements.txt'
                sh 'python -m unittest discover -v -s . -t . -p *test*.py'
            }
        }

    }
}