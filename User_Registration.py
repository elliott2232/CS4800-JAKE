'''''
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from Article import * 
from SearchController import *
from user import User
from bson import ObjectId

import hashlib

#Elliott
class UserRegistration:
    def __init__(self, mongodb_uri, database_name, collection_name):
        self.client = MongoClient(mongodb_uri)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def get_user_by_id(self, user_id):
        try:
            # Convert the user_id string to ObjectId
            user_id = ObjectId(user_id)

            # Search for the user in the collection
            user_data = self.collection.find_one({"_id": user_id})

            if user_data:
                # Create an instance of the User class using the retrieved data
                user = User(
                    email=user_data.get("email"),
                    first_name=user_data.get("First name", ""),
                    last_name=user_data.get("Last name", ""),
                    password=user_data.get("password"),
                    favorites=user_data.get("favorites", [])
                )
                return user

        except Exception as e:
            print(f"Error getting user by ID: {e}")
            return None
        
    def update_user(self, user_id, user_data):
        try:
            user_id = ObjectId(user_id)
            self.collection.update_one({"_id": user_id}, {"$set": user_data})
            print(f"User with ID {user_id} updated successfully.")

        except Exception as e:
            print(f"Error updating user: {e}")



    def register_user(self, email, first_name, last_name, password, favorite=None): #doesnt matter favorite will not be handled on sign in, its default value is none
        try:
            user_obj = User(email, first_name, last_name, password, favorite)
            # Insert the user document into the collection
            result = self.collection.insert_one(user_obj.to_dict())

            # Print a success message
            print("User registered successfully with ID:", result.inserted_id)

        except Exception as e:
            print(f"Error registering user: {e}")
'''