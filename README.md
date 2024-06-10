**Project Overview**

This project aims to predict the likelihood of heart disease using machine learning models and deploy a user-friendly web interface for users to interact with the prediction model. The web application is built using Flask. The machine learning model is trained on a heart disease dataset and is designed to provide accurate predictions based on user inputs and all this is deployed using devops culture.

**Features**

- **User-Friendly Interface**: A simple and intuitive web interface for inputting user data and displaying predictions.
- **Machine Learning Model**: Utilizes a neural network model built with TensorFlow and Keras to predict the probability of heart disease.
- **Data Preprocessing**: Includes steps for data cleaning, feature selection, and data normalization to ensure high model performance.
- **Continuous Integration/Continuous Deployment (CI/CD)**: Automated deployment pipeline using Git, Jenkins, Docker, and Kubernetes.

#### Technologies Used

- **Python**: The core programming language used for the project.
- **Flask**: For building the web application.
- **TensorFlow & Keras**: For developing the machine learning model.
- **Pandas**: For data manipulation and preprocessing.
- **Docker**: For containerizing the application.
- **Jenkins**: For automating the CI/CD pipeline.
- **Kubernetes**: For deploying and managing containerized applications in a clustered environment.
- **Git**: For version control and source code management.


#### Deployment

The project includes a Jenkinsfile and Dockerfile to automate the build, test, and deployment processes. The CI/CD pipeline ensures that every change is tested and deployed seamlessly.

1. **Jenkins Pipeline Setup**
   - Set up Jenkins with necessary plugins for Git, Docker, and Kubernetes.
   - Create a Jenkins pipeline job and point it to the repository.

2. **Docker Setup**
   - Build the Docker image:
   - Run the Docker container:
 

3. **Kubernetes Deployment**
   - Create Kubernetes deployment and service files.
   - Deploy to the Kubernetes cluster:

#### Usage

1. Navigate to the application URL.
2. Enter the required health parameters (Age, Sex, Blood Pressure, Cholesterol, etc.).
3. Submit the form to get the prediction on the likelihood of having heart disease.

#### Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

#### Acknowledgments

- Special thanks to the team at GlobalLogic for their guidance and support throughout the internship.
- Thanks to the open-source community for the tools and libraries that made this project possible.
