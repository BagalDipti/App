pipeline {
  environment {
        registry = "diptibagal3010"
        dockerImage = ''
        Name = "my_image"
  }
  agent any
  stages {
    stage('Cloning Git') {
      steps {
        git 'http://gsgit.gslab.com/dipti_bagal/Jenkins.git'
      }
    }
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build registry + "/" +Name+":$BUILD_NUMBER"
        }
      }
    }
    stage('Deploy Image') {
      steps{
        script {
          docker.withRegistry( '' ) {
            dockerImage.push()
          }
        }
      }
    }
    stage('Docker Run') {
        steps {
          script {
            dockerImage.run(" -p 9191:9090 --rm --name flaskcontainer")
          }
        }

    }

  }
}
