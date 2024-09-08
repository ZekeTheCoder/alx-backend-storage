#!/usr/bin/env python3
"""This script returns students sorted by their average score."""


def top_students(mongo_collection):
    """Function that returns all students sorted by average score."""

    student_aggregation = [
        {
            "$project": {
                "name": 1,
                "topics": 1,
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]

    return mongo_collection.aggregate(student_aggregation)
