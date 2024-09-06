#!/usr/bin/env python3
"""This script provides some stats about Nginx logs stored in MongoDB."""

from pymongo import MongoClient


def get_collection():
    """Establishes a connection to the MongoDB server and
                returns the nginx collection."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    return client.logs.nginx


def count_documents(collection, query):
    """Counts the number of documents that match a query."""
    return collection.count_documents(query)


def print_log_stats(collection):
    """Prints the statistics of Nginx logs."""
    # Count the total number of documents in the collection
    total_logs = count_documents(collection, {})
    print(f"{total_logs} logs")

    # Count the number of documents for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = count_documents(collection, {"method": method})
        print(f"\tmethod {method}: {method_count}")

    # Count the number of documents with method="GET" and path="/status"
    status_check_count = count_documents(
        collection, {"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")


def main():
    """Main function to execute the log stats script."""
    collection = get_collection()
    print_log_stats(collection)


if __name__ == "__main__":
    main()
