#!/usr/bin/env python3
"""This script provides some stats about Nginx logs stored in MongoDB."""
from pymongo import MongoClient


def collection(db: dict) -> int:
    """Function that retrieve logs information"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    return logs.count_documents(db)


def top_ips() -> list:
    """Function to get the top 10 most present IPs"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx
    ip_counts = nginx_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    return list(ip_counts)


def main():
    """Function that returns stats about Nginx logs stored in MongoDB"""
    print(f"{collection({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {collection({'method': 'GET'})}")
    print(f"\tmethod POST: {collection({'method': 'POST'})}")
    print(f"\tmethod PUT: {collection({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {collection({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {collection({'method': 'DELETE'})}")
    print(f"{collection({'method': 'GET', 'path': '/status'})} status check")

    print("IPs:")
    for ip in top_ips():
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    main()
