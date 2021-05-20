
pipeline {
    agent any
    
    environment{
      PROJECT_NAME="task_manager"
    }
    
stages {
    stage('Install Requirements') {
        steps {
          
            sh """
            #Check if OS is Linux, else quit
            os_ver=$(uname -s)
            os_needed="Linux"

            if [ "$os_ver" != "$os_needed" ];then
                echo "OS Mismatch!"
                exit 1
            fi

            #GET the python version, only the major release number
            var=$(python3 -c 'import platform; major, _, _ = platform.python_version_tuple(); print(major)')

            case "$var" in
            "1")
                echo "LOL, python 1!?  proceeding to install python 3.8";
                sudo apt update
                sudo apt install python3-pip
                ;;
            "2")
                echo "python 2 detected,  proceeding to install python 3.8";
                sudo apt update
                sudo apt install python3-pip
                ;;
            "3")
                echo "python 3 detected";
                ;;
            *)
                echo "no python detected, proceeding to install python 3.8"
                sudo apt update
                sudo apt install python3-pip
                ;;
            esac

            # Check if in a VENV
            INVENV=$(python3 -c 'import sys; print ("1" if hasattr(sys, "real_prefix") else "0")')
            case "$INVENV" in
            "0")
                echo "No virtual environment found.. Installing Venv Now...";
                sudo pip3 install virtualenv
                virtualenv venv
                source venv/bin/activate
                ;;
            "1")
                echo "python VENV found";
                ;;
            esac
            """
            }
        }
      
        stage('Unit tests') {
            steps{
          
                echo "---------------------------------"
                echo "Starting Tox..."
                echo "---------------------------------"
                sh 'tox -vvv .'
                }
        }
    
    
        stage ('Static Code Analysis') {
            steps{
                script {
                    def scannerHome = tool'sonarqube-task-manager'
                    withSonarQubeEnv('sonarqube-automation'){
                        sh"${scannerHome}/bin/sonar-scanner -Dsonar.projectName=$PROJECT_NAME -Dsonar.projectKey=$PROJECT_NAME -Dsonar.sources=/task_manager"}
                }
            }
        } 
    
        stage('Build Docker Image') {
            steps{
                sh """ 
                    docker build -t task_manager:$BUILD_NUMBER .
                    sh docker tag task_manager:$BUILD_NUMBER 10.28.108.139:8082/task_manager:$BUILD_NUMBER
                    echo Docker image built
                """
            }
        }
        stage('Promote Docker Image') {
            steps{
                sh """
                    docker push 10.28.108.139:8082/task_manager:$BUILD_NUMBER .
                    echo Docker image succesfully pushed
                """
            }
        }
    }
}
