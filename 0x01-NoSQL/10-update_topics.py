#!/usr/bin/env python3
"""Script that changes all topics of a school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """Function that updates school topics based on name(first match)"""
    mongo_collection.update_one(
        {"name": name},
        {"$set": {"topics": topics}}
    )
