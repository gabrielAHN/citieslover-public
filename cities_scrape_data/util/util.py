import os

import re
import json
import random
import boto3

from dotenv import load_dotenv

load_dotenv()

date_file = os.path.dirname(os.path.abspath(__file__))

REPLACEMENT_PAIRS = [
    ("\xa0", ''),
    ("&nbsp;", ' '),
    ("&#39;", "'"),
    ("&#039;", "'"),
    ("&quot;", "'"),
    ("FTE/FTC", ""),
    ("Hybrid—", "Hybrid"),
    ("Remote—", "Remote"),
    ("On-site—", "On-site")
]


BAD_STRINGS = [
    "See omnystudio.com/policies/listener for privacy information.",
    "Continue reading on TheCityFix.com.",
    "CompTIA&#39;s",
    "Sign up to become a member at strongtowns",
    "\n"
]


def clean_string(string):
    string = re.sub(r'<.*?>', '', string)
    string = re.sub(r'\—$', '', string)
    string = re.sub(r'\s+', ' ', string)
    for pairs in REPLACEMENT_PAIRS:
        string = string.replace(pairs[0], pairs[1])
    for remove in BAD_STRINGS:
        string = string.replace(remove, '')
    string = string.strip()
    return string


def get_dataset(file_type):
    file = "{}/{}.json".format(date_file, file_type)
    try:
        with open(file) as f:
            data = json.load(f)
            return data
    except IOError:
        return None


def limit_objects(website_objects):
    if len(website_objects) > 5:
        return website_objects[:5]
    return website_objects


def randomize_dict(data_dict):
    keys = list(data_dict.keys())
    random.shuffle(keys)
    data_dict = {
        key: data_dict[key]
        for key in keys
    }
    return data_dict


def import_to_s3(file, data, bucket=os.getenv('AWS_BUCKET_NAME')):
    s3 = boto3.resource(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    )
    s3object = s3.Object(bucket, file)
    s3object.put(Body=data)
