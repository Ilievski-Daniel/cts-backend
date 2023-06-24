FROM python:3.9-alpine

# Create a non-root user
RUN adduser --disabled-password --gecos "" appuser

# Set the working directory and adjust permissions
WORKDIR /app
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

# Copy the requirements file and install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the necessary files and directories
COPY main.py .

# Set the default port as an environment variable
ENV PORT=8080

# Expose the port on which the application will run
EXPOSE $PORT

# Set the command to run the application
CMD ["python", "main.py"]