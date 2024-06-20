#!/usr/bin/env python3
""" script to display nginx stats from logs"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs
    nginx = logs.nginx

    doc_count = nginx.count_documents({})
    print(f'{doc_count} logs')

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print('Methods:')
    for method in methods:
        m = nginx.find({"method": method})
        count = nginx.count_documents({"method": method})
        print(f'\tmethod {m}: {count}')

    count = nginx.count_documents({"method": "GET", "path": "/status"})
    print(f'{count} status check')
