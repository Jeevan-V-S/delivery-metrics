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
                script {
                    if (isUnix()) {
                        sh '''
                            python3 -m venv ${VENV} || python -m venv ${VENV}
                            . ${VENV}/bin/activate
                            pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    } else {
                        bat '''
                            python -m venv %VENV%
                            call %VENV%\\Scripts\\activate.bat
                            python -m pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    }
                }
            }
        }

        stage('Automated Test / Validation') {
            steps {
                echo '=== Stage 3: Running Unit Tests & Validation ==='
                script {
                    if (isUnix()) {
                        sh '''
                            . ${VENV}/bin/activate
                            pytest test_exporter.py -v --junitxml=test-results.xml || python3 -m unittest test_exporter.py
                        '''
                    } else {
                        bat '''
                            call %VENV%\\Scripts\\activate.bat
                            pytest test_exporter.py -v --junitxml=test-results.xml || python -m unittest test_exporter.py
                        '''
                    }
                }
            }
        }

        stage('Deployment Packaging') {
            steps {
                echo '=== Stage 4: Packaging Deployment Artifacts ==='
                script {
                    if (isUnix()) {
                        sh '''
                            rm -rf deploy
                            mkdir -p deploy
                            cp exporter.py deploy/
                            cp requirements.txt deploy/
                            echo "Deployment directory contents:"
                            ls -la deploy/
                        '''
                    } else {
                        bat '''
                            if exist deploy rmdir /s /q deploy
                            mkdir deploy
                            copy /y exporter.py deploy\\
                            copy /y requirements.txt deploy\\
                            echo Deployment directory contents:
                            dir deploy
                        '''
                    }
                }
                archiveArtifacts artifacts: 'deploy/**', fingerprint: true
            }
        }
    }

    post {
        always {
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
