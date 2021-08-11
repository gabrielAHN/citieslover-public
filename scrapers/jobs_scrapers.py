import re

from bs4 import BeautifulSoup

from scrapers.clean_strings import *
from scrapers.website_requests import *



class job_object:
    def __init__(self, title, company, location , url, datetime):
        self.title = clean_string(title).title()
        self.company = clean_string(company)
        self.location = clean_string(location.title())
        self.url = url.replace('www.', 'https://')
        self.datetime = get_datetime(clean_string(datetime))


def planetizen_jobs(url):
    response = get_response(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find('div', {'class', 'view-content global-search'})
    if not jobs:
        return []
    jobs = [
        job_object(
            title=job.find('a').text,
            company=job.find('p', {'class', 'author__label'}).text,
            location=job.get('data-location'),
            url='www.planetizen.com{}'.format(job.find('a').get('href')),
            datetime=job.find('span').text
        )
        for job in jobs.find_all('div')
        if job.find('p', {'class', 'author__label'})
        and job.find('span').text
        and 'www.planetizen.com{}'.format(job.find('a').get('href'))
    ]
    if jobs:
        return jobs


def allthingsurban_jobs(url):
    website = 'https://www.allthingsurban.net{}'
    REGEX = re.compile(r'list\-item( list\-item\-overdue)?')
    REGEX_2 = re.compile(r'list-item-(title|subtitle)')

    response = get_response(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find('div', {'class', 'list'})
    if not jobs:
        return []
    jobs = jobs.find_all('div', {'class': 'list-item'})
    jobs = [
        job_object(
            title=job.find(re.compile('h(3|4)'), {'class', REGEX_2}).text,
            company=job.find('h4', {'class': 'list-item-subtitle'}).text,
            location=job.find('div',{'class','list-item-value'}).text,
            url=website.format(job.find('a')['href']),
            datetime=job.find('div', {'class',"list-item-date"}).text,
        )
        for job in jobs
        if job
        and job.find('a') and job.find('h4', {'class': 'list-item-subtitle'})
    ]
    if jobs:
        return jobs


def apany_jobs(url):
    response = get_response(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find_all('tr')
    if not jobs:
        return []
    jobs = [
        job_object(
            title=job.find('h5').text,
            company=job.find_all('td')[1].text,
            location='New York',
            url=job.find('a').get('href'),
            datetime=job.find_all('td')[2].text,
        )
        for job in jobs
        if job.find('h5')
    ]
    if jobs:
        return jobs


def nextcity_jobs(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3)'
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 '
        'Safari/537.36'
    }
    content = get_response_header(url, header)
    soup = BeautifulSoup(content, 'html.parser')
    jobs = soup.find_all('div', {'class', 'panel card panel-default'})
    if not jobs:
        return []
    jobs = [
        job_object(
            title=job.find('a').text,
            company=[
                company
                for company in job.find('div', {'class', 'job-company card-subtitle text-muted'}).text.split('\n')
                if company
                and ", " != company
            ][0],
            location=[
                company
                for company in job.find('div', {'class', 'job-company card-subtitle text-muted'}).text.split('\n')
                if company
                and ", " != company
            ][3],
            url=job.find('a').get('href'),
            datetime=job.find('time').text
        )
        for job in jobs
    ]
    if jobs:
        return jobs


def govlove_jobs(url):
    response = get_response(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find_all('article')
    if not jobs:
        return []
    jobs = [
        job_object(
            title=job.find('a', {'class', "link"}).text,
            company=job.find(
                'span', {'class', 'listing-item__info--item listing-item__info--item-company'}
            ).text,
            location=job.find(
                'span', {'class', 'listing-item__info--item listing-item__info--item-location'}
            ).text,
            url=job.find('a', {'class', "link"}).get('href'),
            datetime=job.find('div', {'class', "listing-item__date"}).text,
        )
        for job in jobs
        if job.find('a', {'class', "link"})
    ]
    if jobs:
        return jobs
