pipeline {
    agent any

    stages {
        stage ('Verify branch') {
            steps {
                echo "$GIT_BRANCH"
            }
        }

        stage ('Build Docker image') {

            steps {
                pwsh(script: 'docker images -a')
                pwsh(script: """
                    cd azure-vote
                    docker images -a 
                    docker build -t azure-vote-jenkins
                    cd..
                """)
            }
        }
    }
}