#!/usr/bin/env python3

"""
inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    return the id of the created document
    """
    
    document = mongo_collection.insertOne(kwargs)
    
    return document.inserted_id
