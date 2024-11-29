
from .data_parsing import create_brand_data, create_jobs_data, create_post_data
from ..scrapers.scraped_objects import get_scrape_objects

from ..websites.websites_info import website_info
from ..util.util import import_to_s3, write_json_files

def create_datasets(max_threads=5, local=False):
    scrape_objects = get_scrape_objects(max_threads=max_threads)

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
