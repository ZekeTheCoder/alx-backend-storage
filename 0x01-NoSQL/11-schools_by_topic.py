#!/usr/bin/env python3
"""This script returns the list of schools that have a specific topic."""


def schools_by_topic(mongo_collection, topic):
    """Function returns the list of schools having a specific topic."""
    return list(mongo_collection.find({"topics": topic}))
