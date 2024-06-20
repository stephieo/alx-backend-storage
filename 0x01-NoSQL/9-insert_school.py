#!/usr/bin/env python3
""" function to insert new document into a mongoDB collection"""


if __name__ == "__main__":
    def insert_school(mongo_collection, **kwargs):
        """ inserts a document into a collection
        Args:
            mongo_collection: pymongo collection object
            **kwargs: key-value pairs for document
        Returns:
            _id of new document
        """
        doc_info = mongo_collection.insert_one(kwargs)
        return doc_info.inserted_id
