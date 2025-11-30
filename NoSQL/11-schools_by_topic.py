#!/usr/bin/env python3
"""returns the list of school with spec"""


def schools_by_topic(mongo_collection, topic):
    """learn python"""

    if not mongo_collection:
        return []

    # MongoDB $in operatoru yox, $elemMatch və ya sadəcə find + list comprehension istifadə olunur
    documents = list(mongo_collection.find({"topics": topic}))
    return documents
