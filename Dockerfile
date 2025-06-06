# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code into the container
COPY . .

# Expose the port the app will run on
EXPOSE 5000

# Define the command to run your app using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]