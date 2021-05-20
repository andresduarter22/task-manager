pipeline {
  agent {label ' automation-a'}

  environment{
      POSTGRES_USER="sonar"
      POSTGRES_PASSWORD="sonaradmin"
      PROJECT_NAME="task_manager"
  }

  stages {
    stage('Install requirements') {
      steps {
        sh '''
        #!/bin/bash
        sudo apt install docker
        sudo apt install python3-pip
        sudo apt install python3-venv
        wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
        echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
        sudo apt -y install mongodb-org
        DIR="./venv"
        if [ ! -d "$DIR" ]; then
        python3 -m venv venv
        fi
        . ./venv/bin/activate
        export PYTHONPATH="$(pwd)"
        pip3 install -r requirements.txt
        ./venv/bin/python3 tests/test_db_task.py
        '''
      }
    }
    /*stage('Unit tests') {
      steps{
        //sh 'docker exec 10.28.108.139:8082/task_manager /tox.ini'
        //sh './venv/bin/python3 tests/test_db_task.py'
        }
      }
    }*/
    stage('Run SonarQube') {
      steps {
        script{
            def scannerHome = tool 'sonarqube-scanner-at'
            withSonarQubeEnv('sonarqube-automation') {
            sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectName=$PROJECT_NAME -Dsonar.projectKey=$PROJECT_NAME -Dsonar.sources=."
        }
        /*sh '''
            docker volume create --name sonarqube_data
            docker volume create --name sonarqube_extensions
            docker volume create --name sonarqube_logs
            docker run -d --name sonardb --network devops --restart always -e POSTGRES_USER=$POSTGRES_USER -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD -v ~/Documents/postgresql:/var/lib/postgresql -v ~/postgresql_data:/var/lib/postgresql/data postgres:12.1-alpine
            docker run -d --name sonarqube --network devops -p 9000:9000 -e SONAR_JDBC_URL=jdbc:postgresql://sonardb:5432/sonar -e SONAR_JDBC_USERNAME=$POSTGRES_USER -e SONAR_JDBC_PASSWORD=$POSTGRES_PASSWORD -v sonarqube_data:/opt/sonarqube/data -v sonarqube_extensions:/sonarqube/extensions -v sonarqube_logs:/opt/sonarqube/logs sonarqube:8.9.0-community
            docker run --network devops --rm -e SONAR_HOST_URL="http://sonarqube:9000" -e SONAR_LOGIN="618532770490e6d78d802fe043eca3d96168edb2"  -v $PWD:/usr/src sonarsource/sonar-scanner-cli -Dsonar.projectKey="task_manager"
            '''
            */
      }
    }
    stage('Build image with docker-compose') {
      steps{
        echo 'TODO docker-compose build and push here'
      }
    }
    stage('Promote image to registry - Nexus') {
      steps{
        echo 'TODO sonar sca'
      }
    }
  }
