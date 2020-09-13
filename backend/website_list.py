import re

from backend.scraping_info import scarping_dict

BAD_STRINGS = [
    "See omnystudio.com/policies/listener for privacy information.",
    "Continue reading on TheCityFix.com.",
    "CompTIA&#39;s",
    "Sign up to become a member at strongtowns"
]


def website_info():
    for i in range(0, len(scarping_dict)):
        title, description, link = scarping_dict[i]['scraped_function'](scarping_dict[i]['website'])
        scarping_dict[i]['title'] = check_none(title)
        scarping_dict[i]['description'] = check_none(description)
        scarping_dict[i]['link'] = check_none(link)
    return scarping_dict


def check_none(string):
	if string:
		return string_clean(string)
	else:
		return ' '


def limit_description(description):
    if not description:
        description = ''    
    if len(description) > 200:
        description = '{}{}'.format(description[:200], '...')
    return description


def string_clean(strings):
    strings = re.sub('<.*?>', '', strings)
    strings = strings.replace("&nbsp;", ' ')
    strings = strings.replace("&#39;", "'")
    strings = strings.replace("&#039;", "'")
    strings = strings.replace("&quot;", "'")
    for string in BAD_STRINGS:
        strings = strings.replace(string, '')
    strings = strings.strip()
    return limit_description(strings)
