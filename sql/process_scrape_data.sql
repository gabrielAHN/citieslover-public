CREATE OR REPLACE PROCEDURE process_scrape_data()
LANGUAGE plpgsql
AS $$
BEGIN
    -- Insert new records into website_data where url and source do not exist
    INSERT INTO website_data (
        source, name, source_type, title, url,
        added_date, latest_date, company, location,
        country, job_type, data_status
    )
    SELECT
        t.source,
        t.name,
        t.source_type,
        t.title,
        t.url,
        t.max_datetime AS added_date,
        t.max_datetime AS latest_date,
        t.company,
        t.location,
        t.country,
        t.job_type,
        'new' AS data_status
    FROM (
        SELECT
            source,
            name,
            source_type,
            title,
            url,
            MAX(datetime) AS max_datetime,
            company,
            location,
            country,
            job_type
        FROM temp_scrape_data
        GROUP BY source, name, source_type, title, url, company, location, country, job_type
    ) t
    WHERE NOT EXISTS (
        SELECT 1 FROM website_data w
        WHERE w.url = t.url AND w.source = t.source
    );

    -- Update existing records in website_data with the latest datetime
    UPDATE website_data w
    SET
        latest_date = GREATEST(w.latest_date, t.max_datetime),
        data_status = CASE
            WHEN GREATEST(w.latest_date, t.max_datetime) - w.added_date <= INTERVAL '2 weeks' THEN 'new'
            WHEN GREATEST(w.latest_date, t.max_datetime) - w.added_date <= INTERVAL '1 month' THEN 'normal'
            ELSE 'old'
        END
    FROM (
        SELECT url, source, MAX(datetime) AS max_datetime
        FROM temp_scrape_data
        GROUP BY url, source
    ) t
    WHERE w.url = t.url AND w.source = t.source;
END;
$$;