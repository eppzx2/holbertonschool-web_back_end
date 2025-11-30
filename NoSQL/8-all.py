#!/usr/bin/python3
"""
lists all doc in collection
"""


def list_all(mongo_collection):
    """pymongo"""

    if not mongo_collection:
        return []
    documents = list(mongo_collection.find())
    return documents
