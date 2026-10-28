pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                
                sh 'pip install -r requirements.txt || python3 -m pip install -r requirements.txt || pip3 install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                
                sh 'python -m unittest test_app.py || python3 -m unittest test_app.py'
            }
        }
    }
}
