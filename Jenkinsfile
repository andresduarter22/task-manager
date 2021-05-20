
pipeline {
    agent any

    environment{
      PROJECT_NAME="task_manager"
    }

    stages {
        stage('Install Requirements') {
            steps {
                sh '''
                
                os_ver=$(uname -s)
                os_needed="Linux"

                if [ "$os_ver" != "$os_needed" ];then
                    echo "OS Mismatch!"
                    exit 1
                fi

                #GET the python version, only the major release number
                var=$(python3 -c \'import platform; major, _, _ = platform.python_version_tuple(); print(major)\')

                case "$var" in
                "3")
                    echo "python 3 detected";
                    ;;
                *)
                    echo "no python detected, please install python 3.8"
                    exit 1
                    ;;
                esac
                
                pip3 install -r requirements.txt
                '''
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
                        def scannerHome = tool'sonarqube-scanner-at'
                        withSonarQubeEnv('sonarqube-task-manager'){
                            sh"${scannerHome}/bin/sonar-scanner -Dsonar.projectName=$PROJECT_NAME -Dsonar.projectKey=$PROJECT_NAME -Dsonar.sources=./task_manager"}
                    }
                }
            }

            stage('Build Docker Image') {
                steps{
                    sh """
                        docker build -t task_manager:0.$BUILD_NUMBER .
                        docker tag task_manager:0.$BUILD_NUMBER 10.28.108.139:8082/task_manager:0.$BUILD_NUMBER
                        echo Docker image built
                    """
                }
            }
            stage('Promote Docker Image') {
                steps{
                    sh """
                        docker login -u admin -p admin123 10.28.108.139:8082
                        docker push 10.28.108.139:8082/task_manager:0.$BUILD_NUMBER
                        echo Docker image succesfully pushed
                    """
                }
            }
            
        }
    post {
        always {
            emailext body: default, recipientProviders: default, default, subject: default
        }
    }
}
