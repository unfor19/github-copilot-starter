

# - The application will send a request to [catninja api](https://catfact.ninja/fact)
# - The application will run as a web server using Flask - will server on http://localhost:8080
# - The application will get a request to `GET /` and return the cat random fact from the `catninja api` by using the `requests` python package to send a request to the `catninja api`
# - We are going to use venv for Virtual Environment `.VENV` dir
# - The app requires Python to run
# - The app will be wrapped with Docker (Dockerfile)

# This Dockerfile serves the app, yalla go

FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Specify the port number the container should expose
# bullshit - for docs only
EXPOSE 8080 

# Run the application
CMD ["python", "app.py"]