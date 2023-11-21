""""
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Assuming Article is defined somewhere
# from your_module import Article

class SearchController:

    def __init__(self):
        self.__article_list = []
        self.__query = None

    def set_query(self, query):
        self.__query = query

    def get_query(self):
        return self.__query

    def search(self, search):
        self.__query = search

        # Connect to database
        client = MongoClient("mongodb+srv://Allan123:School123@cluster0.gqdysfd.mongodb.net/Articles?retryWrites=true&w=majority")
        database = client["Articles"]
        first_collection = database["Computer Science"]
        second_collection = database["Math"]

        # ... Your search logic ...

        # Sort articles
        self.__article_list.sort(key=lambda article: article.get_queryMatch(), reverse=True)

        # Print articles
        for article in self.__article_list:
            print(article.get_title())
            print(article.get_keyphrase())
            print(article.get_url())
            print()

def intersection(lst1, lst2):
    return [value for value in lst1 if value in lst2]



    IN PROGRESS NOT COMPLETED
"""