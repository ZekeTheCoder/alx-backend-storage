#!/usr/bin/env python3
"""This script provides some stats about Nginx logs stored in MongoDB."""
from pymongo import MongoClient


def collection(db: dict) -> int:
    """Function to retrieve logs information"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    logs_count = logs.count_documents(db)
    client.close()  # Close the connection after performing the query
    return logs_count


def main():
    """Function that returns stats about Nginx logs stored in MongoDB"""

    # total number of logs
    print(f"{collection({})} logs")

    # HTTP methods to check
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # count for each HTTP method
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {collection({'method': method})}")

    # status check count
    print(f"{collection({'method': 'GET', 'path': '/status'})} status check")


if __name__ == "__main__":
    main()
