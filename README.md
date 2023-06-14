# CTS Backend Application

The CTS Backend Application is a simple connectivity test server designed to support the mobile multiplayer game "Fun7" by providing latency measurements to determine the best backend server for game connectivity.

## Prerequisites

- Docker: [Installation Guide](https://docs.docker.com/get-docker/)
- Python 3.9 or higher: [Installation Guide](https://www.python.org/downloads/)

## Installation (Run locally)

1. Clone the repository:

   ```bash
   git clone https://github.com/Ilievski-Daniel/cts-backend.git
   ```

2. Change your directory:

   ```bash
   cd cts-backend
   ```

3. Build the Docker image:

    ```
    docker build -t cts-backend .
    ```

4. Access the CTS API endpoint:

    ```
    curl http://localhost:8080/ping
    ```

- The response should be a JSON object with a "message" field.

## Configuration

Port: By default, the application runs on port 8080.

If you wish to change the port, you can modify the main.py file and the Dockerfile. In the main.py file, locate the line app.run(host='0.0.0.0', port=8080) and change the port parameter to your desired port number. Similarly, in the Dockerfile, locate the line EXPOSE 8080 and update the exposed port number accordingly.

Please ensure that you make consistent changes in both files to ensure proper functioning of the application.

## CI/CD Pipeline

The project includes a CI/CD pipeline for automated testing and deployment. 

### It consists of two jobs:

- <b>testing:</b> 
    This job runs on the ubuntu-latest environment and performs linting and unit testing of the application code.

- <b>deploy:</b> 
    This job runs on the ubuntu-latest environment and is triggered only when the testing job is successful and the branch is main. 

    It builds a Docker image, pushes it to Docker Hub, configures the necessary tools for Google Cloud deployment, checks and deletes the existing deployment and service (if any), and then deploys the updated application to the GKE cluster (with pod autoscaling enabled).

Please refer to the [CI/CD Pipeline](/.github/workflows/ci_cd_pipeline.yaml) workflow in the repository for more details on the pipeline configuration.

## GitHub Actions Pipeline Configuration

### Variables

To set up the CI/CD pipeline, you need to define the following variables:

| Variable            |  Description                                                   | 
|:--------------------|:---------------------------------------------------------------|
| GCP_PROJECT_ID      | Google Cloud Platform region                                   |
| GCP_REGION          | Google Kubernetes Engine (GKE) cluster name                    |
| GCP_ZONE	          | Google Cloud Platform zone                                     |
| GKE_CLUSTER_NAME    | Google Kubernetes Engine (GKE) cluster name                    |
| DOCKER_REPO         | Docker Repository for the CTS application image                |
| DEPLOYMENT_REPLICAS | Number of pods that will host the CTS Backend application      |
| SERVICE_PORT        | Port number for the CTS backend service                        |
| CONTAINER_PORT      | Port number the container is listening on                      |
| REQUESTS_CPU        | Amount of CPU that a pod should request                        |
| REQUESTS_MEMORY     | Amount of Memory that a pod should request                     |
| LIMITS_CPU          | Maximum amount of CPU that a pod can use                       |
| LIMITS_MEMORY       | Maximum amount of Memory that a pod can use                    |
| SCALE_CPU_PERCENT   | Scale up/down according to the CPU percentage used by the pods |
| SCALE_MIN           | Min number of replicas/pods that should be running at all times|
| SCALE_MAX           | Max number of replicas/pods that should be running at all times|

Make sure to provide the necessary values for these variables when configuring the GitHub Actions pipeline. 

### Secrets

The following secrets should be added to the GitHub repository:

| Secret          |  Description                                                       |
|:----------------|:-------------------------------------------------------------------|
| DOCKER_USERNAME | Docker Hub username                                                |
| DOCKER_PASSWORD | Docker Hub password                                                |
| GCP_SA_KEY      | Service account key for Google Cloud Platform authentication (JSON)|

The Service Account that is used for authentication should have the Kubernetes Engine Developer Role grant, you can easily complete this with the following command:

```sh
gcloud projects add-iam-policy-binding <project-id> --member="serviceAccount:<service-account-email>" --role="roles/container.developer"
```

<b>Important: </b>You should change and insert your ```<project-id>``` and ```<service-account-email>``` in the right places that are specified in the command.

Make sure to provide the necessary values for these secrets when configuring the GitHub Actions pipeline. 

## Contact
For any questions or inquiries, please contact: [Daniel Ilievski](https://www.linkedin.com/in/danielilievski/)