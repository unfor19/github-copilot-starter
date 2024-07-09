from flask import Flask
import requests
import os

app = Flask(__name__)


def mock_response():
    """
    Mocked response for the cat fact
    :return: str: The first true cats came into existence about 12 million years ago and were the Proailurus.
    """
    mocked_response = {
        "fact": "The first true cats came into existence about 12 million years ago and were the Proailurus.",
        "length": 91
    }
    return mocked_response['fact']


def fetch_cat_fact_from_api():
    """
    Fetches a random cat fact from the catninja api
    :return: str: A random cat fact
    """


def fetch_cat_fact_from_api():
    """
    Fetches a random cat fact from the catninja api
    :return: str: A random cat fact or an error message
    """
    try:
        response = requests.get('https://catfact.ninja/fact')
        # Raises an HTTPError if the response status code is 4XX/5XX
        response.raise_for_status()
        return response.json().get('fact', 'No fact found')
    except requests.exceptions.HTTPError as http_err:
        return f'HTTP error occurred: {http_err}'
    except requests.exceptions.ConnectionError as conn_err:
        return f'Connection error occurred: {conn_err}'
    except requests.exceptions.Timeout as timeout_err:
        return f'Timeout error occurred: {timeout_err}'
    except requests.exceptions.RequestException as req_err:
        return f'Error fetching cat fact: {req_err}'
    except Exception as e:
        return f'An error occurred: {e}'


@app.route('/')
def get_cat_fact():
    response = None

    # Check if MOCK_RESPONSE is set to true, if so, return a mocked response
    if os.environ.get('MOCK_RESPONSE', 'false').lower() == 'true':
        response = mock_response()
    else:
        response = fetch_cat_fact_from_api()

    # Enrich response with more details
    response = f'Cat fact: {response}'

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
