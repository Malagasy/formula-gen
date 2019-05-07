pipeline {
    agent none
    stages {
        stage('build') {
            agent { 
                dockerfile true
            }
            steps {
                sh "pwd"
                sh "ls"
                sh 'python --version'
                sh 'pip install -r requirements.txt'
                sh "python -m unittest discover -v -s ${WORKSPACE} -t ${WORKSPACE} -p *test*.py"
            }
        }

    }
}