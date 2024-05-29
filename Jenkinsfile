node {
    // Define environment variables
    def dockerHubCredentialsId = 'Dockerhub // Replace with your Docker Hub credentials ID
    def dockerImageName = 'raavi/heart_13'
    def gitRepoUrl = 'https://github.com/Raavi-Chauhan/Heart.git'
    def gitBranch = 'main'
    
    // Catch any errors in the build process
    try {
        // Trigger the build on GitHub pull request
        properties([
            pipelineTriggers([[$class: 'GitHubPushTrigger']])
        ])
        
        stage('Clone Repository') {
            // Clone the repository from GitHub
            cleanWs()
            git branch: gitBranch, url: gitRepoUrl
        }

        stage('Build Docker Image') {
            // Build the Docker image with the build number as the tag
            def buildNumber = env.BUILD_NUMBER
            def imageName = "${dockerImageName}:${buildNumber}"
            sh "docker build -t ${imageName} ."


            docker.withRegistry('https://hub.docker.com/', dockerHubCredentialsId) {
            sh "docker push ${imageName}"
            }
            //sh "docker login -u "raavi13" --password 'Nice2Meetyou'"
            // Push the image to Docker Hub
            //sh "docker push ${imageName}"

        }

    } catch (Exception e) {
        // Handle errors
        echo "Error: ${e.getMessage()}"
        currentBuild.result = 'FAILURE'
    }
}
