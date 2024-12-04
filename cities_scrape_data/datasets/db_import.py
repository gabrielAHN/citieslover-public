import os
import io
import psycopg2
import itertools

from dotenv import load_dotenv
from ..scrapers.scraped_objects import get_scrape_objects
from ..websites.websites_info import website_info


load_dotenv()

def ensure_list(value):
    if value is None:
        return []
    elif isinstance(value, list):
        return value
    else:
        return [value]

def db_import(max_threads=5, chunks=25):
    database_url = os.getenv('DATABASE_PUBLIC_URL')
    if not database_url:
        raise ValueError("DATABASE_URL environment variable not set.")

    try:
        conn = psycopg2.connect(database_url)
        conn.autocommit = False  # Start a transaction
        cur = conn.cursor()

        create_temp_table = """
        CREATE TEMPORARY TABLE temp_scrape_data (
            source TEXT,
            name TEXT,
            source_type TEXT,
            title TEXT,
            url TEXT,
            datetime TIMESTAMP,
            company TEXT,
            country TEXT[],
            location TEXT,
            job_type TEXT[]
        ) ON COMMIT DROP;
        """
        cur.execute(create_temp_table)

        scrape_objects = get_scrape_objects(max_threads=max_threads)
        
        db_import_brand_data(website_info, cur, chunks)
        db_import_website_data(scrape_objects, cur, chunks)

        cur.execute("CALL process_scrape_data();")

        conn.commit()  # Commit the transaction
        print("Database import successful ✅")
    except Exception as e:
        conn.rollback()
        print(f"Error during bulk upload: {e}")
    finally:
        cur.close()
        conn.close()

def db_import_brand_data(website_info, cur, chunks):
    total_records = len(website_info)
    cur.execute("TRUNCATE TABLE brand_data;")
                
    for i in range(0, total_records, chunks):
        chunk = website_info[i:i+chunks]
        buffer = io.StringIO()

        for item in chunk:
            # Extracting 'type' as strings instead of dictionaries
            brand_type = [scraper['type'] for scraper in item.get('scrapers', [])]
            brand_type_formatted = '{' + ','.join(brand_type) + '}' if brand_type else '{}'
            fields = [
                item.get('id', ''),
                item.get('name', ''),
                item.get('image', ''),
                brand_type_formatted
            ]

            # Sanitize fields
            sanitized_fields = [
                str(v).replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').replace('\\', '\\\\')
                for v in fields
            ]
            buffer.write('\t'.join(sanitized_fields) + '\n')
        buffer.seek(0)
        chunk_import(
            cur=cur,
            buffer=buffer,
            tablename='brand_data',
            columns=('id', 'name', 'image', 'brand_type')
        )

def db_import_website_data(scrape_objects, cur, chunks):
    for chunk in chunk_iterator(iter(scrape_objects), chunks):
        buffer = io.StringIO()
        for scrape_object in chunk:
            source = scrape_object.source or ''
            name = scrape_object.name or ''
            source_type = scrape_object.source_type or ''
            title = scrape_object.title or ''
            url = scrape_object.url or ''
            datetime_str = scrape_object.datetime.strftime('%Y-%m-%d %H:%M:%S') if scrape_object.datetime else ''
            company = getattr(scrape_object, 'company', '') or ''
            country = getattr(scrape_object, 'country', [])
            location = getattr(scrape_object, 'location', '') or ''
            job_type = getattr(scrape_object, 'job_type', [])

            # Format lists as required
            country_formatted = '{' + ','.join(country) + '}' if country else '{}'
            job_type_formatted = '{' + ','.join(job_type) + '}' if job_type else '{}'

            # Prepare fields
            fields = [
                source,
                name,
                source_type,
                title,
                url,
                datetime_str,
                company,
                country_formatted,
                location,
                job_type_formatted
            ]

            # Sanitize fields
            sanitized_fields = [
                str(field).replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').replace('\\', '\\\\')
                for field in fields
            ]

            buffer.write('\t'.join(sanitized_fields) + '\n')
        
        buffer.seek(0)
        chunk_import(
            cur=cur,
            buffer=buffer,
            tablename='temp_scrape_data',
            columns=(
                'source', 'name', 'source_type', 'title', 'url',
                'datetime', 'company', 'country', 'location',
                'job_type'
            )
        )

def chunk_import(cur, buffer, tablename, columns):
    cur.copy_from(
        file=buffer,
        table=tablename,
        columns=columns,
        sep='\t',
        null=''
    )

def chunk_iterator(iterator, size):
    """Yield successive chunks from the iterator of specified size."""
    while True:
        chunk = list(itertools.islice(iterator, size))
        if not chunk:
            break
        yield chunk