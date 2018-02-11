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

        stage ('deploy') {
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS' 
                }
            }
            steps {
                build job: 'web-app-deploy', wait: true, parameters: [[$class: 'StringParameterValue', name: 'apps', value: 'volunteer_dashboard_api']]
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