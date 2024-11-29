import sys
import argparse
import os

from .datasets.create_data_files import create_datasets
from .datasets.db_import import db_import

from .scrape_logging.scrape_logging import get_filtered_sources, get_websites_info


def main():
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
        '--local',
        action='store_true',
        help='create dataset local'
    )
    parser_create_datasets.add_argument(
        '--threads',
        type=int,
        default=5,
        help='Number of threads for multi-threading (default: 5).'
    )

    parser_import_datasets = subparsers.add_parser(
        'db_import',
        help='Import datasets to DB.'
    )
    parser_import_datasets.add_argument(
        '--threads',
        type=int,
        default=5,
        help='Number of threads for multi-threading (default: 5).'
    )
    parser_import_datasets.add_argument(
        '--chunks',
        type=int,
        default=25,
        help='Number of chunks for copy into DB (default: 25).'
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
        create_datasets(max_threads=args.threads, local=args.local)
    elif args.command == 'db_import':
        db_import(max_threads=args.threads, chunks=args.chunks)
    elif args.command == 'get_websites':
        get_websites_info()
    else:
        print('No command provided.')
        parser.print_help()
        sys.exit(1)