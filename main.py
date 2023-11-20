from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from Article import * 
from Interface import *
from SearchController import *


def main_interface(): 
  
  interface = Interface()
  interface.search_button("Infrastructure")
  

 
    
if __name__ == "__main__":
    main_interface()
