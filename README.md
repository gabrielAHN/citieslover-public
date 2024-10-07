# Cities Lover

Cities Lover 💚 a place where you can find jobs 💼 and news 📰 for all those looking for anything related to urbanism 🌆.

This script scrapes different websites and uploads to S3 Buckets to be rendered here **[Cities Lover](https://www.gabrielhn.com/citieslover/)**

![website](/citieslover.gif)

## Setup
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Use
```
# Test scrape for a specific source
python -m cities_scrape_data test_source --source <source_id> [--response] [--threads <number_of_threads>]

# Test scrape by source type (e.g., jobs, podcasts, articles)
python -m cities_scrape_data test_by_type --type <jobs or newsletter> [--response] [--threads <number_of_threads>]

# Test scraping all data sources
python -m cities_scrape_data test_all [--response] [--threads <number_of_threads>]

# Create datasets to be uploaded to the S3 Bucket
python -m cities_scrape_data create_datasets [--threads <number_of_threads>]

# Get websites info
python -m cities_scrape_data get_websites
```