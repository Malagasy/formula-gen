pipeline {
    agent none
    stages {
        stage('build') {
            agent { 
                dockerfile true
            }
            steps {
                sh 'ls -l'
            }
        }
    }
}