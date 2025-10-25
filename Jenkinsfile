pipeline{
  agent any

  stages{
    stage('Install dependencies'){
      steps{
        sh '''
          python -m venv myenv
          ./myenv/bin/pip install --upgrade pip
          ./myenv/bin/pip install -r requirements.txt
        '''
      }
    }

    stage('Run tests'){
      steps{
        sh './myenv/bin/pytest -v --maxfail=1'
      }
    }
    stage('Check code coverage'){
      steps{
        sh './myenv/bin/pytest --cov --cov-report=html'
      }
    }

    stage('Upload artifact'){
      steps{
        archiveArtifacts artifacts: 'htmlcov/**', fingerprint: true
      }
    }
  }

  post{
    always{
      echo 'Pipeline completed'
      cleanWs()
    }
  }
}