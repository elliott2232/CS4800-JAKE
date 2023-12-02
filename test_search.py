from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from Article import *
from Boundaries import *




def test_main():

    boundaries = Boundaries()
    
    #boundaries.search_all_button(input("Enter search: "))
    
    boundaries.search_math()
   
   
if __name__ == "__main__":
    test_main()
