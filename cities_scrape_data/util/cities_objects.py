from ..scrapers.classifying.date_formatting import get_datetime
from ..scrapers.classifying.location_standardizer import location_standardizer, country_standardizer
from ..util.util import clean_string


class request_object:
    def __init__(self, id, name, url, type, scraper, response=None, error=None, content=None):
        self.id = id
        self.name = name
        self.url = url
        self.type = type
        self.scraper = scraper
        self.error = error
        self.content = content

        if isinstance(response, list):
            if any(resp.status_code == 200 for resp in response):
                self.response = 200
            else:
                self.response = response[0].status_code if response else None
        elif hasattr(response, 'status_code'):
            self.response = response.status_code
        else:
            self.response = response


class scrape_object:
    def __init__(self, source, name, source_type, title, url, datetime, company=None, country=[], location=[], job_type=[]):
        self.source = source
        self.name = name
        self.source_type = source_type
        self.title = title
        self.url = url
        self.datetime = datetime
        self.company = company
        self.country = country
        self.location = location
        self.job_type = job_type


class job_object:
    def __init__(self, title, url, datetime, company, location, job_type):
        self.title = clean_string(title).title()
        self.url = url.replace('www.', 'https://')
        self.datetime = get_datetime(
            *(clean_string(datetime),) if datetime else ())
        self.company = clean_string(company)
        self.country = country_standardizer(location)
        self.location = location_standardizer(location)
        self.job_type = job_type


class article_object:
    def __init__(self, title, url, datetime):
        self.title = clean_string(title).title()
        self.url = url
        self.datetime = get_datetime(datetime)
