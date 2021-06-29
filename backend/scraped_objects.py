import random

from backend.website_info import website_dict


class source_object:
    def __init__(self, source, articles, article_type, image, image_size):
        self.source = source
        self.articles = articles
        self.article_type = article_type
        self.image = image
        self.image_size = image_size


def article_objects():
    articles = []
    [
        articles.append(
                source_object(
                    source=website_info['source'],
                    articles=website_info['scraped_function'](website_info['website']),
                    article_type=website_info['type'],
                    image=website_info['image'],
                    image_size= website_info['image_size'],
                )
            )
        for website_info in website_dict
        if website_info['scraped_function'](website_info['website'])
    ]
    random.shuffle(articles)
    return articles

