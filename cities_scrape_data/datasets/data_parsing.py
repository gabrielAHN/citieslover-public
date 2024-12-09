import json
import random


def create_jobs_data(scrape_objects):
    scrape_objects = sorted(
        scrape_objects,
        key=lambda x: x.datetime,
        reverse=True
    )

    jobs_data = [
        {
            'source': job.source,
            'source_name': job.name,
            'title': job.title,
            'company': job.company,
            'location': job.location,
            'country': job.country,
            'url': job.url,
            'post_time': str(job.datetime),
            'job_type': job.job_type
        }
        for job in scrape_objects
        if 'jobs' in job.source_type
        and hasattr(job, 'company')
    ]
    random.shuffle(jobs_data)
    return json.dumps(jobs_data, indent=2)


def create_post_data(scrape_objects):
    post_data = [
        {
            'source': post.source,
            'source_name': post.name,
            'title': post.title,
            'url': post.url,
            'type': post.source_type,
            'post_time': str(post.datetime)
        }
        for post in scrape_objects
        if 'jobs' != post.source_type
    ]
    random.shuffle(post_data)
    return json.dumps(post_data, indent=2)


def create_brand_data(website_info):
    brand_data = {
        brand['id']: {
            'name': brand['name'],
            'type': list(set([
                scraper['type']
                for scraper in brand['scrapers']
            ])),
            'image': brand['image'],
        }
        for brand in website_info
    }
    return json.dumps(brand_data, indent=2)
