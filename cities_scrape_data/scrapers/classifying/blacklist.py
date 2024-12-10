JOB_TITLES_BLOCK = [
    'finance', 'health', 'hr', 'strategic', 'office coordinator',
    'advertising', 'payroll', 'office manager', 'accountant',
    'full time seasonal', 'driver', 'talent acquisition',
    'talent pool', 'mechanic', 'shift', 'technician',
    'recruiter', 'ranger', 'mécanicien', 'financial',
    'open application', 'submit your resume', 'tax', 'payroll',
    'equipment maintenance', 'accountant', 'treasury', 'diversity',
    'foot patrol', 'hr compensations', 'don\'t see a position that',
    'want to join inspiration', "don\'t see a role for you?",
    'cost controller', 'project accountant', 'copywriter',
    'general application', 'diversity and inclusion', 'head Of tax',
    'workplace'
]

def check_blacklist_object(response_object, object):
    if (response_object.type == "jobs"):
        title_check = [
            job_title
            for job_title in JOB_TITLES_BLOCK
            if  job_title in object.title.lower()
        ]
        if title_check:
            return None
    return object