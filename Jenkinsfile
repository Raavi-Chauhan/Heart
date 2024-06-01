node {
    // Define environment variables
    //def dockerHubCredentialsId = 'Dockerhub // Replace with your Docker Hub credentials ID'
    def dockerImageName = 'raavi13/new'
    def gitRepoUrl = 'https://github.com/Raavi-Chauhan/Heart.git'
    def gitBranch = 'main'
    def dockerHubUsername ='raavi13'
    def dockerHubPassword ='Nice2Meetyou'
    
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
        }

        stage('Push Docker image to DockerHub'){
            //docker.withRegistry('https://hub.docker.com/', dockerHubCredentialsId) {
            //sh "docker push ${imageName}"
            //}
            def buildNumber = env.BUILD_NUMBER
            def imageName = "${dockerImageName}:${buildNumber}"
            sh "docker login -u '${dockerHubUsername}' https://index.docker.io/v1/ --password '${dockerHubPassword}'"
            //sh "docker login -u "raavi13" --password 'Nice2Meetyou'"
            // Push the image to Docker Hub
            sh "docker push ${imageName}"

        }

        stage('Deply on Kubernetes'){
            def buildNumber = env.BUILD_NUMBER
            sh "kubectl apply -f deployment.yaml"
            sh "kubectl apply -f servive.yaml"
            sh "kubectl get svc -n jenkins"
            sh "minikube service heart-service -n jenkins --url"
            sd "kubectl port-forward service/heart-service --address 0.0.0.0 3000:80"
            

    } catch (Exception e) {
        // Handle errors
        echo "Error: ${e.getMessage()}"
        currentBuild.result = 'FAILURE!!'
    }
}
