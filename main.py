import os
import argparse
from datetime import timedelta, date

from datasets.data_parsing import create_jobs_data, create_website_post_data
from scrapers.scraped_objects import get_scrape_objects, get_test_scrape_objects



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--test_source', nargs='?', help='test_source')
    parser.add_argument("--create_datasets", nargs='?', help='create_datasets')
    args = parser.parse_args()

    today_date = date.today()

    if args.test_source:
        test_source(args.test_source, today_date)
    elif args.create_datasets == 'all':
        create_all_scrape_datasets(today_date)
    elif args.create_datasets in ['job', 'post']:
        create_specific_datasets(today_date, args.create_datasets)


def test_source(source_id, today_date):
    scraped_objects = get_test_scrape_objects(source_id, today_date)


def create_all_scrape_datasets(today_date):
    data_date = today_date - timedelta(days=30)
    scrape_objects = get_scrape_objects(data_date)
    create_jobs_data(scrape_objects)
    create_website_post_data(scrape_objects)
    print('datasets_created')  


def create_specific_datasets(today_date, dataset_type):
    data_date = today_date - timedelta(days=30)
    scrape_objects = get_scrape_objects(data_date)
    if 'job' == dataset_type:
        create_jobs_data(scrape_objects)
        print('Created job dataset')
    if 'post' == dataset_type:
        create_website_post_data(scrape_objects)
        print('Created post dataset')



if __name__ == "__main__":
    main()
