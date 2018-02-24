#!/usr/bin/env groovy

/**
 * Jenkinsfile
 */
pipeline {
    agent any

    stages {

        stage ('Run tests') {
            
            steps {
                sh """
                sudo docker build -f Dockerfile_test . -t jenkins_test
                sudo docker run --rm jenkins_test
                """
            }
        }

        stage ('deploy to docker hub') {
            
            steps {
                withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'docker_hub_password', usernameVariable: 'USERNAME', passwordVariable: 'DOCKER_HUB_PASSWORD']]) {
                    sh """
                    sudo docker build . -t villy393/volunteer_dashboard_api:$env.BRANCH_NAME
                    # feed password into std-in so that it isn't printed in output
                    echo $DOCKER_HUB_PASSWORD | sudo docker login -u villy393 --password-stdin
                    sudo docker push villy393/volunteer_dashboard_api:$env.BRANCH_NAME
                    """
                }
            }
        }


        stage ('deploy') {
            when {
                expression {
                    (currentBuild.result == null || currentBuild.result == 'SUCCESS') && env.BRANCH_NAME == 'master'
                }
            }
            steps {
                build job: 'web-app-deploy/master', wait: true, parameters: [[$class: 'StringParameterValue', name: 'apps', value: 'volunteer_dashboard_api']]
            }
        }

    }
}