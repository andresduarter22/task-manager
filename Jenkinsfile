pipeline {
    agent{label 'automation-r'}

    environment{
      PROJECT_NAME="task_manager"
      NEXUS_URL = "10.28.108.139:8082"
      EMAIL_HEADER = "Hi Devs!\nYour Jenkins here reporting, pipeline execution completed!\n"
    }

    stages {
        stage('Install Requirements') {
            environment{
                JENKINS_AUTH = 'jenkins'
                }

            steps {

                sh '''

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


                pip3 install -r requirements.txt
                '''
                }
            }

            stage ('Unit Tests') {
            steps {
                sh """
                python3 -m coverage run --source=tests/ 
                python3 -m coverage xml
                """
            }
        }

            stage ('Static Code Analysis') {
                steps{
                    script {
                        def scannerHome = tool'sonarqube-scanner-at'
                        withSonarQubeEnv('sonarqube-task-manager'){
                            sh"${scannerHome}/bin/sonar-scanner -Dsonar.projectName=$PROJECT_NAME -Dsonar.projectKey=$PROJECT_NAME -Dsonar.python.coverage.reportPaths=coverage.xml -Dsonar.sources=./task_manager"}
                    }
                }
            }

            stage('Build Docker Staging Image') {
                when {
                    branch 'development'
                }
                steps{
                    sh 'docker build -t $NEXUS_URL/task_manager:0.$BUILD_NUMBER-stg .'
                }
            }
        
            stage('Build Docker Production Image') {
                when {
                    branch 'master'
                }
                steps{
                    sh 'docker build -t $NEXUS_URL/task_manager:0.$BUILD_NUMBER-prod .'
                }
            } 
        
            

            stage('Mount Docker Staging Image') {
                when {
                    branch 'development'
                }
                steps{

                    sh """
                        docker run -d -v /home/ubuntu/mongo/data/:/mongo-data mongo
                        docker run -d $NEXUS_URL/task_manager:0.$BUILD_NUMBER-stg
                    """
                }
            }

            stage('Mount Docker Production Image') {
                when {
                    branch 'master'
                }
                steps{

                    sh """
                        docker run -d -v /home/ubuntu/mongo/data/:/mongo-data mongo
                        docker run -d $NEXUS_URL/task_manager:0.$BUILD_NUMBER-prod
                    """
                }
            }

            stage('Acceptance Testing') {
                when {
                    branch 'development'
                }
                steps{

                    sh """
                        /bin/curl http://localhost:5000/api/v1/tasks/db | grep 200
                        /bin/curl http://localhost:5000/api/v1/api_tasks?config={'load_default':'False','url':'http://httpbin.org/get','r_type':'GET'}&data=[]&priority=100 | grep 200

                    """
                }
            }

            stage('Promote Docker Staging Image') {
                when {
                    branch 'development'
                }
                environment{
                      NEXUS_CREDENTIAL = credentials("nexus-credential")
                }
                steps{

                    sh """
                        echo $NEXUS_CREDENTIAL_PSW | docker login -u $NEXUS_CREDENTIAL_USR --password-stdin $NEXUS_URL
                        docker push $NEXUS_URL/task_manager:0.$BUILD_NUMBER-stg 
                    """
                }
            }
        
            stage('Promote Docker Production Image') {
                when {
                    branch 'master'
                }
                environment{
                      NEXUS_CREDENTIAL = credentials("nexus-credential")
                }
                
                steps{

                    sh """
                        echo $NEXUS_CREDENTIAL_PSW | docker login -u $NEXUS_CREDENTIAL_USR --password-stdin $NEXUS_URL
                        docker push $NEXUS_URL/task_manager:0.$BUILD_NUMBER-prod
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
            sh '''docker logout $NEXUS_URL'''
            
        }
    }
}
