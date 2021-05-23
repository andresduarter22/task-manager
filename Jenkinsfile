pipeline {
//just testing webhooks :D
    agent any

    environment{
      PROJECT_NAME="task_manager"
      NEXUS_URL = "10.28.108.139:8082"
      EMAIL_HEADER = "Hi Devs!\nYour Jenkins here reporting, pipeline execution completed!\n"
    }

    stages {
        stage('Install Requirements') {
            steps {
                sh '''

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
                            sh"${scannerHome}/bin/sonar-scanner \-Dsonar.projectName=$PROJECT_NAME -Dsonar.projectKey=$PROJECT_NAME -Dsonar.sources=./task_manager"}
                    }
                }
            }

            stage('Build Docker Image') {
                steps{
                    sh 'docker build -t $NEXUS_URL/task_manager:0.$BUILD_NUMBER .'
                }
            }
            stage('Promote Docker Image') {
                environment{
                      NEXUS_CREDENTIAL = credentials("nexus-credential")
                }
                steps{

                    sh """
                        echo $NEXUS_CREDENTIAL_PSW | docker login -u $NEXUS_CREDENTIAL_USR --password-stdin $NEXUS_URL

                        docker push $NEXUS_URL/task_manager:0.$BUILD_NUMBER
                    """
                }
            }

        }
    post {
        always {
            emailext body: "$EMAIL_HEADER ${currentBuild.currentResult}: Job ${env.JOB_NAME} build ${env.BUILD_NUMBER}\n More info at: ${env.BUILD_URL}",
                recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']],
                subject: "Jenkins Build ${currentBuild.currentResult}: Job ${env.JOB_NAME}",
                to: '$DEFAULT_RECIPIENTS'
            sh """
            docker rmi -f $NEXUS_URL/task_manager:0.$BUILD_NUMBER
            docker logout $NEXUS_URL
            """
        }
    }
}
