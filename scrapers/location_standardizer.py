import re
from scrapers.clean_strings import clean_string


USA_COUNTRY_REGEX = re.compile(r'(\(usa\)| us(a)?|united states)')
USA_STATE_REGEX = re.compile(
    r'(houston|washington|newark|new york|nyc|portland|san (francisco|josé)'
    r'|, (ma|mn|va|ny|ca|dc|il|co)$|california)|seattle|austin|dallas'
    r'|buena park|san franciso|indianapolis|fort collins|sacramento'
    r'|los angeles|atlanta|springfield|washington|virginia|new jersey')

UK_COUNTRY_REGEX = re.compile(r'united kingdom|uk')
UK_STATE_REGEX = re.compile(r'(london|cambridge)')

CANADA_COUNTRY_REGEX = re.compile(r'canada|^ca$')
CANADA_STATE_REGEX = re.compile(r'(vancouver|ottawa|montr(é|e)al(,)?)')

FRANCE_COUNTRY_REGEX = re.compile(r'france')
FRANCE_STATE_REGEX = re.compile(r'(lille|ottawa|paris(,)?)')

GERMANY_COUNTRY_REGEX = re.compile(r'germany')
GERMANY_STATE_REGEX = re.compile(r'(berlin|hannover|ludwigshafen)')

ITALY_COUNTRY_REGEX = re.compile(r'italy')
ITALY_STATE_REGEX = re.compile(r'((.*)?milan|rome)')

SPANISH_COUNTRY_REGEX = re.compile(r'(spain)')
SPANISH_STATE_REGEX = re.compile(r'(madrid)')

BELGIUM_COUNTRY_REGEX = re.compile(r'belgium')

SINGAPORE_CITY_REGEX = re.compile(r'singapore')

ARGENTIA_COUNTRY_REGEX = re.compile(r'buenos aires')

CHILE_COUNTRY_REGEX = re.compile(r'chile')

COLOMBIA_COUNTRY_REGEX = re.compile(r'colombia')

JAMAICA_COUNTRY_REGEX = re.compile(r'jamaica')

MEXICO_CITY_COUNTRY_REGEX = re.compile(r'mexico( city)?')

BRAZIL_COUNTRY_REGEX = re.compile(r'(são paulo|brazil)')

URUGUAY_COUNTRY_REGEX = re.compile(r'uruguay')


def remote_or_hybrid_standard(location):
    remote_regex = r'remote'
    hybrid_regex = r'hybrid'

    hybrid_match = re.search(hybrid_regex, location)
    remote_match = re.search(remote_regex, location)

    if hybrid_match:
        return 'Hybrid'
    elif remote_match:
        return 'Remote'


def usa_country_standard(location):

    USA_COUNTRY = re.search(USA_COUNTRY_REGEX, location)
    USA_STATE = re.search(USA_STATE_REGEX, location)

    if USA_COUNTRY or USA_STATE:
        return 'USA'


def uk_country_standard(location):

    UK_COUNTRY = re.search(UK_COUNTRY_REGEX, location)
    UK_STATE = re.search(UK_STATE_REGEX, location)

    if UK_COUNTRY or UK_STATE:
        return 'UK'


def canada_country_standard(location):

    CANADA_COUNTRY = re.search(CANADA_COUNTRY_REGEX, location)
    CANADA_STATE = re.search(CANADA_STATE_REGEX, location)

    if CANADA_COUNTRY or CANADA_STATE:
        return 'Canada'


def germany_country_standard(location):

    GERMANY_COUNTRY = re.search(GERMANY_COUNTRY_REGEX, location)
    GERMANY_STATE = re.search(GERMANY_STATE_REGEX, location)

    if GERMANY_COUNTRY or GERMANY_STATE:
        return 'Germany'


def belgium_country_standard(location):

    BELGIUM_COUNTRY = re.search(BELGIUM_COUNTRY_REGEX, location)

    if BELGIUM_COUNTRY:
        return 'Belgium'


def france_country_standard(location):

    FRANCE_COUNTRY = re.search(FRANCE_COUNTRY_REGEX, location)
    FRANCE_STATE = re.search(FRANCE_STATE_REGEX, location)

    if FRANCE_COUNTRY or FRANCE_STATE:
        return 'France'


def italy_country_standard(location):
    ITALY_COUNTRY = re.search(ITALY_COUNTRY_REGEX, location)
    ITALY_STATE = re.search(ITALY_STATE_REGEX, location)

    if ITALY_COUNTRY or ITALY_STATE:
        return 'Italy'


def spanish_country_standard(location):

    SPANISH_COUNTRY = re.search(SPANISH_COUNTRY_REGEX, location)
    SPANISH_STATE = re.search(SPANISH_STATE_REGEX, location)

    if SPANISH_COUNTRY or SPANISH_STATE:
        return 'Spain'


