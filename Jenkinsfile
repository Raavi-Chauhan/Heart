node {
    // Define environment variables
    //def dockerHubCredentialsId = 'Dockerhub // Replace with your Docker Hub credentials ID'
    def dockerImageName = 'raavi13/new'
    def gitRepoUrl = 'https://github.com/Raavi-Chauhan/Heart.git'
    def gitBranch = 'main'
    def dockerHubUsername ='raavi13'
    def dockerHubPassword ='Nice2Meetyou'
    def kubernetesCredentialsId = 'Kubernetes-Token'  // Replace with your Kubernetes credentials ID
    def kubeconfigPath = '/home/ubuntu/kubes/configs.yaml'  // Path where kubeconfig is stored on Jenkins

    
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
            //def buildNumber = env.BUILD_NUMBER
            //sh """
                //sed 's|IMAGE_TAG|${buildNumber}|g' deployment.yaml > deployment-processed.yaml
                //sed 's|IMAGE_TAG|${buildNumber}|g' pod.yaml > pod-processed.yaml
                //cp servive.yaml servive-processed.yaml
            //"""
            script {
                        def deploymentYaml = readFile 'deployment.yaml'
                        def processedDeploymentYaml = deploymentYaml.replace('raavi13/new:latest', "${dockerImageName}:${env.BUILD_NUMBER}")
                        writeFile file: 'deployment-processed.yaml', text: processedDeploymentYaml

                        // Process pod.yaml if needed
                        def podYaml = readFile 'pod.yaml'
                        def processedPodYaml = podYaml.replace('raavi13/new:latest', "${dockerImageName}:${env.BUILD_NUMBER}")
                        writeFile file: 'pod-processed.yaml', text: processedPodYaml
                    }
            // Deploy to Minikube
            withCredentials([string(credentialsId: kubernetesCredentialsId, variable: 'KUBE_TOKEN')]) {
                //sh 'mkdir -p /var/lib/jenkins/.kube'
                //sh "echo \"${KUBE_TOKEN}\" > ${kubeconfigPath}"

                // Apply the Kubernetes manifests
                
                sh 'kubectl --token $KUBE_TOKEN --server https://192.168.49.2:8443 --insecure-skip-tls-verify=true apply -f deployment.yaml -n jenkins '
                //sh "kubectl --kubeconfig=${kubeconfigPath} apply -f deployment-processed.yaml --validate=false"
                sh 'kubectl --token $KUBE_TOKEN --server https://192.168.49.2:8443 --insecure-skip-tls-verify=true apply -f servive.yaml -n jenkins '
                sh 'kubectl --token $KUBE_TOKEN --server https://192.168.49.2:8443 --insecure-skip-tls-verify=true apply -f pod.yaml -n jenkins '
               //sh "kubectl --kubeconfig=${kubeconfigPath} apply -f pod-processed.yaml --validate=false"
                sh 'kubectl --token $KUBE_TOKEN --server https://192.168.49.2:8443 --insecure-skip-tls-verify=true get svc -n jenkins '
                //sh 'minikube service heart-service -n jenkins --url'
                //sh 'kubectl --token $KUBE_TOKEN --server https://192.168.49.2:8443 --insecure-skip-tls-verify=true port-forward service/heart-service -n jenkins --address 0.0.0.0 3000:80 '
                //sh 'kubectl --token $api_token --server https://192.168.49.2:8443 --insecure-skip-tls-verify=true apply -f deployment-processed.yaml '
                //sh "kubectl --kubeconfig=${kubeconfigPath} apply -f servive-processed.yaml --validate=false"
            }
        }
            
        
    } catch (Exception e) {
        // Handle errors
        echo "Error: ${e.getMessage()}"
        currentBuild.result = 'FAILURE!!'
    }
}
