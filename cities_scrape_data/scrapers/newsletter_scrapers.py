import re
import urllib3
import xml.etree.ElementTree as ET


from bs4 import BeautifulSoup

from .classifying.date_formatting import *
from ..util.requests_types import *
from ..util.cities_objects import article_object


urllib3.disable_warnings()


def rss_parser(response, name='', id=''):
    try:
        root = ET.fromstring(response.content)
    except (ET.ParseError, AttributeError) as e:
        print(f'Error parsing {e}')
        return None

    items = root.find('channel')

    items = items.findall("item")

    articles = [
        article_object(
            title=item.find('title').text,
            url=item.find('link').text,
            datetime=None
        )
        for item in items
    ]
    if articles:
        return articles


def apple_parser(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')

    script = soup.find('script', type='application/ld+json')
    if not script:
        return None

    json_text = script.string
    data = json.loads(json_text)

    if 'workExample' not in data:
        return None

    episodes = data['workExample']

    articles = [
        article_object(
            title=episode.get('name'),
            url=episode.get('url'),
            datetime=None
        )
        for episode in episodes
    ]

    if articles:
        return articles


def allthingsurban(response, name='', id=''):
    website = 'https://www.allthingsurban.net{}'

    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('div', {'class': 'blog-item'})

    articles = [
        article_object(
            title=article.find('h3', {"class", "blog-item-title"}).text,
            url=website.format(article.find('a')['href']),
            datetime=None
        )
        for article in articles
        if article
        and article.find('a') and article.find('h4', {'class': 'blog-item-subtitle'})
    ]
    if articles:
        return articles


def govtech(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = soup.find_all('div', {'class': "PromoB-content"})

    articles = [
        article_object(
            title=article.find('div', {'class', 'Promo-title'}).text,
            url=article.find(
                'div', {'class', 'Promo-title'}).find('a').get('href'),
            datetime=None
        )
        for article in articles
    ]
    if articles:
        return articles


def streetsblog(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article')

    articles = [
        article_object(
            title=article.find('h2', {'class': 'entry-title'}).text,
            url=article.find('a')['href'],
            datetime=None
        )
        for article in articles
    ]
    if articles:
        return articles


def transitcenter(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = soup.find_all('div', {'class': 'container wide is-widescreen'})

    articles = [
        article_object(
            title=article.find(
                'a', {'class', 'd-block sans-medium py-4 has-text-black is-size-4'}).text,
            url=article.find('a').get('href'),
            datetime=None
        )
        for article in articles
        if article.find('a', {'class', 'd-block sans-medium py-4 has-text-black is-size-4'})
    ]
    if articles:
        return articles


def spur(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('div', {'class', 'content'})[2:]

    articles = [
        article_object(
            title=article.find('h2').text,
            url=article.find('a').get('href'),
            datetime=None
        )
        for article in articles
        if article.find('time')
        and article.find('a')
        and article.find('h2')
    ]
    if articles:
        return articles


def parking_mobility(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('div', {'class', 'blog-post-info'})

    articles = [
        article_object(
            title=article.find('h2').text,
            url=article.find('a')['href'],
            datetime=None
        )
        for article in articles
    ]
    if articles:
        return articles


def axios(response, name='', id=''):

    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('amp-layout')

    articles = [
        article_object(
            title=article.find('h3').text,
            url=article.find('h3').find('a').get('href'),
            datetime=None
        )
        for article in articles
        if article
        and article.find('h3')
    ]
    if articles:
        return articles


def zag(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article')

    articles = [
        article_object(
            title=article.find('h2').text,
            url=article.find('a').get('href'),
            datetime=None
        )
        for article in articles[1:]
    ]
    if articles:
        return articles


def transloc(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all(
        'div', {"class", "esg-entry-content eg-blog-posts-content"})

    articles = [
        article_object(
            title=article.find('a').text,
            url=article.find('a').get('href'),
            datetime=None
        )
        for article in articles
    ]
    if articles:
        return articles


def commutifi(response, name='', id=''):
    website = 'https://www.commutifi.com/{}'

    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all(
        'a', {"class", "resource-item ver-2 w-inline-block"})
    links = [
        website.format(article.get('href'))
        for article in articles
    ]
    articles = []

    for link in links:
        try:
            response = get_response(link)
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.find('h1', {'class', "heading-no-bot-margin"}).text
            articles.append(
                article_object(
                    title=title.split(':')[1].strip(),
                    url=link,
                    datetime=None
                )
            )
        except:
            continue
    if articles:
        return articles


def electronomous(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all(
        'h1', {'class', "elementor-heading-title elementor-size-default"})

    articles = [
        article_object(
            title=article.find('a').text,
            url=article.find('a').get('href'),
            datetime=None
        )
        for article in articles
        if article
        and article.find('a').text
    ]
    if articles:
        return articles


def rpa_parser(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.findAll('li', class_=re.compile(
        r'(l-card-grid__card l-card-grid__card--featured js-append-latest'
        r'|l-card-grid__card js-append-latest)'
        r'|l-card-grid__card l-card-grid__card--featured')
    )

    articles = [
        article_object(
            title=article.find('p',
                               class_=re.compile(
                                   r'(featured-heading-set__heading|media-blurb__subtitle)'
                               )).text,
            url=article.find('a', {'class': "card-link"}).get('href'),
            datetime=None
        )
        for article in articles
        if article
        and article.find('p', {'class', 'tag__text'}).text
    ]
    if articles:
        return articles


def curbed_scraper(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('li', {'class', 'article'})

    articles = [
        article_object(
            title=article.find('span', {'class', 'headline'}).text,
            url=article.find('a', {"class", "link-text"}).get('href'),
            datetime=None
        )
        for article in articles
        if article
        and article.find('span', {'class', 'headline'}).text
    ]
    if articles:
        return articles


def chartercitiesinstitute_podcast_parser(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article')

    articles = [
        article_object(
            title=article.find('h3').text,
            url=article.find('a').get('href'),
            datetime=None
        )
        for article in articles
        if article
        and article.find('span', {'class', 'elementor-post-date'}).text
    ]
    if articles:
        return articles


def chartercitiesinstitute_blog_parser(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article')

    articles = [
        article_object(
            title=article.find('h3').text,
            url=article.find('a').get('href'),
            datetime=None
        )
        for article in articles
        if article
        and article.find('span', {'class', 'elementor-post-date'}).text
    ]
    if articles:
        return articles


def eurocities_parser(response, name='', id=''):
    REGEX = re.compile(
        r'(other-story-list|other-story-list mb-60 lastestlist)')

    soup = BeautifulSoup(response.content, 'html.parser')
    articles_list = soup.find_all(re.compile('ul'), {'class', REGEX})

    if not articles_list:
        return None

    articles = [
        article
        for articles in articles_list
        for article in articles.find_all('li')
    ]

    articles = [
        article_object(
            title=article.find('h2').text,
            url=article.find('a').get('href'),
            datetime=None
        )
        for article in articles
        if article
        and article.find('span', {'class', 'date'})
        and article.find('h2')
    ]
    if articles:
        return articles


def activecities_parser(response, name='', id=''):
    website = 'https://www.interregnorthsea.eu{}'

    soup = BeautifulSoup(response.content, 'html.parser')

    articles = soup.find_all('article', attrs={'role': 'article'})

    articles = [
        article_object(
            title=article.find('h3').text,
            url=website.format(article.find(
                'a', {'class', "c-card c-card--with-ribbon"}).get('href')),
            datetime=None
        )
        for article in articles
        if article
        and article.find('h3').text
    ]
    if articles:
        return articles


def gvshp_parser(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = soup.find_all('article')

    articles = [
        article_object(
            title=article.find('h2').text,
            url=article.find('a')['href'],
            datetime=None
        )
        for article in articles
        if article
        and article.find('a')['href']
    ]
    if articles:
        return articles


def itdpTransportMatters_parser(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = soup.find_all('div', {'class', 'post-detail'})

    articles = [
        article_object(
            title=article.find('a').text,
            url=article.find('a').get('href'),
            datetime=None
        )
        for article in articles
        if article
        and article.find('a')['href']
        and article.find('p', {'class', 'post-date'})
    ]
    if articles:
        return articles


def futuremobility_parser(response, name='', id=''):
    website = 'https://futuremobility.lindholmen.se{}'

    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('div', {"class", "alpha-card__content"})

    articles = [
        article_object(
            title=article.find('h3').text,
            url=website.format(article.find('a').get('href')),
            datetime=None
        )
        for article in articles
        if article
        and article.find('div', {"class", "card-with-meta__meta"})
        and article.find('h3')
    ]
    if articles:
        return articles


def urbanomnibus_parser(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = soup.find_all('article')

    articles = [
        article_object(
            title=article.find('h3').text,
            url=article.find('h3').find('a').get('href'),
            datetime=None
        )
        for article in articles
        if article
        and article.find('h3').text
        and article.find_all('span', {'class', "meta"})
    ]
    if articles:
        return articles


def enotransportation_parser(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = soup.find_all('article')

    articles = [
        article_object(
            title=article.find('a').get('title'),
            url=article.find('a').get('href'),
            datetime=None
        )
        for article in articles
        if article
        and article.find('div', {'class', 'etw-article-meta'})
        and article.find('a')
    ]
    if articles:
        return articles


def nusurbananalytics_parser(response, name='', id=''):
    website = 'https://ual.sg{}'
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = soup.find_all(
        'div', {'class', 'media stream-item view-compact'})

    articles = [
        article_object(
            title=article.find('a').text,
            url=website.format(article.find('a').get('href')),
            datetime=None
        )
        for article in articles
        if article
        and article.find('a')
        and article.find('span', {'class', 'article-date'})
    ]
    if articles:
        return articles


def journal_buildingscities_parser(response, name='', id=''):
    website = 'https://journal-buildingscities.org{}'
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = soup.find_all('div', {'class', "fPSBzf gfYZhR"})

    articles = [
        article_object(
            title=article.find('div', {'class', 'jaxCjk'}).text,
            url=website.format(article.find(
                'div', {'class', 'jaxCjk'}).find('a')['href']),
            datetime=None
        )
        for article in articles
        if article
        and article.find('time')
        and article.find('div', {'class', 'jaxCjk'})
    ]
    if articles:
        return articles
