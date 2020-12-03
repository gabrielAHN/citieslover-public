from backend.new_website_page import create_updated_website
from backend.scraped_objects import article_objects

file = "/citylover/test.html"


def newsletter_page():
    articles = article_objects()
    html = create_updated_website(articles)
    Html_file = open(file, "+w")
    Html_file.write(html)
    Html_file.close()


if __name__ == "__main__":
    newsletter_page()
