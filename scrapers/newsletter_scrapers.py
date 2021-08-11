import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup

from scrapers.clean_strings import *
from scrapers.website_requests import *


class article_object:
    def __init__(self, title, url, datetime):
        self.title = clean_string(title).title()
        self.url = url
        self.datetime = get_datetime(datetime)


def rss_parser(url):
    try:
        response = get_response(url)
        root = BeautifulSoup(response.content, "xml")
    except ET.ParseError as err:
        return []
    items = root.findAll("item")
    if not items:
        return []
    articles = [
        article_object(
            title=item.find('title').text,
            url=item.find('link').text,
            datetime=item.find('pubDate').text,
        )
        for item in items
        if item.find('title')
        and item.find('link')
    ]
    if articles:
        return articles


def apple_parser(url):
    response = get_response(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('li', {'class', 'tracks__track tracks__track--podcast'})
    if not articles:
        return []
    articles = [
        article_object(
            title=article.find('a').text,
            url=article.find('a').get('href'),
            datetime=article.find('time').text
        )
        for article in articles
    ]
    if articles:
        return articles


def allthingsurban(url):
    website = 'https://www.allthingsurban.net{}'

    response = get_response(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('div', {'class': 'blog-item'})
    if not articles:
        return []
    articles = [
        article_object(
            title=article.find('h3', {"class", "blog-item-title"}).text,
            url=website.format(article.find('a')['href']),
            datetime=article.find('h4', {'class',"blog-item-subtitle"}).text,
        )
        for article in articles
        if article
        and article.find('a') and article.find('h4', {'class': 'blog-item-subtitle'})
    ]
    if articles:
        return articles


def govtech(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3)'
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 '
        'Safari/537.36'
    }
    content = get_response_header(url, header)
    soup = BeautifulSoup(content, 'html.parser')
    articles = soup.find_all('div', {'class': "ListA-items-item"})
    if not articles:
        return []
    articles = [
        article_object(
            title=article.find('div', {'class', 'Promo-title'}).text,
            url=article.find('div', {'class', 'Promo-title'}).find('a').get('href'),
            datetime=article.find('div', {'class', 'Promo-date'}).text
        )
        for article in articles
    ]
    if articles:
        return articles


def streetsblog(url):
    response = get_response(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article')
    if not articles:
        return []
    
    articles = [
        article_object(
            title=article.find('h2', {'class': 'entry-title'}).text,
            url=article.find('a')['href'],
            datetime=article.find('time').text
        )
        for article in articles
    ]
    if articles:
        return articles


def transitcenter(website):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3)'
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 '
        'Safari/537.36'
    }
    content = get_response_header(website, header)
    soup = BeautifulSoup(content, 'html.parser')
    articles = soup.find_all('div', {'class': 'container wide is-widescreen'})
    if not articles:
        return []
    articles = [
        article_object(
            title=article.find('a', {'class', 'd-block sans-medium py-4 has-text-black is-size-4'}).text,
            url=article.find('a').get('href'),
            datetime=article.find('div', {'class', 'has-color-primary sans-medium is-size-6 py-2'}).text
        )
        for article in articles
        if article.find('a', {'class', 'd-block sans-medium py-4 has-text-black is-size-4'})
    ]
    if articles:
        return articles


def spur(url):
    response = get_response(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('div', {'class', 'content'})[2:]
    if not articles:
        return []
    articles = [
        article_object(
            title=article.find('h2').text,
            url=article.find('a').get('href'),
            datetime=article.find('time').text
        )
        for article in articles
    ]
    if articles:
        return articles


def parking_mobility(url):
    response = get_response(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('div', {'class', 'blog-post-info'})
    if not articles:
        return []
    articles = [
        article_object(
            title=article.find('h2').text,
            url=article.find('a')['href'],
            datetime=article.find('p').previous_sibling
        )
        for article in articles
    ]
    if articles:
        return articles


def axios(url):
    response = get_response(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('amp-layout')
    if not articles:
        return []
    articles = [
        article_object(
            title= article.find('h3').text,
            url= article.find('h3').find('a').get('href'),
            datetime=article.find(
                'span', {'data-testid', "time-rubric"}
            ).text.split(' - ')[0]
        )
        for article in articles
        if article
        and article.find('h3')
    ]
    if articles:
        return articles


def umc(url):
    response = get_response(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article')
    if not articles:
        return []
    articles = [
        article_object(
            title=article.find('h2').text,
            url=article.find('a').get('href'),
            datetime=article.find('span', {'class', "published"}).text
        )
        for article in articles
    ]
    if articles:
        return articles

