#!/usr/bin/env python3
"""This script to list all documents in a MongoDB collection"""
import pymongo


def list_all(mongo_collection):
    """Function that lists all documents in a collection"""

		# handle None Case
    if mongo_collection is None:
        return []

    return list(mongo_collection.find())
