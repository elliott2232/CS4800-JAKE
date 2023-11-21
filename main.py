from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from Article import * 
from Interface import *
from SearchController import *

def connect_to_cluster(cluster_url):
    try:
        client = MongoClient(cluster_url, server_api=ServerApi('1'))
        # Send a ping to confirm a successful connection
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None

def search_articles(client, search_query, collection_name):
    database = client["Articles"]
    collection = database[collection_name]

    results = []

    for result in collection.find():
        article = Article()
        article.set_id(result.get("_id"))
        article.set_title(result.get("title"))
        article.set_isPartOf(result.get("isPartOf"))
        article.set_publicationYear(result.get("publicationYear"))
        article.set_url(result.get("url"))
        article.set_creator(result.get("creator"))
        article.set_publisher(result.get("publisher"))
        article.set_keyphrase(result.get("keyphrase"))

        if (
            len(intersection(search_query.split(), article.get_keyphrase())) > 0
            or len(intersection(search_query.split(), article.get_split_title())) > 0
        ):
            results.append(article.get_title())

    return results

def intersection(lst1, lst2):
    return [value for value in lst1 if value in lst2]

def main():
    cluster_url = "mongodb+srv://Allan123:School123@cluster0.gqdysfd.mongodb.net/Articles?retryWrites=true&w=majority"
    client = connect_to_cluster(cluster_url)

    if client:
        search_query = input("Search: ")
        
        
        # Perform searches on different collections if needed
        search_articles(client, search_query, "Computer Science")
        # search_articles(client, split_query, "Math")  # Uncomment if searching in the Math collection

 
    
if __name__ == "__main__":
    main_interface()
