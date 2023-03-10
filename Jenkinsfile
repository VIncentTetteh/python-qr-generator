pipeline{
  agent any
  stages{
    stage("SCM"){
      steps{
        git branch: 'main', credentialsId: 'github-credentials', url: 'https://github.com/VIncentTetteh/python-qr-generator'
        echo "hello world"
        echo "it works!!"
      }
    }
  }
}
