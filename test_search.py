from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from Article import *
from SearchController import SearchController




def test_main():

  search_controller = SearchController()
  
  results = search_controller.search_all_button(input("Enter search: "))
  
  for result in range(len(results)):
        print(results[result])
       
  
  user_input = input("Do you want to filter by computer science? ")
  if (user_input == 'Y'):
  
        for result in range(len(results)):
            
            if (results[result].get_is_computer_science() == True):
                print(results[result])
                print(results[result].get_is_computer_science())
                print()
                
                
                
        user_input = input("Do you want to filter by english? ")
  if (user_input == 'Y'):
  
        for result in range(len(results)):
            
            if (results[result].get_is_english() == True):
                print(results[result])
                print(results[result].get_is_english())
                print()
                
                
                
        user_input = input("Do you want to filter by history? ")
  if (user_input == 'Y'):
  
        for result in range(len(results)):
            
            if (results[result].get_is_history() == True):
                print(results[result])
                print(results[result].get_is_history())
                print()
            
            
        user_input = input("Do you want to filter by biology? ")
  if (user_input == 'Y'):
  
        for result in range(len(results)):
            
            if (results[result].get_is_biology() == True):
                print(results[result])
                print(results[result].get_is_biology())
                print()
                
                
        user_input = input("Do you want to filter by physics? ")
  if (user_input == 'Y'):
  
        for result in range(len(results)):
            
            if (results[result].get_is_physics() == True):
                print(results[result])
                print(results[result].get_is_physics())
                print()
                
                

   
if __name__ == "__main__":
    test_main()