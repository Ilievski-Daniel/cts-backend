# CTS Backend Application

The CTS Backend Application is a simple connectivity test server designed to support the mobile multiplayer game "Fun7" by providing latency measurements to determine the best backend server for game connectivity.

## Prerequisites

- Docker: [Installation Guide](https://docs.docker.com/get-docker/)
- Python 3.9 or higher: [Installation Guide](https://www.python.org/downloads/)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Ilievski-Daniel/cts-backend.git
   cd cts-backend
   ```

2. Build the Docker image:

    ```
    docker build -t cts-backend .
    ```

3. Access the CTS API endpoint:

    ```
    curl http://localhost:8080/ping
    ```

<b>The response should be a JSON object with a "message" field.</b>

## Configuration

Port: By default, the application runs on port 8080.

If you wish to change the port, you can modify the main.py file and the Dockerfile. In the main.py file, locate the line app.run(host='0.0.0.0', port=8080) and change the port parameter to your desired port number. Similarly, in the Dockerfile, locate the line EXPOSE 8080 and update the exposed port number accordingly.

Please ensure that you make consistent changes in both files to ensure proper functioning of the application.

## Deployment
To deploy the CTS Backend Application to Google Cloud or any other cloud platform, follow the standard deployment procedures for deploying Docker containers.

## Contact
For any questions or inquiries, please contact: [Daniel Ilievski](https://www.linkedin.com/in/danielilievski/)