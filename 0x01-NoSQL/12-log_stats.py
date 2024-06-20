#!/usr/bin/env python3
""" script to display nginx stats from logs"""
from pymongo import MongoClient


client = MongoClient()
logs = client.logs
nginx = logs.nginx

doc_count = nginx.count_documents({})
print(f'{doc_count} logs')

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

print('Methods:')
for method in methods:
    count = nginx.count_documents({"method": method})
    print(f'    method {method}: {count}')

count = nginx.count_documents({"method": "GET", "path": "/status"})
print(f'{count} status check')
