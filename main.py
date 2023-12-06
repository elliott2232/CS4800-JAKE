from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from Article import * 
from Boundaries import *
from SearchController import *
from user import User
import hashlib

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
            results.append(article)

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

#Elliott
class UserRegistration:
    def __init__(self, mongodb_uri, database_name, collection_name):
        self.client = MongoClient(mongodb_uri)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]



    def register_user(self, email, first_name, last_name, password, favorite=None): #doesnt matter favorite will not be handled on sign in, its default value is none
        try:
            user_obj = User(email, first_name, last_name, password, favorite)
            # Insert the user document into the collection
            result = self.collection.insert_one(user_obj.to_dict())

            # Print a success message
            print("User registered successfully with ID:", result.inserted_id)

        except Exception as e:
            print(f"Error registering user: {e}")

        finally:
            # Close the MongoDB connection   
               #self.client.close()
               pass

class UserLogin(User):
    def __init__(self, mongodb_uri, database_name, collection_name):
        super().__init__(email="", first_name="", last_name="", password="")  # Initialize with empty values
        self.mongodb_uri = mongodb_uri
        self.database_name = database_name
        self.collection_name = collection_name

    def authenticate_user(self, email, password):
        try:
            # Hash the provided password for comparison
            hashed_password = self._hash_password(password)

            # Establish MongoDB connection
            with MongoClient(self.mongodb_uri) as client:
                db = client[self.database_name]
                collection = db[self.collection_name]

                # Search for the user in the collection
                user = collection.find_one({"email": email, "password": hashed_password})

                return user

        except Exception as e:
            print(f"Error authenticating user: {e}")
            return None
        