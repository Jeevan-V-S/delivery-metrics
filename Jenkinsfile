pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {
        stage('Source Checkout') {
            steps {
                echo '=== Stage 1: Checking out source code from SCM ==='
                checkout scm
            }
        }

        stage('Dependency Installation / Build') {
            steps {
                echo '=== Stage 2: Creating Virtual Environment & Installing Dependencies ==='
                // Linux / macOS agent execution
                sh '''
                    python3 -m venv ${VENV} || python -m venv ${VENV}
                    . ${VENV}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Automated Test / Validation') {
            steps {
                echo '=== Stage 3: Running Unit Tests & Validation ==='
                sh '''
                    . ${VENV}/bin/activate
                    pytest test_exporter.py -v --junitxml=test-results.xml
                '''
            }
        }

        stage('Deployment Packaging') {
            steps {
                echo '=== Stage 4: Packaging Deployment Artifacts ==='
                sh '''
                    rm -rf deploy
                    mkdir -p deploy
                    cp exporter.py deploy/
                    cp requirements.txt deploy/
                    echo "Deployment package prepared successfully in deploy/ folder:"
                    ls -la deploy/
                '''
                // Archive artifacts in Jenkins
                archiveArtifacts artifacts: 'deploy/**', fingerprint: true
            }
        }
    }

    post {
        always {
            // Publishes test report in Jenkins UI if JUnit plugin is installed
            junit allowEmptyResults: true, testResults: 'test-results.xml'
        }
        success {
            echo 'SUCCESS: All pipeline stages completed successfully. Runnable artifact archived.'
        }
        failure {
            echo 'FAILURE: Pipeline execution halted due to an error in the preceding stage.'
        }
    }
}
