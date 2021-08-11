import random

from datetime import timedelta, date
from websites.websites_info import website_info
from datasets.data_parsing import create_brand_data, get_dataset
from scrapers.jobs_scrapers import job_object


class scrape_object:
    def __init__(self, source, source_type, scrape_object):
        self.source = source
        self.source_type = source_type
        self.scrape_object = scrape_object


def get_scrape_objects(data_date):
    create_brand_data(website_info)

    newsletter_objects = [
        scrape_object(
            source=website,
            source_type=website_info[website]['type'],
            scrape_object=article
        )
        for website in website_info
        for article in get_items_list(website_info[website].get('newsletter', []), data_date)
        if article
    ]
    jobs_objects = [
        scrape_object(
            source=website,
            source_type='job',
            scrape_object=job
        )
        for website in website_info
        for job in get_items_list(website_info[website].get('jobs', []), data_date)
        if job
    ]
    job_features = [
        scrape_object(
            source=jobs,
            source_type='job',
            scrape_object=job_object(
                title=job.get('title'),
                company=jobs,
                location=job.get('location'),
                url=job.get('url'),
                datetime='today'
            )
        )
        for jobs in get_dataset('job_features').keys()
        for job in get_dataset('job_features')[jobs]
    ]
    scrape_objects = jobs_objects + newsletter_objects + job_features
    return scrape_objects


def get_test_scrape_objects(source_id, data_date):
    filter_website_info = {
        website: website_info[website]
        for website in website_info
        if website == source_id
    }
    newsletter_objects = [
        scrape_object(
            source=website,
            source_type=filter_website_info[website]['type'],
            scrape_object=article
        )
        for website in filter_website_info
        for article in get_items_list(filter_website_info[website].get('newsletter', []), data_date)
        if article
    ]
    jobs_objects = [
        scrape_object(
            source=website,
            source_type='job',
            scrape_object=job
        )
        for website in filter_website_info
        for job in get_items_list(filter_website_info[website].get('jobs', []), data_date)
        if job
    ]
    scrape_objects = jobs_objects + newsletter_objects
    return scrape_objects


def get_items_list(website, data_date):
    if not website:
        return []
    scrape_function = website.get('scrape_function')
    if not scrape_function:
        return []
    items = scrape_function(website['website'])
    items = filter_latest(items, data_date)
    return items


def filter_latest(items, data_date):
    items = [
        item
        for item in items
        if item.datetime > data_date
    ]
    return items
