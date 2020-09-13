from backend.making_html import email_html, website_html
from backend.website_list import website_info


file = "/citylover/city_lover_newsletter.html"


def main():
	websites_list = website_info()
	html = website_html(websites_list)
	Html_file = open(file, "+w")
	Html_file.write(html)
	Html_file.close()


if __name__ == "__main__":
    main()
