# - The application will send a request to [catninja api](https://catfact.ninja/fact)
# - The application will run as a web server using Flask - will server on http://localhost:8080
# - The application will get a request to `GET /` and return the cat random fact from the `catninja api` by using the `requests` python package to send a request to the `catninja api`
from flask import Flask
import requests
import os

app = Flask(__name__)


def mock_response():
    mocked_response = {
        "fact": "The first true cats came into existence about 12 million years ago and were the Proailurus.",
        "length": 91
    }
    return mocked_response['fact']


def fetch_cat_fact_from_api():
    response = requests.get('https://catfact.ninja/fact')
    return response.json()['fact']

@app.route('/')
def get_cat_fact():
    if os.getenv('MOCK_RESPONSE'):
        return mock_response()
    else:
        return fetch_cat_fact_from_api()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
