import json
import requests
from .cities_objects import request_object

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 '
                  'Safari/537.36'
}


def get_response_header(website):
    response = requests.get(website, headers=header,
                            verify=False, timeout=20)
    return response


def get_response(website):
    response = requests.get(website, verify=False, timeout=20)
    return response


def get_post_response(website, header, payload):
    payload = json.dumps(payload)
    response = requests.post(
        website, headers=header, data=payload, timeout=20)
    return response

def get_multi_responses(website, end_points):
    responses = [
        requests.get(website+url, verify=False, timeout=20)
        for url in end_points
    ]
    return responses

def website_requests(website, scrapers):
    response_type = scrapers['requests'].get('request_type')

    try:
        if response_type.__name__ == 'get_post_response':
            response = response_type(
                website=scrapers['website'],
                header=scrapers['requests']['header'],
                payload=scrapers['requests']['payload']
            )
        elif response_type.__name__ == 'get_multi_responses':
            response = response_type(
                website=scrapers['website'],
                end_points=scrapers['requests']['end_points']
            )
        else:
            response = response_type(scrapers['website'])

        return request_object(
            id=website['id'],
            name=website['name'],
            url=scrapers['website'],
            type=scrapers['type'],
            scraper=scrapers['scrape_function'],
            response=response,
            error=None,
            content=response,
        )
    except Exception as e:
        return request_object(
            id=website['id'],
            name=website['name'],
            url=scrapers['website'],
            type=scrapers['type'],
            scraper=scrapers['scrape_function'],
            response=None,
            error=str(e),
            content=None,
        )
