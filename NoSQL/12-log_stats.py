#!/usr/bin/env python3
""" 12-log_stats.py """

from pymongo import collection
from pymongo import MongoClient


def log_stats():

"""conncet to MongoDB and retrieve stats"""

client = MongoClient("mongodb://127.0.0.1:27017")
db = client.logs
collection = db.nginx

"""get the total number of documents in the collection"""

total = collection.count_documents({})

"""get the number of documents for each method"""

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_count = {
        method: collection.count_documents({"method": method}) for method in methods
    }

    """get the number of documents with method=GET and path=/status"""

    status_check = collection.count_documents({"method": "GET", "path": "/status"})

    print(f"{total} logs")
    print("Methods:")
    for method, count in method_count.items():
				print(f"\tmethod {method}: {count}")
    print(f"{status_check} status check")

    if __name__ == "__main__":
				log_stats()
