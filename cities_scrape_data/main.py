import sys
import argparse
import os

from .datasets.data_parsing import create_datasets
from .scrapers.scraped_objects import get_scrape_objects
from .scrape_logging.scrape_logging import get_filtered_sources, get_websites_info


def create_scrape_datasets(max_threads=5):
    scrape_objects = get_scrape_objects(max_threads=max_threads)
    scrape_objects = create_datasets(scrape_objects)
    return 'datasets_created'


def main():
    print(f"PYTHONPATH: {sys.path}")
    print(f"Current working directory: {os.getcwd()}")
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(
        title='Commands',
        dest='command',
        description='Available commands',
        help='Description'
    )

    parser_test_source = subparsers.add_parser(
        'test_source',
        help='Test data by source.'
    )
    parser_test_source.add_argument(
        '--source',
        required=True,
        help='Specify the source to test.'
    )
    parser_test_source.add_argument(
        '--response',
        action='store_true',
        help='Get responses only.'
    )
    parser_test_source.add_argument(
        '--threads',
        type=int,
        default=5,
        help='Number of threads for multi-threading (default: 5).'
    )

    parser_test_by_type = subparsers.add_parser(
        'test_by_type',
        help='Test data by type.'
    )
    parser_test_by_type.add_argument(
        '--type',
        required=True,
        help='Specify the type to test.'
    )
    parser_test_by_type.add_argument(
        '--response',
        action='store_true',
        help='Get responses only.'
    )
    parser_test_by_type.add_argument(
        '--threads',
        type=int,
        default=5,
        help='Number of threads for multi-threading (default: 5).'
    )

    parser_test_all = subparsers.add_parser(
        'test_all',
        help='Test all data.'
    )
    parser_test_all.add_argument(
        '--response',
        action='store_true',
        help='Get responses only.'
    )
    parser_test_all.add_argument(
        '--threads',
        type=int,
        default=5,
        help='Number of threads for multi-threading (default: 5).'
    )

    parser_create_datasets = subparsers.add_parser(
        'create_datasets',
        help='Create datasets.'
    )
    parser_create_datasets.add_argument(
        '--threads',
        type=int,
        default=5,
        help='Number of threads for multi-threading (default: 5).'
    )

    subparsers.add_parser(
        'get_websites',
        help='Get websites info.'
    )

    args = parser.parse_args()

    if args.command == 'test_source':
        get_filtered_sources(
            source_id=args.source,
            response=args.response,
            max_threads=args.threads
        )
    elif args.command == 'test_by_type':
        get_filtered_sources(
            source_type=args.type,
            response=args.response,
            max_threads=args.threads
        )
    elif args.command == 'test_all':
        get_filtered_sources(
            response=args.response,
            max_threads=args.threads
        )
    elif args.command == 'create_datasets':
        create_scrape_datasets(max_threads=args.threads)
    elif args.command == 'get_websites':
        get_websites_info()
    else:
        print('No command provided.')
        parser.print_help()
        sys.exit(1)