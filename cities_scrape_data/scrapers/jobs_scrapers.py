import re

from bs4 import BeautifulSoup

from .classifying.date_formatting import *
from ..util.requests_types import *
from ..util.cities_objects import job_object
from ..scrapers.classifying.job_typer import *
from ..scrapers.classifying.location_standardizer import *


def lever_jobs(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')

    jobs = soup.find_all('div', {'class', 'posting'})

    jobs = [
        job_object(
            title=job.find('h5').text,
            company=name,
            location=[i.text for i in job.find(
                'div', {'class', 'posting-categories'}).find_all('span')],
            url=job.find('a').get('href'),
            datetime=None,
            job_type=job_typer(job.find('h5').text, name)
        )
        for job in jobs
        if job

    ]
    if jobs:
        return jobs


def greenhouse_jobs(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find_all('tr', {'class': 'job-post'})

    jobs = [
        job_object(
            title=job.find_all('p')[0].text,
            company=name,
            location=[job.find_all('p')[1].text],
            url=job.find('a').get('href'),
            datetime=None,
            job_type=job_typer(
                job.find_all('p')[0].text
            )
        )
        for job in jobs
        if job_typer(
            job.find_all('p')[0].text
        )
        and job
    ]
    if jobs:
        return jobs


def greenhouse_older_jobs(response, name='', id=''):
    website = 'https://boards.greenhouse.io{}'
    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find_all('div', {'class': 'opening'})

    jobs = [
        job_object(
            title=job.find('a').text,
            company=name,
            location=[job.find('span', {'class', 'location'}).text],
            url=website.format(job.find('a').get('href')),
            datetime=None,
            job_type=job_typer(
                job.find('a').text
            )
        )
        for job in jobs
        if job_typer(
            job.find('a').text
        )
        and job
    ]
    if jobs:
        return jobs


def workable_jobs(response, name='', id=''):
    website = "https://apply.workable.com/{}/j/{}/"
    jobs = response.json()

    jobs = [
        job_object(
            title=job.get('title'),
            company=name,
            location=[
                f"{locations['city']}, {locations['country']}"
                for locations in job['locations']
            ] + (['remote'] if job.get('remote') else []),
            url=website.format(id, job.get('shortcode')),
            datetime=None,
            job_type=job_typer(job.get('title'), name)
        )
        for job in jobs.get('results')
    ]
    if jobs:
        return jobs


def planetizen_jobs(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find('div', {'class', 'view-content global-search'})

    jobs = [
        job_object(
            title=job.find('a').text,
            company=job.find('p', {'class', 'author__label'}).text,
            location=[job.get('data-location')],
            url='www.planetizen.com{}'.format(job.find('a').get('href')),
            datetime=None,
            job_type=job_typer(job.find('a').text, job.find(
                'p', {'class', 'author__label'}).text)
        )
        for job in jobs.find_all('div')
        if job.find('p', {'class', 'author__label'})
        and job.find('span').text
        and 'www.planetizen.com{}'.format(job.find('a').get('href'))

    ]
    if jobs:
        return jobs


def allthingsurban_jobs(response, name='', id=''):
    REGEX_2 = re.compile(r'list-item-(title|subtitle)')

    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find('div', {'class', 'list'})

    jobs = jobs.find_all('div', {'class': 'list-item'})
    jobs = [
        job_object(
            title=job.find(re.compile('h(3|4)'), {'class', REGEX_2}).text,
            company=job.find('h4', {'class': 'list-item-subtitle'}).text,
            location=[job.find('div', {'class', 'list-item-value'}).text],
            url='www.allthingsurban.net{}'.format(job.find('a')['href']),
            datetime=None,
            job_type=job_typer(
                job.find(re.compile('h(3|4)'), {'class', REGEX_2}).text,
                job.find('h4', {'class': 'list-item-subtitle'}).text
            )
        )
        for job in jobs
        if job
        and job.find('a') and job.find('h4', {'class': 'list-item-subtitle'})
        and not 'Administrator' in job.find(re.compile('h(3|4)'), {'class', REGEX_2}).text
    ]
    if jobs:
        return jobs


def uber_jobs(response, name='', id=''):
    jobs = response.json()

    jobs = [
        job_object(
            title=job['title'],
            company=name,
            location=[i['region'] for i in job['allLocations'] if i['region']],
            url=f"www.uber.com/global/en/careers/list/{job['id']}/",
            datetime=None,
            job_type=job_typer(job['title'],
                               'Uber', ['transport_enthusiast']
                               )
        )
        for job in jobs['data']['results']
        if jobs.get('data')
        and jobs.get('data').get('results')
    ]
    if jobs:
        return jobs


def govlove_jobs(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find_all('article')

    jobs = [
        job_object(
            title=job.find('a', {'class', "link"}).text,
            company=job.find(
                'span', {
                    'class', 'listing-item__info--item listing-item__info--item-company'}
            ).text,
            location=[job.find(
                'span', {
                    'class', 'listing-item__info--item listing-item__info--item-location'}
            ).text],
            url=job.find('a', {'class', "link"}).get('href'),
            datetime=None,
            job_type=job_typer(job.find('a', {'class', "link"}).text,
                               job.find('a', {'class', "link"}).text, [
                'gov_lovers']
            )
        )
        for job in jobs
        if job.find('a', {'class', "link"})
    ]
    if jobs:
        return jobs


def nyc_planning_jobs(response, name='', id=''):
    website = 'www.nyc.gov'
    jobs = response.json()

    jobs = [
        job_object(
            title=job.get('name'),
            company=name,
            location=['New York City'],
            url=website+job.get('link'),
            datetime=None,
            job_type=job_typer(
                job.get('name'), 'NYC Planning Department', ['gov_lovers'])
        )
        for job in jobs
        if job_typer(job.get('name'), 'NYC Planning Department', ['gov_lovers'])
    ]
    if jobs:
        return jobs


def transitcenter_job(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')

    jobs = soup.find('div', {'class', "content-body"})
    jobs = jobs.find_all('a')

    jobs = [
        job_object(
            title=job.text,
            company=name,
            location=['New York'],
            url=job.get('href'),
            datetime=None,
            job_type=job_typer(job.text, 'Transit Center')
        )
        for job in jobs
        if job_typer(job.text, 'Transit Center')
        and job
    ]
    if jobs:
        return jobs


def mobilitydata_jobs(response, name='', id=''):
    website = 'https://careers.mobilitydata.org{}'

    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find_all('li', {'class': 'position transition'})

    jobs = [
        job_object(
            title=job.find('h2').text,
            company=name,
            location=[
                i.text
                for i in job.find('li', {'class': "location"}).find_all('span')
            ],
            url=website.format(job.find('a').get('href')),
            datetime=None,
            job_type=job_typer(job.find('h2').text, 'Mobility Data', [
                               'transport_enthusiast'])
        )
        for job in jobs
        if job_typer(job.find('h2').text, 'Mobility Data', ['transport_enthusiast'])
        and job
    ]
    if jobs:
        return jobs


def smartgrowamerica_jobs(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find('div', {'class', 'fw-content'})
    jobs = jobs.find_all('h2')

    jobs = [
        job_object(
            title=job.find('a').text.replace('Now hiring: ', ''),
            company=name,
            location=['Washington, DC'],
            url=job.find('a').get('href'),
            datetime=None,
            job_type=job_typer(
                job.find('a').text.replace('Now hiring: ', ''),
                'Smart Growth America'
            )
        )
        for job in jobs
        if job_typer(
            job.find('a').text.replace('Now hiring: ', ''),
            'Smart Growth America'
        )
        and job
    ]
    if jobs:
        return jobs


def optibus_jobs(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find('ul', {'class': 'comeet-positions-list'})

    jobs = jobs.find_all('li')

    jobs = [
        job_object(
            title=job.find('div').text,
            company=name,
            location=[
                job.find('div', {'class': 'location-tag filter-tags'}).text],
            url=f"https:{job.find('a').get('href')}",
            datetime=None,
            job_type=job_typer(
                job.find('div').text,
                name
            )
        )
        for job in jobs
        if job
    ]
    if jobs:
        return jobs


def ito_jobs(response, name='', id=''):
    website = "https://itoworld.bamboohr.com/careers/{}"

    jobs = response.json()

    jobs = [
        job_object(
            title=job['jobOpeningName'],
            company=name,
            location=['Cambridge, Cambridgeshire (Remote)'],
            url=website.format(job['id']),
            datetime=None,
            job_type=job_typer(
                job['jobOpeningName'],
                name,
                ['transport_enthusiast']
            )
        )
        for job in jobs['result']
        if job_typer(
            job['jobOpeningName']
        )
        and job
    ]
    if jobs:
        return jobs


def voi_jobs(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')

    jobs = soup.find('ul', {'class': 'block-grid',
                     'id': 'jobs_list_container'})
    jobs = jobs.find_all('li')

    jobs = [
        job_object(
            title=job.find('span').get('title'),
            company=name,
            location=[
                clean_string(i.text)
                for i in job.find_all('span')[2:]
                if i and '·' not in i
            ],
            url=job.find('a').get('href'),
            datetime=None,
            job_type=job_typer(
                job.find('span').get('title'),
                name,
                ['transport_enthusiast']
            )
        )
        for job in jobs
        if job_typer(
            job.find('span').get('title'),
            name,
            ['transport_enthusiast']
        )
        and job
    ]
    if jobs:
        return jobs


def dbf_jobs(response, name='', id=''):
    website = 'www.digitalbluefoam.com{}'

    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.findAll('div', {'class': 'w-layout-grid grid-6'})



    jobs = [
        job_object(
            title=job.find('h3').text,
            company=name,
            location=[job.find('div', {'class': 'text-block-27'}).text],
            url=website.format(job.find('a').get('href')),
            datetime=None,
            job_type=job_typer(job.find('h3').text, name)
        )
        for job in jobs
        if job_typer(job.find('h3').text, name)
        and job
    ]
    if jobs:
        return jobs


def replica_jobs(response, name='', id=''):
    website = 'https://replicainc.applytojob.com{}'

    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find_all('a', {'class': 'job_title_link'})

    jobs = [
        job_object(
            title=job.text,
            company=name,
            location=['Leawood, KS'],
            url=website.format(job.get('href')),
            datetime=None,
            job_type=job_typer(job.text)
        )
        for job in jobs
        if job_typer(job.text)
        and job
    ]
    if jobs:
        return jobs


def lastminute_jobs(response, name='', id=''):
    website = 'https://corporate.lastminute.com/{}'

    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find_all('div', {'class': 'job-row'})

    jobs = [
        job_object(
            title=job.find('a', {'class', "uk-link-heading"}).text,
            company=name,
            location=[job.find('div', {"class": "job-location"}).text],
            url=website.format(
                job.find('a', {'class', "uk-link-heading"}).get('href')),
            datetime=None,
            job_type=job_typer(
                job.find('a', {'class', "uk-link-heading"}).text)
        )
        for job in jobs
        if job
        and job.find('a', {'class', "uk-link-heading"})
    ]
    if jobs:
        return jobs


def la_metro_jobs(response, name='', id=''):
    website = "https://jobs.metro.net/{}"

    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find(
        'table', {"id": "ctl00_ContentPlaceHolder1_dgvMetroJobPTSC"})


    jobs = jobs.find_all('td', {'align': 'left'})
    jobs = [a.find('a') for a in jobs if a.find('a')]


    jobs = [
        job_object(
            title=job.text,
            company=name,
            location=['Los Angeles, CA'],
            url=website.format(job.get('href')),
            datetime=None,
            job_type=job_typer(job.text)
        )
        for job in jobs
        if job_typer(job.text)
        and 'other' not in job_typer(job.text)
        and job
    ]
    if jobs:
        return jobs


def rpa_jobs(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find_all('div', {'class': 'content-table-row__opening'})



    jobs = [
        job_object(
            title=job.find(
                'p', {'class': 'content-table-row__opening-title'}).text,
            company=name,
            location=[
                job.find('p', {'class': 'content-table-row__opening-location'}).text],
            url=job.find('a').get('href'),
            datetime=None,
            job_type=job_typer(
                job.find(
                    'p', {'class': 'content-table-row__opening-title'}).text
            )
        )
        for job in jobs
        if job
    ]
    if jobs:
        return jobs


def lyft_jobs(response, name='', id=''):
    jobs = response.json()



    jobs = jobs.get('jobs')

    jobs = [
        job_object(
            title=job.get('title'),
            company=name,
            location=([
                location['location']
                for location in job.get('offices')]
                if None not in [
                location['location']
                for location in job.get('offices')]
                else [job.get('location')]),
            url=job['publicUrl'],
            datetime=None,
            job_type=job_typer(
                job.get('title'),
                name,
                ['transport_enthusiast']
            )
        )
        for job in jobs
        if job and job.get('offices')
    ]
    if jobs:
        return jobs


def transit_jobs(response, name='', id=''):
    website = "https://manifesto.transitapp.com{}"

    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find('div', {'class', 'framer-nhflh7'})

    jobs = jobs.find_all('div', {
        'class', 'framer-1yx909s-container',
        "style", "opacity: 1"})



    jobs = [
        job_object(
            title=job.find('h5').text,
            company=name,
            location=[job.find('p').text],
            url=website.format(job.find('a').get('href')[1:]),
            datetime=None,
            job_type=job_typer(job.find('h5').text)
        )
        for job in jobs
        if job

    ]
    if jobs:
        return jobs


def spare_jobs(response, name='', id=''):
    jobs = response.json()



    jobs = jobs.get('data')


    jobs = [
        job_object(
            title=job.get('title'),
            company=name,
            location=([job.get('location').get('name')]),
            url=job['url'],
            datetime=None,
            job_type=job_typer(
                job.get('title'),
                name,
                ['transport_enthusiast']
            )
        )
        for job in jobs
        if job and job.get('title')
    ]
    if jobs:
        return jobs


def mobilityhouse_jobs(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')

    jobs = soup.find(
        'section', {"class", "sc-3fe7f201-0 sc-3226279f-0 btDIwT khtdVs"})


    jobs = jobs.find_all('a', attrs={
        'target': '_blank',
        'rel': 'noopener noreferrer'
    })

    jobs = [
        job_object(
            title=job.find('strong').text,
            company=name,
            location=([job.find('strong').text]),
            url=job.get('href'),
            datetime=None,
            job_type=job_typer(
                job.find('strong').text,
                name,
                ['transport_enthusiast']
            )
        )
        for job in jobs
        if job and job.find('strong')
    ]
    if jobs:
        return jobs


def gvshp_jobs(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')

    jobs = soup.find_all(
        'a', href=re.compile(r'\.pdf$'),
        attrs={'title': "", 'rel': "noopener"})



    jobs = [
        job_object(
            title=job.find('em').text,
            company=name,
            location=(['New York']),
            url=job.get('href'),
            datetime=None,
            job_type=job_typer(
                job.find('em').text,
                name,
                ['city_builders']
            )
        )
        for job in jobs
        if job and job.find('em').text
    ]
    if jobs:
        return jobs


def urbandesignforum_parser(response, name='', id=''):
    REGEX = re.compile(r'were-hiring')

    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find_all('a', href=REGEX)



    jobs = [
        job_object(
            title=job.text,
            company=name,
            location=(['New York']),
            url=job.get('href'),
            datetime=None,
            job_type=job_typer(
                job.text,
                name
            )
        )
        for job in jobs
        if job and job.text
    ]
    if jobs:
        return jobs


def zencity_jobs(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find_all('li', {'class': 'comeet_position_cont'})



    jobs = [
        job_object(
            title=job.find('div', {'class': "comeet-position-name"}).text,
            company=name,
            location=([job.get('data-location')]),
            url=f"https:{job.find('a').get('href')}",
            datetime=None,
            job_type=job_typer(
                job.find('div', {'class': "comeet-position-name"}).text,
                name
            )
        )
        for job in jobs
        if job and job.get('data-location')
    ]
    if jobs:
        return jobs


def electricera_jobs(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find_all('div', {'class', 'ee_careers_posting'})

    jobs = [
        job_object(
            title=job.find('h3').text,
            company=name,
            location=(['Seattle, USA']),
            url=job.find('a')['href'].replace('https://', ''),
            datetime=None,
            job_type=job_typer(job.text)
        )
        for job in jobs
        if job and job.find('a')

    ]
    if jobs:
        return jobs


def parkmobile_jobs(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find('ul', {'id': 'jobs_list_container'})
    jobs = jobs.find_all('li', {'class': 'w-full'})



    jobs = [
        job_object(
            title=job.find(
                'span', class_='text-block-base-link').get_text(strip=True),
            company=name,
            location=[
                i.text
                for i in job.find('div', class_='mt-1 text-md').find_all('span')
                if i.text not in ['·']
                and 'Sales' not in i.text
            ],
            url=job.find('a', href=True)['href'],
            datetime=None,
            job_type=job_typer(
                job.find('span', class_='text-block-base-link').get_text(strip=True))
        )
        for job in jobs
        if job
        and job.find('span', class_='text-block-base-link')

    ]
    if jobs:
        return jobs


def fleet_jobs(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find('div', {'class', 'careers-grid'})
    jobs = jobs.find_all('a')


    jobs = [
        job_object(
            title=job.find_all('div')[0].text,
            company=name,
            location=([job.find_all('div')[1].text]),
            url=job.get('href'),
            datetime=None,
            job_type=job_typer(job.find_all('div')[0].text)
        )
        for job in jobs
        if job and job.find_all('div')

    ]
    if jobs:
        return jobs


def nplan_jobs(response, name='', id=''):
    website = 'https://nplan.breezy.hr{}'
    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find_all('ul', {'class', 'positions location'})



    jobs = [
        position
        for job_list in jobs
        for position in job_list.find_all('li', class_='position transition')
    ]



    jobs = [
        job_object(
            title=job.find('h2').text,
            company=name,
            location=[
                span.text
                for span in job.find('li', class_='location').find_all('span')
                if span
            ],
            url=website.format(job.find('a')['href']),
            datetime=None,
            job_type=job_typer(job.find('h2').text)
        )
        for job in jobs
        if job
        and job.find('h2')
        and job.find('li', class_='location')

    ]

    if jobs:
        return jobs


def arcadis_jobs(response, name='', id=''):
    jobs = [
        job_object(
            title=job.find('h4').text,
            company=name,
            location=[page.find('h3').text],
            url=job.find('a')['href'],
            datetime=None,
            job_type=job_typer(job.find('h4').text)
        )
        for response in response
        for page in BeautifulSoup(response.content, 'html.parser')
        for job in page.find_all('li')
        if job.find('h4')
    ]
    if jobs:
        return jobs


def gridwise_jobs(response, name='', id=''):
    website = 'https://gridwise.io/careers/?ashby_jid={}'
    soup = BeautifulSoup(response.content, 'html.parser')

    script_tag = soup.find('script', text=re.compile(r'window\.__appData\s*='))
    if not script_tag:
        return None

    script_content = script_tag.string

    start_index = script_content.find('window.__appData =')
    if start_index == -1:
        return None

    json_start = script_content.find('{', start_index)
    if json_start == -1:
        return None

    json_end = script_content.find('};', json_start)
    if json_end == -1:
        return None

    json_text = script_content[json_start:json_end+1]
    
    app_data = json.loads(json_text)
    job_board = app_data.get('jobBoard', {})
    job_postings = job_board.get('jobPostings', [])


    jobs = [
        job_object(
            title=job.get('title'),
            company=name,
            location=[job.get('locationName')],
            url=website.format(job.get('id')),
            datetime=None,
            job_type=job_typer(job.get('title'))
        )
        for job in job_postings
        if job
        and job.get('title')

    ]
    if jobs:
        return jobs


def foursquareitp_jobs(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find('div', {'class', 'col col-xs-7 jobs-list'})


    jobs = jobs.find_all('li')


    jobs = [
        job_object(
            title=job.find('a').text,
            company=name,
            location=[job.find('li').text],
            url=job.find('a')['href'],
            datetime=None,
            job_type=job_typer(job.find('a').text)
        )
        for job in jobs
        if job
        and job.find('a')
        and job.find('li')

    ]

    if jobs:
        return jobs


def inrix_jobs(response, name='', id=''):
    website = 'https://jobs.jobvite.com{}'
    soup = BeautifulSoup(response.content, 'html.parser')

    jobs = [
        job
        for job_table in soup.find_all('table', {'class', 'jv-job-list'})
        for job in job_table.find_all('tr')
        if job_table.find_all('tr')
        and soup.find_all('table', {'class', 'jv-job-list'})
    ]

    jobs = [
        job_object(
            title=job.find('a').text,
            company=name,
            location=[job.find('td', {'class', 'jv-job-list-location'}).text],
            url=website.format(job.find('a')['href']),
            datetime=None,
            job_type=job_typer(job.find('a').text)
        )
        for job in jobs
        if job
        and job.find('td', {'class', 'jv-job-list-location'})
        and job.find('a')

    ]
    if jobs:
        return jobs


def masabi_job_parser(response, name='', id=''):
    website = "https://careers.masabi.com/?ashby_jid={}"
    jobs = response.json()

    jobs = jobs.get('data').get('jobBoard').get('jobPostings')

    jobs = [
        job_object(
            title=job.get('title'),
            company=name,
            location=[job.get('locationName')],
            url=website.format(job.get('id')),
            datetime=None,
            job_type=job_typer(job.get('title'))
        )
        for job in jobs
        if job

    ]
    if jobs:
        return jobs


def rebel_job_parser(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')

    jobs = soup.find_all('div', {'class', 'card card--equal js-link'})


    jobs = [
        job_object(
            title=job.find('a').text,
            company=name,
            location=[job.find('li').text],
            url=job.find('a').get('href'),
            datetime=None,
            job_type=job_typer(job.find('a').text, pre_type=[
                               'transport_enthusiast'])
        )
        for job in jobs
        if job

    ]
    if jobs:
        return jobs


def haydenai_parser(response, name='', id=''):
    website = "www.hayden.ai/careers?ashby_jid={}"
    jobs = response.json()


    jobs = jobs.get('data').get('jobBoard').get('jobPostings')


    jobs = [
        job_object(
            title=job.get('title'),
            company=name,
            location=[job.get('locationName')],
            url=website.format(job.get('id')),
            datetime=None,
            job_type=job_typer(job.get('title'))
        )
        for job in jobs
        if job

    ]
    if jobs:
        return jobs


def cabify_jobs(response, name='', id=''):
    website = 'https://cabify.careers{}'
    soup = BeautifulSoup(response.content, 'html.parser')

    jobs = soup.find('ul', {'class', 'grid'})

    jobs = jobs.find_all('li')

    jobs = [
        job_object(
            title=job.find('div', {'class', "card-title heading-1"}).text,
            company=name,
            location=[job.find('div', {'class', 'card-info-location'}).text],
            url=website.format(job.find('a')['href']),
            datetime=None,
            job_type=job_typer(
                job.find('div', {'class', "card-title heading-1"}).text)
        )
        for job in jobs
        if job
        and job.find('div', {'class', "card-title heading-1"})

    ]
    if jobs:
        return jobs

def urbanfootprint_jobs(response, name='', id=''):
    website = 'https://boards.greenhouse.io{}'
    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find_all('div', {'class', 'opening'})

    jobs = [
        job_object(
            title=job.find('a').text,
            company=name,
            location=[job.find('span', {'class', 'location'}).text],
            url=website.format(job.find('a')['href']),
            datetime=None,
            job_type=job_typer(
                job.find('a').text)
        )
        for job in jobs
        if job
    ]
    if jobs:
        return jobs

def podaris_jobs(response, name='', id=''):
    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find_all('a', {'class', 'homerun-widget__vacancy'})

    jobs = [
        job_object(
            title=job.find('h3').text,
            company=name,
            location=[job.find('span', {'class', 'homerun-widget__vacancy__department'}).text],
            url=job.get('href'),
            datetime=None,
            job_type=job_typer(
                job.find('h3').text)
        )
        for job in jobs
        if job
    ]
    if jobs:
        return jobs
