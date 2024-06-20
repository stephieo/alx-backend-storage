 #!/usr/bin/env python3
"""function to list all documents in a collection"""

if __name__ == "__main__":
    def list_all(mongo_collection):
        """ lists all documents in a collection"
        Args:
            mongo_collection: pymongo Collection object
        
        Returns:
            list of all documents
        """
        doc_list = []
        if mongo_collection is None:
            return doc_list
        for doc in mongo_collection.find():
            doc_list.append(doc)
        return doc_list
