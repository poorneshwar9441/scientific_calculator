pipeline{
  agent any

  environment {
    CI = 'true'
    registry = 'spoider/pyth'
    DOCKERHUB_CRED = credentials('dockee')
    registryCredential = 'dockee'
    dockerimage = ''
}
stages{

stage('Git Pull') {
  steps {
      git url: 'https://github.com/poorneshwar9441/scientific_calculator.git',
      branch: 'main',
      credentialsId: ''
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
stage('Build Docker Image') {
  steps {
    script{
       dockerimage = sh '/usr/local/bin/docker build -t '+registry+':v1.0 .'
} }


}
stage('Push Image to dockerHub') {
    steps {
      script{
          sh '/usr/local/bin/docker push ' +registry +':v1.0'
} }
}

stage('Free local space') {
    steps {
        sh '/usr/local/bin/docker rmi $registry:v1.0'
    }
}
stage('Deploy'){
    steps{
    sh '/Users/poorneshwarreddychaganti/Library/Python/3.9/bin/ansible-playbook playbook.yml -i inventory -e image_name=spoider/pyth'
     }
}

 }

}