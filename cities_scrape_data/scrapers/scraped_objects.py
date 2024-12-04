import concurrent.futures

from ..util.util import limit_objects
from ..util.cities_objects import scrape_object
from ..util.requests_types import website_requests
from ..websites.websites_info import website_info
from ..scrapers.classifying.blacklist import check_blacklist_object



def get_scrape_objects(source_id=None, source_type=None, response=False, max_threads=None):
    if source_id is not None:
        filtered_websites = [
            website
            for website in website_info
            if website['id'] == source_id
        ]
    else:
        filtered_websites = website_info

    for website in filtered_websites:
        if source_type is not None:
            website['scrapers'] = [
                scraper
                for scraper in website.get('scrapers', [])
                if scraper.get('type') == source_type
            ]

    website_scraper_list = [
        (website, scraper)
        for website in filtered_websites
        for scraper in website.get('scrapers', [])
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

                if response_object.type != 'jobs':
                    scraper_objects = limit_objects(scraper_objects)

                for object in scraper_objects:
                    object=check_blacklist_object(response_object, object)
                    if object:
                        obj = scrape_object(
                            source=response_object.id,
                            name=response_object.name,
                            source_type=response_object.type,
                            url=getattr(object, 'url', None),
                            title=getattr(object, 'title', None),
                            datetime=getattr(object, 'datetime', None),
                            company=getattr(object, 'company', None),
                            country=getattr(object, 'country', None),
                            location=getattr(object, 'location', []),
                            job_type=getattr(object, 'job_type', [])
                        )
                        result.append(obj)
            return result

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
            scrape_objects_list = list(executor.map(process_response, website_response))

        scrape_objects = [obj for sublist in scrape_objects_list for obj in sublist]
        return scrape_objects