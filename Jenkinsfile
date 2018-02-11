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
                withCredentials([usernameColonPassword(credentialsId: 'docker_hub_password', variable: 'DOCKER_HUB_PASSWORD')]) {
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
                    currentBuild.result == null || currentBuild.result == 'SUCCESS' 
                }
            }
            steps {
                build job: 'web-app-deploy/master', wait: true, parameters: [[$class: 'StringParameterValue', name: 'apps', value: 'volunteer_dashboard_api']]
            }
        }

    }
    // post {
        // failure {
        //     mail body: "${env.JOB_NAME} (${env.BUILD_NUMBER}) ${env.projectName} build error " +
        //                "is here: ${env.BUILD_URL}\nStarted by ${env.BUILD_CAUSE}" ,
        //          from: env.emailFrom,
        //          //replyTo: env.emailFrom,
        //          subject: "${env.projectName} ${env.JOB_NAME} (${env.BUILD_NUMBER}) build failed",
        //          to: env.emailTo
        // }
        // success {
        //             }
    // }
}