pipeline {
    agent {
        label 'linux'
    }

    environment {
        APP_NAME = 'jenkins_python_demo'
        APP_VERSION = '1.0.0'
        DEPLOY_DIR = '/opt/jenkins-python-wheel-demo'
        VENV_DIR = '/opt/jenkins-python-wheel-demo/venv'
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Step 1: Pulling latest code from GitHub'
                checkout scm
            }
        }

        stage('Check Python and Pip') {
            steps {
                echo 'Step 2: Checking Python and pip versions'
                sh '''
                    python3 --version
                    python3 -m pip --version
                '''
            }
        }

        stage('Create Virtual Environment') {
            steps {
                echo 'Step 3: Creating local virtual environment for Jenkins workspace'
                sh '''
                    rm -rf .venv
                    python3 -m venv .venv
                    . .venv/bin/activate
                    python -m pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Step 4: Installing test and build dependencies'
                sh '''
                    . .venv/bin/activate
                    python -m pip install -r requirements-dev.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Step 5: Running unit tests using pytest'
                sh '''
                    . .venv/bin/activate
                    python -m pytest -v
                '''
            }
        }

        stage('Build Wheel') {
            steps {
                echo 'Step 6: Building Python wheel file'
                sh '''
                    . .venv/bin/activate
                    rm -rf dist build *.egg-info src/*.egg-info
                    python -m build
                    echo "Generated wheel file:"
                    ls -lh dist/
                '''
            }
        }

        stage('Verify Wheel') {
            steps {
                echo 'Step 7: Verifying wheel file exists'
                sh '''
                    test -f dist/${APP_NAME}-${APP_VERSION}-py3-none-any.whl
                    echo "Wheel verification successful"
                '''
            }
        }

        stage('Deploy Wheel') {
            steps {
                echo 'Step 8: Deploying wheel file to deployment directory'
                sh '''
                    mkdir -p ${DEPLOY_DIR}
                    cp dist/${APP_NAME}-${APP_VERSION}-py3-none-any.whl ${DEPLOY_DIR}/
                    echo "Wheel deployed to ${DEPLOY_DIR}"
                    ls -lh ${DEPLOY_DIR}
                '''
            }
        }

        stage('Install Deployed Wheel') {
            steps {
                echo 'Step 9: Installing deployed wheel in deployment virtual environment'
                sh '''
                    rm -rf ${VENV_DIR}
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    python -m pip install --upgrade pip
                    python -m pip install ${DEPLOY_DIR}/${APP_NAME}-${APP_VERSION}-py3-none-any.whl
                '''
            }
        }

        stage('Run Application') {
            steps {
                echo 'Step 10: Running installed application from wheel command'
                sh '''
                    . ${VENV_DIR}/bin/activate
                    jenkins-python-demo
                '''
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: Code pulled, tested, wheel built, deployed, installed, and executed successfully.'
        }

        failure {
            echo 'FAILED: Pipeline failed. Please check the failed stage in Jenkins console output.'
        }

        always {
            echo 'Pipeline execution finished.'
        }
    }
}
