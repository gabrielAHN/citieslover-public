import json
import random

from ..websites.websites_info import website_info
from ..util.util import import_to_s3, write_json_files


def create_datasets(scrape_objects, local):
    jobs_data = create_jobs_data(scrape_objects)
    post_data = create_post_data(scrape_objects)
    brand_dict = create_brand_data(website_info)
    
    if local:
        print('Creating datasets locally...')
        write_json_files('jobs_data.json', jobs_data)
        write_json_files('post_data.json', post_data)
        write_json_files('brand_dict.json', brand_dict)
    else:
        print('Creating datasets in S3...')
        import_to_s3('citieslover-data/jobs_data.json', jobs_data)
        import_to_s3('citieslover-data/post_data.json', post_data)
        import_to_s3('citieslover-data/brand_dict.json', brand_dict)

    print("Datasets created ✅")


def create_jobs_data(scrape_objects):
    scrape_objects = sorted(
        scrape_objects,
        key=lambda x: x.scrape_object.datetime,
        reverse=True
    )

    jobs_data = [
        {
            'source': job.source,
            'source_name': job.name,
            'title': job.scrape_object.title,
            'company': job.scrape_object.company,
            'location': job.scrape_object.location,
            'country': job.scrape_object.country,
            'url': job.scrape_object.url,
            'post_time': str(job.scrape_object.datetime),
            'job_type': job.scrape_object.job_type
        }
        for job in scrape_objects
        if 'job' in job.source_type
        and hasattr(job.scrape_object, 'company')
    ]
    random.shuffle(jobs_data)
    return json.dumps(jobs_data, indent=2)


def create_post_data(scrape_objects):
    post_data = [
        {
            'source': post.source,
            'source_name': post.name,
            'title': post.scrape_object.title,
            'url': post.scrape_object.url,
            'type': post.source_type,
            'post_time': str(post.scrape_object.datetime)
        }
        for post in scrape_objects
        if 'jobs' != post.source_type
        and not hasattr(post.scrape_object, 'company')
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
