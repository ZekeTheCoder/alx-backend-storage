#!/usr/bin/env python3
"""This script provides some stats about Nginx logs stored in MongoDB."""
from pymongo import MongoClient


def collection(db: dict) -> int:
    """Function to retrieve logs information"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    return logs.count_documents(db)


def main():
    """Function that returns stats about Nginx logs stored in MongoDB"""

    print(f"{collection({})} logs")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {collection({'method': method})}")
    print(f"{collection({'method': 'GET', 'path': '/status'})} status check")


if __name__ == "__main__":
    main()
