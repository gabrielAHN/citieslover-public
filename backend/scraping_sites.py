import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup


def get_response(website):
    response = requests.get(website)
    return response.content


def get_response_header(website, header):
    response = requests.get(website, headers=header)
    return response.content


def moncole(website):
    content = get_response(website)
    root = ET.fromstring(content)
    items = root.findall('*/item')
    article = items[1]
    title = article.find('title').text
    description = article.find('description').text
    link = article.find('link').text
    return title, description, link


def cityfix(website):
    content = get_response(website)
    soup = BeautifulSoup(content, 'lxml')
    link = soup.find_all('comments')[0].text
    title = soup.find_all('title')[1].text
    description = soup.find_all('description')[1].text
    return title, description, link


def planetizen(website):
    content = get_response(website)
    soup = BeautifulSoup(content, 'html.parser')
    article = soup.find_all('item')[0]
    title = article.find('title').text
    description = article.find('description').text
    link = article.find('guid').text
    return title, description, link


def govtech(website):
    content = get_response(website)
    soup = BeautifulSoup(content, 'html.parser')
    articles = soup.find_all('div', {'class': "sub-feature-article"})
    title = articles[0].find('a').text
    link = articles[0].find('a')['href']
    content = get_response(link)
    soup = BeautifulSoup(content, 'html.parser')
    description = soup.find('p').text
    return title, description, link


def streetsblog(website):
    content = get_response(website)
    soup = BeautifulSoup(content, 'html.parser')
    article = soup.find_all('article')[0]
    title = article.find('h2', {'class': 'entry-title'}).text
    link = article.find('a')['href']
    description = article.find('div', {'class': 'entry-excerpt'}).text
    return title, description, link


def smartcities(website):
    content = get_response(website)
    soup = BeautifulSoup(content, 'html.parser')
    articles = soup.find_all('item')
    title = articles[0].find('title').text
    link = articles[0].find('guid').text
    description = articles[0].find('description').text
    return title, description, link


def datasmart(website):
    content = get_response(website)
    soup = BeautifulSoup(content, 'html.parser')
    articles = soup.find_all('item')
    title = articles[0].find('title').text
    link = articles[0].find('guid').text
    description = articles[0].find('description').text
    return title, description, link


def strongtowns(website):
    content = get_response(website)
    soup = BeautifulSoup(content, 'html.parser')
    articles = soup.find_all('item')
    title = articles[0].find('title').text
    link = articles[0].find('comments').text
    description = articles[0].find('description').text
    return title, description, link


def transitcenter(website):
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3)'
     'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
    content = get_response_header(website, header)
    soup = BeautifulSoup(content, 'html.parser')
    articles = soup.find_all('div', {'class': 'container wide is-widescreen'})
    link = articles[0].find('a')['href']
    description = articles[0].find('p').text
    content = get_response_header(link, header)
    soup = BeautifulSoup(content, 'html.parser')
    title = soup.find('div', {'class':'h2 sans-medium'}).text
    return title, description, link


def masstransit(website):
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3)'
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
    content = get_response_header(website, header)
    soup = BeautifulSoup(content, 'html.parser')
    articles = soup.find('div', {'class', 'col-lg-4 mb-block'})
    articles = articles.find_all('div', {'class', "node__contents node__contents--body"})
    title = articles[0].find('h5').text
    link = website + articles[0].find('a')['href']
    content = get_response_header(link, header)
    soup = BeautifulSoup(content, 'html.parser')
    description = soup.find('p', {'class', "page-wrapper__deck"}).text
    return title, description, link


def itetalk(website):
    content = get_response(website)
    root = ET.fromstring(content)
    items = root.findall('*/item')
    article = items[0]
    title = article.find('title').text
    description = article.find('description').text
    link = article.find('link').text
    return title, description, link


def metro_mag(website):
    content = get_response(website)
    root = ET.fromstring(content)
    items = root.findall('*/item')
    article = items[0]
    title = article.find('title').text
    description = article.find('description').text
    link = article.find('link').text
    return title, description, link
