import re

from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta


AGO_REGEX = re.compile(r'\d+ (day|week|month)s? ago')
DATE_NAME_REGEX = re.compile(r'\d+\.\d+\.\d+\, .+')
DAY_REGEX = re.compile(r'(?P<amount>\d+) (?P<days>days?) ago')
WEEK_REGEX = re.compile(r'(?P<amount>\d+) (?P<week>weeks?) ago')
MONTH_REGEX = re.compile(r'(?P<amount>\d+) (?P<month>months?) ago')


def get_datetime(url_date=None):
    date_parsers = (
        "%B %d, %Y", "%b %d %Y",
        "%b %d, %Y", "%d %B %Y",
        "%Y-%m-%d", "%b. %d, %Y",
        '%d/%m/%Y',
    )
    today = date.today()

    if not url_date:
        return today
    
    try:
        url_date = re.sub(r'((\+|\-)\d+|GMT$)', '', url_date).strip()
        url_date = datetime.strptime(url_date, "%a, %d %b %Y %H:%M:%S").date()
        return url_date
    except ValueError:
        pass
    try:
        year = date.today().year
        url_date = datetime.strptime(
            url_date, "%B %d").replace(year=year).date()
        return url_date
    except ValueError:
        pass
    for date_text in date_parsers:
        try:
            url_date = datetime.strptime(url_date, date_text).date()
            return url_date
        except ValueError:
            pass
    if re.search(DATE_NAME_REGEX, url_date):
        url_date = re.sub(r'\,.+', '', url_date).strip()
        url_date = datetime.strptime(url_date, "%d.%m.%Y").date()
        return url_date
    if re.search(AGO_REGEX, url_date):
        day_match = re.match(DAY_REGEX, url_date)
        week_match = re.match(WEEK_REGEX, url_date)
        month_match = re.match(MONTH_REGEX, url_date)
        if day_match:
            day_amount = day_match.groupdict().get('amount')
            today = today - timedelta(days=int(day_amount))
            return today
        if week_match:
            week_amount = week_match.groupdict().get('amount')
            today = today - relativedelta(weeks=int(week_amount))
            return today
        if month_match:
            month_amount = month_match.groupdict().get('amount')
            today = today - relativedelta(months=int(month_amount))
            return today
    return today
