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
        root = BeautifulSoup(content, "xml")
    except ET.ParseError as err:
        return []
    items = root.findAll("item")
    if not items:
        return []
    elif len(items) > 5:
        items = items[:5]
    articles = [
        article_object(
            title= item.find('title').text,
            url= item.find('link').text,
        )
        for item in items
        if item.find('title')
        and item.find('link')
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
        if item.find('title')
        and item.find('link')
    ]
    if articles:
        return articles


def int_transport(website):
    content = get_response(website)
    soup = BeautifulSoup(content, 'html.parser')
    items = soup.find_all('article')
    if len(items) > 5:
        items = items[:5]
    articles = [
        article_object(
            title= item.find('h3').text,
            url= item.find('a')['href']
        )
        for item in items
        if item.find('h3')
        and item.find('a')
    ]
    if articles:
        return articles


def spur(website):
    content = get_response(website)
    soup = BeautifulSoup(content, 'html.parser')
    items = soup.find_all('article')[1:]
    if len(items) > 5:
        items = items[:5]
    articles = [
        article_object(
            title= item.find('h2').text,
            url= item.find('a')['href']
        )
        for item in items
        if item.find('h2')
        and item.find('a')
    ]
    if articles:
        return articles


def parking_mobility(website):
    content = get_response(website)
    soup = BeautifulSoup(content, 'html.parser')
    items = soup.find_all('div', {'class', 'blog-post-info'})
    if len(items) > 5:
        items = items[:5]
    articles = [
        article_object(
            title= item.find('h2').text,
            url= item.find('a')['href']
        )
        for item in items
        if item.find('h2')
        and item.find('a')
    ]
    if articles:
        return articles


def axios(website):
    content = get_response(website)
    soup = BeautifulSoup(content, 'html.parser')
    items = soup.find_all('a', {'class', 'title-link gtm-content-click'})
    if len(items) > 5:
        items = items[:5]
    articles = [
        article_object(
            title= item.text,
            url= item.get('href')
        )
        for item in items
        if item
        and item.get('href')
    ]
    if articles:
        return articles


def umc(website):
    url = 'https://urbanmobilitycompany.com'
    content = get_response(website)
    soup = BeautifulSoup(content, 'html.parser')
    items = soup.find('ul', {'class', "grid svelte-1dt5b9d"})
    if not items:
        return None
    items = items.find_all('li')
    if len(items) > 5:
        items = items[:5]
    articles = [
        article_object(
            title= item.find('h2').text,
            url= '{}{}'.format(url, item.find('a')['href'])
        )
        for item in items
        if item.find('h2')
        and item.find('a')['href']
    ]
    if articles:
        return articles
