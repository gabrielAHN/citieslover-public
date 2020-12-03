import requests
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup

from backend.clean_strings import clean_string


class article_object:
    def __init__(self, title, url):
        self.title = clean_string(title).title()
        self.url = url


def get_response(website):
    response = requests.get(website)
    return response.content


def get_response_header(website, header):
    response = requests.get(website, headers=header)
    return response.content


def rss_parser(website):
    try:
        content = get_response(website)
        root = ET.fromstring(content)
    except ET.ParseError as err:
        return []
    items = root.findall('*/item')
    if len(items) > 5:
        items = items[:5]
    articles = [
        article_object(
            title= item.find('title').text,
            url= item.find('link').text,
        )
        for item in items
        if item.find('title').text
        and item.find('link').text
    ]
    if articles:
        return articles


def govtech(website):
    content = get_response(website)
    soup = BeautifulSoup(content, 'html.parser')
    items = soup.find_all('div', {'class': "sub-feature-article"})
    if len(items) > 5:
        items = items[:5]
    articles = [
        article_object(
            title= item.find('a').text,
            url= item.find('a')['href']
        )
        for item in items
    ]
    if articles:
        return articles


def streetsblog(website):
    content = get_response(website)
    soup = BeautifulSoup(content, 'html.parser')
    items = soup.find_all('article')
    if len(items) > 5:
        items = items[:5]
    articles = [
        article_object(
            title= item.find('h2', {'class': 'entry-title'}).text,
            url= item.find('a')['href']
        )
        for item in items
    ]
    if articles:
        return articles


def transitcenter(website):
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3)'
     'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
    content = get_response_header(website, header)
    soup = BeautifulSoup(content, 'html.parser')
    items = soup.find_all('div', {'class': 'container wide is-widescreen'})
    if len(items) > 5:
        items = items[:5]
    articles = [
        article_object(
            title= section.text,
            url= section['href']
        )
        for item in items
        for section in item.find_all(
            'a', {'class', 'd-block sans-medium py-4 has-text-black is-size-4'}
        )
    ]
    if articles:
        return articles


def the_city(website):
    content = get_response(website)
    soup = BeautifulSoup(content, 'html.parser')
    items = soup.find_all('entry')
    if len(items) > 5:
        items = items[:5]
    articles = [
        article_object(
            title= item.find('title').text,
            url= item.find('link')['href']
        )
        for item in items
        if item.find('title').text
        and item.find('link')
    ]
    if articles:
        return articles
