#!/usr/bin/env python3
"""List all documents in a collection"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection

    Args:
        mongo_collection: pymongo collection object

    Returns:
        List of all documents, empty list if no documents
    """
    return list(mongo_collection.find())