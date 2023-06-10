FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Set the default port as an environment variable
ENV PORT=8080

# Expose the port on which the application will run
EXPOSE $PORT

# Set the command to run the application
CMD ["python", "main.py"]