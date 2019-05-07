pipeline {
    agent none
    stages {
        stage('build') {
            agent { 
                dockerfile true
            }
            steps {
                sh "python -m xmlrunner discover -v -s ${WORKSPACE} -t ${WORKSPACE} -p *test*.py -o ${WORKSPACE}/reports"
            }
        }

    }
}