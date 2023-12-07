''''
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from Article import * 
from SearchController import *
from user import User
from bson import ObjectId

import hashlib

#Elliott
class UserLogin(User):
    def __init__(self, mongodb_uri, database_name, collection_name):
        super().__init__(email="", first_name="", last_name="", password="", favorites="")  # Initialize with empty values
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
'''