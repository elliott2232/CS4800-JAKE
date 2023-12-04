from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from Article import *
from Boundaries import *




def test_main():

    boundaries = Boundaries()
    
    boundaries.search_all_button(input("Enter search: "))
    #boundaries.search_math_button()
    #boundaries.search_computer_science_button()
    
    if input() == "y":
        boundaries.sort_by_date_button()
        #boundaries.sort_by_relevancy_button()
        
    
   
if __name__ == "__main__":
    test_main()
