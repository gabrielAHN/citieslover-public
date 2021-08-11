import requests


def get_response_header(website, header):
    response = requests.get(website, headers=header)
    return response.content


def get_response(website):
    response = requests.get(website)
    return response

