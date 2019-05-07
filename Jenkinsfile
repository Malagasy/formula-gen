pipeline {
    agent none
    stages {
        stage('build') {
            agent { 
                dockerfile { 
                    customWorkspace '/www/app'
                }
            }
            steps {
                sh "pwd"
                sh "ls lib"
                sh 'python --version'
                sh 'pip install -r requirements.txt'
                sh "python -m unittest discover -v -s ${WORKSPACE} -t ${WORKSPACE} -p *test*.py"
            }
        }

    }
}