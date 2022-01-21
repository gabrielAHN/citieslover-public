# City Lover

City Lover is a newsletter built from scraping a bunch of city centric articles, and formatting them into an html page. See the real page here **[City Lover](https://www.gabrielhn.com/topics/citylover/)**

![website](/website_example.png)

## Use
```
# Test scrape for source
python main.py --test_source <source_id>

# Commands create datasets for jobs and post
python main.py --create_datasets all

# Commands create dataset for job
python main.py --create_datasets job

# Commands create dataset for post
python main.py --create_datasets post

```

## Setup
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
