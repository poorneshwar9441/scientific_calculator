pipeline{
  agent any
  stages{

stage('Git Pull') {
  steps {
      git url: 'https://github.com/poorneshwar9441/scientific_calculator.git',
      branch: 'main',
      credentialsId: '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'
} }
stage('Build') {
  steps {
      sh 'echo Build step'
} }
stage('Test') {
    steps {
        sh 'python3 test_calculator.py'
    }
}
 }
}