# CityLover

Citylover 💚a place where you can find jobs 💼 and news 📰 for all those looking for anything related to urbanism  🌆.

This script scrapes different websites and uploads to S3 Buckets to be rendered here **[City Lover](https://www.gabrielhn.com/citylover/)**

![website](/citylover-hover.gif)

## Setup
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Use
```
# Test scrape for differet source
python main.py --test_source <source_id>

# Test scrape by source type
python main.py --test_source <jobs or newsletter>

# Get all sources id
python main.py get_websites

# Create files to be Uploaded to S3 Bucket
python main.py create_datasets
```