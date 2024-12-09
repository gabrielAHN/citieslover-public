import re


def cityleaders(title, company):
    title_list = [
        r'chief( of staff| planner| marketing officer)', r'director( of|,)', r'team lead',
        r'(vp|head) of', r'vice president', r'manager'
    ]
    company_list = []
    job_type = job_labeling('city_leaders', title_list,
                            company_list, title, company)
    return job_type


def city_sellers(title, company):
    title_list = [
        r'(sales|revenue) operations', r'sales( development)? representative',
        r'public sector sales', r'(acquisition|business|account) manager',
        r'account executive', r'(customer success|sales) manager', r'director of marketing'
        r'city partnerships director', r'emerging business', r'(business|rider growth) (coordinator|development|analyst)',
        r'go\-to\-market', r'growth \& success', r'head of bids'
    ]
    company_list = [
    ]
    job_type = job_labeling('city_sellers', title_list,
                            company_list, title, company)
    return job_type


def urban_scholars(title, company):
    title_list = [
        r'gis lecturer', r'(assistant|associate) professor',
        r'internship\: architecture', r'intern(s)?', 'researcher',
        r'research associate', r'education'
    ]
    company_list = [
        [r'urban Policy', r'(research fellow)'],
        [r'university', r'dean']
    ]
    job_type = job_labeling('urban_scholars', title_list,
                            company_list, title, company)
    return job_type


def transport_enthusiast(title, company):
    title_list = [
        r'transit operations',
        r'(transportation) plan(n)?(er|ing)',
        r'transportation planning',
        r'director of transportation',
        r'mobility'
    ]
    company_list = [
        [r'department of transportation', r'planner'],
        [r'State of .*', r'(Transportation Planner)'],
        [r'.* county', r'(public transportation)'],
        [r'(planning|transportation) commission', r'(planning|manager)']
    ]
    job_type = job_labeling('transport_enthusiast',
                            title_list, company_list, title, company)
    return job_type


def city_builders(title, company):
    title_list = [
        r'(associate|transportation|community|sustainability|environmental|senior|urban|principal|land( use)?|park|regional) planner',
        r'urban design', r'zoning specialist', r'planning (intern|manager)', r'deputy commissioner of planning',
        r'^planner$', r'(director of|transportation|Bridge) engineer(ing)?', r'architect', r'landscape project designer',
    ]
    company_list = [
        [r'(city|department of) planning', r'(director)'],
        [r'((city( and County)?|town) of)', r'(plann(ing|er))'],
        [r'county (board of|planning department)', r'plan(ner|ning director)']
    ]
    job_type = job_labeling('city_builders', title_list,
                            company_list, title, company)
    return job_type

def urban_techies(title, company):
    title_list = [
        r'(cloud|analytics|full stack|ios|python|react|software|reliability|(back|front(-)?)end|site '
        r'reliability|qa|support|platform security |design computation |gtfs|(staff )?machine learning|android|'
        r'customer success|mobile|automation|data) engineer', r'product analytics',
        r'(data|staff product|solutions|backend|customer support) (engineer|analyst)', r'\(?gis\)? (administrator|analyst)',
        r'database specialist', r'(engineering|product analytics|technical product) (manager|director)',
        r'(data infra|full stack) team', r'(front-end|java software|full(\-| )?stack( web)?|software|backend|java( or kotlin)?) developer',
        r'head of (ai|automation)', r'application support', r'(tech|analytics) lead', r'data scientist'
    ]
    company_list = [
    ]
    job_type = job_labeling('urban_techies', title_list,
                            company_list, title, company)
    return job_type


def gov_lovers(title, company):
    title_list = [
        r'of Government', r'department of', r'council of governments',
        r'^(city|state|town|county) of .*', r'government relations manager',
        r'senior manager, public Affairs', 'tax'
    ]

    company_list = [
        [r'(city planning)', r'(deputy director)'],
        [r'department of (housing( preservation)?|transportation|planning)',
         r'(community coordinator|project manager|analyst|director|policy (manager|specialist))'],
        [r'^((city|state|town) of .*|planning commission)', r'plan(ning|ner)'],
        [r'county board', r'planning director'],
        [r'.* county', r'(public transportation|planner)'],
        [r'council of governments', r'land use planner'],
        [r'transportation commission', r'manager']
    ]
    job_type = job_labeling('gov_lovers', title_list,
                            company_list, title, company)
    return job_type


def job_labeling(job_type, title_list, company_list, title, company):
    title_match = title_matching(title_list, title)
    if title_match:
        return job_type

    company_match = company_matching(company_list, title, company)
    if company_match:
        return job_type


def title_matching(title_list, title):
    if not title_list:
        return False
    keyword_match = [
        i
        for i in title_list
        if re.search(i, title.lower()) is not None
    ]
    if keyword_match:
        return True
    return False


def company_matching(company_list, title, company):
    if not company_list:
        return False
    keyword_match = [
        i
        for i in company_list
        if re.search(i[0], company.lower()) is not None
        and re.search(i[1], title.lower()) is not None
    ]
    if keyword_match:
        return True
    return False


def job_typer(title, company='', pre_type=[]):
    if not title:
        return []

    job_type_list = [
        urban_techies, city_builders, transport_enthusiast,
        gov_lovers, urban_scholars, city_sellers, cityleaders
    ]

    job_typings = [
        job_type(title, company)
        for job_type in job_type_list
        if job_type(title, company) is not None
    ]

    if pre_type:
        job_typings.extend(pre_type)
        job_typings = list(set(job_typings))

    if len(job_typings) == 0:
        return ['other']
    else:
        return job_typings
