#!/usr/bin/env python3
"""
pymongo ile kwargs istifade edib sened elave edtmek
"""


def insert_school(mongo_collection, **kwargs):
    """kwargs usage"""

    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
