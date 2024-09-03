#!/usr/bin/env python3

"""
lists all documents in a collection
"""

import pymongo

def list_all(mongo_collection):
    """
    lists all documents in a collection
    """
    collection_list = []
    if mongo_collection.count_documents({}) == 0:
        return collection_list
    else:
        collection_list = list(mongo_collection.find())
        return collection_list
