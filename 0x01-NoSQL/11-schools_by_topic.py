 #!/usr/bin/env python3
 """ reads data from document """

    if __name__ == "__main__":
    def schools_by_topic(mongo_collection, topic):
        """ return a list of schools having a specific topic
        Args: 
            mongo_collection: pymongo collection object
            topic(string): topic to match
        """
        match_list = mongo_collection.find({"topics": topic})
        for doc in match_list:
