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
                    cd azure-vote/
                    docker images -a 
                    docker build -t azure-vote-jenkins .
                    cd..
                """)
            }
        }
        stage ('Start container') {
            steps {
                pwsh(script: 'docker-compose up -d')

            }
            post {
                success {
                    echo "App started with success!"
                }
                failure {
                    echo "App not started!"
                }
            }
        }
        stage ('Test') {
            steps {
                pwsh(script: """
                    cd python-test/
                    python3 ping.py
                    """)
            }
        }
        stage ('End container') {
            steps {
                pwsh(script: """
                    cd ..
                    docker-compose down
                    """)

            }
        }
    }
}