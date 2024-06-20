#!/usr/bin/python3
""" function to update fields in a document """


if __name__ == "__main__":
    def update_topics(mongo_collection, name, topics):
        """ changes all topics in a document based on the name
        Args:
            mongo_collection: pymongo collection object
            name(string): school name to update
            topics(list): list of topics approached in school
        """
        mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
        