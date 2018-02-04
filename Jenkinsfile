#!/usr/bin/env groovy

/**
 * Jenkinsfile
 */
pipeline {
    agent any
    environment {
    }

    stages {

        stage ('Run tests') {
            steps {
                sh """
                make docker_test
                """
            }
        }

        // stage ('Lint') {
        //     steps {
        //         sh """
        //         make docker_test
        //         """
        //     }
        // }


    // post {
    //     failure {
    //         mail body: "${env.JOB_NAME} (${env.BUILD_NUMBER}) ${env.projectName} build error " +
    //                    "is here: ${env.BUILD_URL}\nStarted by ${env.BUILD_CAUSE}" ,
    //              from: env.emailFrom,
    //              //replyTo: env.emailFrom,
    //              subject: "${env.projectName} ${env.JOB_NAME} (${env.BUILD_NUMBER}) build failed",
    //              to: env.emailTo
    //     }
    //     success {
    //         mail body: "${env.JOB_NAME} (${env.BUILD_NUMBER}) ${env.projectName} build successful\n" +
    //                    "Started by ${env.BUILD_CAUSE}",
    //              from: env.emailFrom,
    //              //replyTo: env.emailFrom,
    //              subject: "${env.projectName} ${env.JOB_NAME} (${env.BUILD_NUMBER}) build successful",
    //              to: env.emailTo
    //     }
    // }
}