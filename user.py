from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from Article import * 
from Boundaries import *
from SearchController import *
import hashlib

#Joey - this is the user object file

class User:
    def __init__(self, email, first_name, last_name, password, favorite=None): 
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = self._hash_password(password)
        self.favorite = [favorite] if favorite else [] 
        #favorites are complicated. when a user is registered, they may not have 
        #any favs, so there needs to be a way to store all favs in a list, but also
        #have an option for none to be stored. this solves this issue

    def _hash_password(self, password): 
        # Hash the password using SHA-256 - taken from main.py
            return hashlib.sha256(password.encode()).hexdigest()
        
    def to_dict(self):
            return {
                "email": self.email,
                "First name": self.first_name,
                "Last name": self.last_name,
                "Password": self._hash_password(self.password), #looks complicated, just hashing the pw
                "Favorites": self.favorite
            }