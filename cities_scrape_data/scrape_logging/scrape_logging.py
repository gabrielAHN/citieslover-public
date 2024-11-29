from ..websites.websites_info import website_info
from ..scrapers.scraped_objects import (
    get_scrape_objects
)


def get_websites_info():
    all_websites = [
        website['id']+'\n'
        for website in website_info
    ]
    all_websites = ''.join(all_websites)
    print(all_websites)


def get_filtered_sources(source_id=None, source_type=None, response=False, max_threads=5):
    scraped_objects = get_scrape_objects(
        source_id=source_id, source_type=source_type, response=response, max_threads=max_threads
    )
    if response:
        for object in scraped_objects:
            print(
                f"id: {object.id}\nresponse: {object.response}\nurl: {object.url}\nerror: {object.error}")
    else:
        for object in scraped_objects:
            result = f'id: {object.source}\n'
            result += (
                ''.join("%s: %s\n" % item
                        for item in vars(object).items())
            )
            print(result)
