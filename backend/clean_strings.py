import re


BAD_STRINGS = [
    "See omnystudio.com/policies/listener for privacy information.",
    "Continue reading on TheCityFix.com.",
    "CompTIA&#39;s",
    "Sign up to become a member at strongtowns"
]

REPLACEMENT_PAIRS = [
    ("&nbsp;", ' '),
    ("&#39;", "'"),
    ("&#039;", "'"),
    ("&quot;", "'"),
]


def clean_string(string):
    string = re.sub(r'<.*?>', '', string)
    for pairs in REPLACEMENT_PAIRS:
        string = string.replace(pairs[0], pairs[1])
    for remove in BAD_STRINGS:
        string = string.replace(remove, '')
    string = string.strip()
    return string
