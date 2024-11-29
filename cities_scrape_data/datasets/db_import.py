import os
import io
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
from ..scrapers.scraped_objects import get_scrape_objects

def ensure_list(value):
    if value is None:
        return []
    elif isinstance(value, list):
        return value
    else:
        return [value]

def db_import(max_threads=5, chunks=25):
    load_dotenv()

    database_url = os.getenv('DATABASE_URL')
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
        # No need to commit here; the table exists within the transaction

        scrape_objects = get_scrape_objects(max_threads=max_threads)

        data = []
        for scrape_object in scrape_objects:
            item = {
                'source': scrape_object.source,
                'name': scrape_object.name,
                'source_type': scrape_object.source_type,
                'title': scrape_object.title,
                'url': scrape_object.url,
                'datetime': scrape_object.datetime,
                'company': getattr(scrape_object, 'company', None),
                'country': ensure_list(getattr(scrape_object, 'country', [])),
                'location': getattr(scrape_object, 'location', None),
                'job_type': ensure_list(getattr(scrape_object, 'job_type', []))
            }
            data.append(item)

        total_records = len(data)
        for i in range(0, total_records, chunks):
            chunk = data[i:i+chunks]
            process_chunk(chunk, cur)
            # No need to commit after each chunk; commit at the end

        cur.execute("CALL process_scrape_data();")
        # The temporary table is accessible within the same transaction

        conn.commit()  # Commit the transaction
        print("Database import successful ✅")
    except Exception as e:
        conn.rollback()
        print(f"Error during bulk upload: {e}")
    finally:
        cur.close()
        conn.close()

def process_chunk(chunk, cur):
    buffer = io.StringIO()
    for item in chunk:
        job_type_formatted = '{' + ','.join(item['job_type']) + '}' if item['job_type'] else '{}'
        country_formatted = '{' + ','.join(item['country']) + '}' if item['country'] else '{}'
        fields = [
            item['source'] or '',
            item['name'] or '',
            item['source_type'] or '',
            item['title'] or '',
            item['url'] or '',
            item['datetime'].strftime('%Y-%m-%d %H:%M:%S') if item['datetime'] else '',
            item['company'] or '',
            country_formatted,
            item['location'] or '',
            job_type_formatted
        ]

        fields = [str(v).replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').replace('\\', '\\\\') for v in fields]
        buffer.write('\t'.join(fields) + '\n')
    buffer.seek(0)

    cur.copy_from(
        file=buffer,
        table='temp_scrape_data',
        columns=('source', 'name', 'source_type', 'title', 'url',
                 'datetime', 'company', 'country', 'location', 'job_type'),
        sep='\t',
        null=''
    )