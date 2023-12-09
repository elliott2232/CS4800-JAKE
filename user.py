#written by: Elliot Lewis
#Tested by: Elliot Lewis
#Debugged by: Elliot Lewis

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from Article import * 
from SearchController import *
from hashlib import sha256

class UserObject:
    def __init__(self, email, first_name, last_name, password, favorites=None, **kwargs): 
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = self._hash_password(password)
        self.favorite = favorites or [] #Joey

    @staticmethod
    def _hash_password(password): 
        # Hash the password using SHA-256
        return sha256(password.encode()).hexdigest()
        
    def to_dict(self):
        return {
            "email": self.email,
            "First name": self.first_name, 
            "Last name": self.last_name,
            "password": self.password,  # Use the hashed password directly
            "favorites": self.favorite #Joey
        }
    
    def add_favorite(self, article_title): #Joey
        if article_title not in self.favorite:
            self.favorite.append(article_title)

    def remove_favorite(self, article_title): #Joey
        if article_title in self.favorite:
            self.favorite.remove(article_title)