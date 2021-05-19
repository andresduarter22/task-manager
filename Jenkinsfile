
pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh 'docker pull 10.28.108.139:8082/task_manager:latest'
        sh 'docker run 10.28.108.139:8082/task_manager'
      }
    }
    stage('Unit tests') {
      steps{
        sh 'docker exec 10.28.108.139:8082/task_manager /tox.ini'
        }
      }
    }
    stage('Static code analysis') {
      steps{
        echo 'TODO sonar sca'

      }
    }
  }
}
