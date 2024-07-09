# github-copilot-starter

This is a starter project for GitHub Copilot.

## Goals

- The application will send a request to [catninja api](https://catfact.ninja/fact)
- The application will run as a web server using Flask - will server on http://localhost:8080
- The application will get a request to `GET /` and return the cat random fact from the `catninja api` by using the `requests` python package to send a request to the `catninja api`
- We are going to use venv for Virtual Environment `.VENV` dir
- The app requires Python to run
- The app will be wrapped with Docker (Dockerfile)

## Requirements

- Python 3.6+
- Docker


## Setup

Initial setup to run this application:

1. Clone this repository
1. Create a virtual environment
   ```bash
   python -m venv .VENV
   ```
2. Activate the virtual environment
   ```bash
   source .VENV/bin/activate
   ```
3. Install the dependencies
   ```bash
   pip install -r requirements.txt
   ```

## Docker

1. Build the docker image
   ```bash
    docker build -t copilot-starter .
    ```
1. Run the docker container
   ```bash
    docker run -p 8080:8080 copilot-starter
    ```
1. Run container with env var `MOCK_RESPONSE`
   ```bash
    docker run -p 8080:8080 -e MOCK_RESPONSE=True copilot-starter
    ```