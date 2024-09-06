#!/usr/bin/env python3
"""This script provides some stats about Nginx logs stored in MongoDB."""
from pymongo import MongoClient


def main():
    """Function that returns stats about Nginx logs stored in MongoDB."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    print(f"{logs.count_documents({})} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {logs.count_documents({'method': method})}")

    status_check_count = logs.count_documents(
        {'method': 'GET', 'path': '/status'})
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    main()
