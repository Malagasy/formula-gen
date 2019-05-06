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
                sh 'python --version'
                sh 'pip install -r requirements.txt'
                sh "python -m unittest discover -v -s ${WORKSPACE} -t ${WORKSPACE} -p '*test*.py'"
            }
        }

    }
}