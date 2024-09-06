#!/usr/bin/env python3
"""This script inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document into the collection and returns the new _id."""
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
