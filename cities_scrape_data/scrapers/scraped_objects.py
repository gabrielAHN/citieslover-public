from ..websites.websites_info import website_info
from ..util.cities_objects import scrape_object
from ..util.requests_types import website_requests
from ..util.util import limit_objects
import concurrent.futures


def get_scrape_objects(source_id=None, source_type=None, response=False, max_threads=None):
    all_websites = website_info.copy()

    if source_id is not None:
        all_websites = [
            website for website in all_websites
            if website['id'] == source_id
        ]

    for website in all_websites:
        if source_type is not None:
            website['scrapers'] = [
                scraper for scraper in website['scrapers']
                if scraper['type'] == source_type
            ]
        elif isinstance(source_type, list):
            website['scrapers'] = [
                scraper for scraper in website['scrapers']
                if scraper['type'] in source_type
            ]

    website_scraper_list = [
        (website, scraper)
        for website in all_websites
        for scraper in website['scrapers']
    ]

    def fetch_website_request(args):
        website, scraper = args
        return website_requests(website, scraper)

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        website_response = list(executor.map(fetch_website_request, website_scraper_list))

    if response:
        return website_response
    else:
        def process_response(response_object):
            result = []
            if response_object.response == 200 and response_object.content is not None:
                scraper_objects = response_object.scraper(
                    response=response_object.content,
                    name=response_object.name,
                    id=response_object.id,
                ) or []
                
                # Check if the source_type is 'jobs', if not, limit to 5 objects
                if response_object.type != 'jobs':
                    scraper_objects = limit_objects(scraper_objects)

                for scraper_object in scraper_objects:
                    if scraper_object:
                        obj = scrape_object(
                            source=response_object.id,
                            name=response_object.name,
                            source_type=response_object.type,
                            scrape_object=scraper_object
                        )
                        result.append(obj)
            return result

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
            scrape_objects_list = list(executor.map(process_response, website_response))

        scrape_objects = [obj for sublist in scrape_objects_list for obj in sublist]
        return scrape_objects