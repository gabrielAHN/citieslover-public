import os
import json
import random


date_file = os.path.dirname(os.path.abspath(__file__))


def create_jobs_data(scrape_objects):
    jobs_file = '{}/job_objects.json'.format(date_file)
    scrape_objects = sorted(
        scrape_objects,
        key=lambda x: x.scrape_object.datetime,
        reverse=True
    )
    jobs_data = [
        {
            'source': job.source,
            'title': job.scrape_object.title,
            'company': job.scrape_object.company,
            'location': job.scrape_object.location,
            'url': job.scrape_object.url,
            'post_time': str(job.scrape_object.datetime)
        }
        for job in scrape_objects
        if job.source_type == 'job'
    ]

    with open(jobs_file, 'w+') as f:
        json.dump(jobs_data, f, indent=2)


def create_website_post_data(scrape_objects):
    post_file = '{}/post_objects.json'.format(date_file)
    brand_dict = get_dataset('brand_dict') 
    post_data = {
        brand: limit_objects(
                [
                    {
                        'source': post.source,
                        'title': post.scrape_object.title,
                        'url': post.scrape_object.url,
                        'post_time': str(post.scrape_object.datetime)
                    }
                    for post in scrape_objects
                    if post.source_type != 'job'
                    and brand == post.source
                ]
        )
        for brand in brand_dict

    }
    post_data = {
        post: post_data[post]
        for post in post_data
        if post_data[post]

    }
    post_data = randomize_dict(post_data)
    with open(post_file, 'w+') as f:
        json.dump(post_data, f, indent=2)


def create_brand_data(website_info):
    brand_file = '{}/brand_dict.json'.format(date_file)
    brands = {
        brand: {
            'name': website_info[brand].get('name'),
            'type': website_info[brand].get('type'),
            'image': website_info[brand].get('image'),
            'image_size': website_info[brand].get('image_size')
        }
        for brand in website_info
    }
    with open(brand_file, 'w+') as f:
        json.dump(brands, f, indent=2)


def get_dataset(file_type):
    file = "{}/{}.json".format(date_file, file_type)
    try:
        with open(file) as f:
            data = json.load(f)
            return data
    except IOError:
        return None


def limit_objects(website_objects):
    if len(website_objects) > 5:
        return website_objects[:5]
    return website_objects


def randomize_dict(data_dict):
    keys = list(data_dict.keys())
    random.shuffle(keys)
    data_dict = {
        key: data_dict[key]
        for key in keys
    }
    return data_dict
