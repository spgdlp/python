pipeline {
  agent any
  stages {
    stage('python version') {
      steps {
        bat 'python --version'
      }
    }
    stage('descompress') {
      steps {
        bat 'python descompresor_zip.py'
      }
    }
  }
}
