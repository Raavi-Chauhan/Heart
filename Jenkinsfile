node {
    // Define environment variables
    //def dockerHubCredentialsId = 'Dockerhub // Replace with your Docker Hub credentials ID'
    def dockerImageName = 'raavi13/new'
    def gitRepoUrl = 'https://github.com/Raavi-Chauhan/Heart.git'
    def gitBranch = 'main'
    def dockerHubUsername ='raavi13'
    def dockerHubPassword ='Nice2Meetyou'
    def kubernetesCredentialsId = 'Kubernetes-Token'  // Replace with your Kubernetes credentials ID
    def kubeconfigPath = '/home/ubuntu/.kube/config'  // Path where kubeconfig is stored on Jenkins

    
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
            sh """
                sed 's|IMAGE_TAG|${buildNumber}|g' deployment.yaml > deployment-processed.yaml
                sed 's|IMAGE_TAG|${buildNumber}|g' pod.yaml > pod-processed.yaml
                cp servive.yaml servive-processed.yaml
            """

            // Deploy to Minikube
            withCredentials([string(credentialsId: kubernetesCredentialsId, variable: 'KUBE_TOKEN')]) {
                sh 'sudo chmod 777 /home/ubuntu/.kube/'
                sh 'mkdir -p /var/lib/jenkins/.kube'
                //sh "echo \"${KUBE_TOKEN}\" > ${kubeconfigPath}"

                // Apply the Kubernetes manifests
                sh "kubectl --kubeconfig=${kubeconfigPath} apply -f deployment-processed.yaml --validate=false"
                sh "kubectl --kubeconfig=${kubeconfigPath} apply -f pod-processed.yaml --validate=false"
                sh "kubectl --kubeconfig=${kubeconfigPath} apply -f servive-processed.yaml --validate=false"
            }
        }
            
        
    } catch (Exception e) {
        // Handle errors
        echo "Error: ${e.getMessage()}"
        currentBuild.result = 'FAILURE!!'
    }
}
