#!/usr/bin/env python3
""" reads data from document """


def schools_by_topic(mongo_collection, topic):
    """ return a list of schools having a specific topic
    Args:
        mongo_collection: pymongo collection object
        topic(string): topic to match
    """
    match_list = mongo_collection.find({"topics": topic})
    return match_list