def argentia_country_standard(location):

    ARGENTIA_COUNTRY = re.search(ARGENTIA_COUNTRY_REGEX, location)

    if ARGENTIA_COUNTRY:
        return 'Argentina'


def chile_country_standard(location):

    CHILE_COUNTRY = re.search(CHILE_COUNTRY_REGEX, location)

    if CHILE_COUNTRY:
        return 'Chile'


def colombia_country_standard(location):

    COLOMBIA_COUNTRY = re.search(COLOMBIA_COUNTRY_REGEX, location)

    if COLOMBIA_COUNTRY:
        return 'Colombia'


def jamaica_country_standard(location):

    JAMAICA_COUNTRY = re.search(JAMAICA_COUNTRY_REGEX, location)

    if JAMAICA_COUNTRY:
        return 'Jamaica'


def mexico_city_country_standard(location):

    MEXICO_CITY_COUNTRY = re.search(MEXICO_CITY_COUNTRY_REGEX, location)

    if MEXICO_CITY_COUNTRY:
        return 'Mexico'


def brazil_country_standard(location):

    BRAZIL_COUNTRY = re.search(BRAZIL_COUNTRY_REGEX, location)

    if BRAZIL_COUNTRY:
        return 'Brazil'


def uruguay_country_standard(location):

    URUGUAY_COUNTRY = re.search(URUGUAY_COUNTRY_REGEX, location)

    if URUGUAY_COUNTRY:
        return 'Uruguay'


def singapore_country_standard(location):

    SINGAPORE_CITY = re.search(SINGAPORE_CITY_REGEX, location)

    if SINGAPORE_CITY:
        return 'Singapore'


def location_standardizer(locations, area='', country=''):

    location_list = []

    for location in locations:
        clean_location = clean_string(location)

        if clean_location:
            clean_location = clean_location.lower()
            remote_or_hybrid = remote_or_hybrid_standard(clean_location)

            if remote_or_hybrid:
                location_list.append(remote_or_hybrid)
            elif clean_location:
                location_list.append(clean_location.title())
            else:
                location_list.append('other')
    location_list = [
        i.strip()
        for i in location_list
        if i.strip() != '-'
    ]
    return ' - '.join(list(set(location_list)))


def country_standardizer(locations):
    location_list = []

    for location in locations:
        if location:
            clean_location = clean_string(location).lower()
            usa_country = usa_country_standard(clean_location)
            uk_country = uk_country_standard(clean_location)
            germany_country = germany_country_standard(clean_location)
            belgium_country = belgium_country_standard(clean_location)
            france_country = france_country_standard(clean_location)
            canada_country = canada_country_standard(clean_location)
            italy_country = italy_country_standard(clean_location)
            spanish_country = spanish_country_standard(clean_location)
            argentia_country = argentia_country_standard(clean_location)
            chile_country = chile_country_standard(clean_location)
            colombia_country = colombia_country_standard(clean_location)
            jamaica_country = jamaica_country_standard(clean_location)
            mexico_city_country = mexico_city_country_standard(clean_location)
            brazil_country = brazil_country_standard(clean_location)
            uruguay_country = uruguay_country_standard(clean_location)
            singapore_country = singapore_country_standard(clean_location)
            remote_or_hybrid = remote_or_hybrid_standard(clean_location)

            if usa_country:
                location_list.append(usa_country)
            if uk_country:
                location_list.append(uk_country)
            if canada_country:
                location_list.append(canada_country)
            if germany_country:
                location_list.append(germany_country)
            if belgium_country:
                location_list.append(belgium_country)
            if france_country:
                location_list.append(france_country)
            if italy_country:
                location_list.append(italy_country)
            if spanish_country:
                location_list.append(spanish_country)
            if singapore_country:
                location_list.append(singapore_country)
            if argentia_country:
                location_list.append(argentia_country)
            if chile_country:
                location_list.append(chile_country)
            if colombia_country:
                location_list.append(colombia_country)
            if jamaica_country:
                location_list.append(jamaica_country)
            if mexico_city_country:
                location_list.append(mexico_city_country)
            if brazil_country:
                location_list.append(brazil_country)
            if uruguay_country:
                location_list.append(uruguay_country)
            if 'tokyo' in clean_location:
                location_list.append('Japan')
            if 'israel' in clean_location:
                location_list.append('Israel')
            if 'norway' in clean_location:
                location_list.append('Norway')
            if 'warsaw' in clean_location:
                location_list.append('Poland')
            if 'hungary' in clean_location:
                location_list.append('Hungary')
            if 'saudi arabia' in clean_location:
                location_list.append('Saudi Arabia')
            if 'greece' in clean_location:
                location_list.append('Greece')
            if 'austria' in clean_location:
                location_list.append('Austria')
            if 'china' in clean_location:
                location_list.append('China')
            if 'switzerland' in clean_location:
                location_list.append('Switzerland')
            if remote_or_hybrid:
                location_list.append(remote_or_hybrid)

    if location_list:
        return list(set(location_list))
    else:
        return ['Other']
