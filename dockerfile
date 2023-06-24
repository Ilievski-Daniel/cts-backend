FROM python:3.9-alpine

# Create a non-root user
RUN adduser --disabled-password --gecos "" appuser

# Set the working directory and adjust permissions
WORKDIR /app

# Copy the requirements file and install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY main.py .

# Adjust ownership and permissions
RUN chown -R appuser:appuser /app
RUN chmod 755 main.py

# Switch to the non-root user
USER appuser

# Set the default port as an environment variable
ENV PORT=8080

# Expose the port on which the application will run
EXPOSE $PORT

# Set the command to run the application
CMD ["python", "main.py"]