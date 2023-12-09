#written by: Allan Tornero
#Tested by: Allan Tornero
#Debugged by: Allan Tornero

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
                print("Computer Science: " + str(results[result].get_is_computer_science()))
                print("Math: " + str(results[result].get_is_math()))
                print("Biology: " + str(results[result].get_is_biology()))
                print("Physics: " + str(results[result].get_is_physics()))
                print("History: " + str(results[result].get_is_history()))
                print("English: " + str(results[result].get_is_english()))
                print()
                
                
                
  user_input = input("Do you want to filter by english? ")
  if (user_input == 'Y'):
  
        for result in range(len(results)):
            
            if (results[result].get_is_english() == True):
                print(results[result])
                print("Computer Science: " + str(results[result].get_is_computer_science()))
                print("Math: " + str(results[result].get_is_math()))
                print("Biology: " + str(results[result].get_is_biology()))
                print("Physics: " + str(results[result].get_is_physics()))
                print("History: " + str(results[result].get_is_history()))
                print("English: " + str(results[result].get_is_english()))
                print()
                
                
                
  user_input = input("Do you want to filter by history? ")
  if (user_input == 'Y'):
  
        for result in range(len(results)):
            
            if (results[result].get_is_history() == True):
                print(results[result])
                print("Computer Science: " + str(results[result].get_is_computer_science()))
                print("Math: " + str(results[result].get_is_math()))
                print("Biology: " + str(results[result].get_is_biology()))
                print("Physics: " + str(results[result].get_is_physics()))
                print("History: " + str(results[result].get_is_history()))
                print("English: " + str(results[result].get_is_english()))
                print()
            
            
  user_input = input("Do you want to filter by biology? ")
  if (user_input == 'Y'):
  
        for result in range(len(results)):
            
            if (results[result].get_is_biology() == True):
                print(results[result])
                print("Computer Science: " + str(results[result].get_is_computer_science()))
                print("Math: " + str(results[result].get_is_math()))
                print("Biology: " + str(results[result].get_is_biology()))
                print("Physics: " + str(results[result].get_is_physics()))
                print("History: " + str(results[result].get_is_history()))
                print("English: " + str(results[result].get_is_english()))
                print()
                
                
  user_input = input("Do you want to filter by physics? ")
  if (user_input == 'Y'):
  
        for result in range(len(results)):
            
            if (results[result].get_is_physics() == True):
                print(results[result])
                print("Computer Science: " + str(results[result].get_is_computer_science()))
                print("Math: " + str(results[result].get_is_math()))
                print("Biology: " + str(results[result].get_is_biology()))
                print("Physics: " + str(results[result].get_is_physics()))
                print("History: " + str(results[result].get_is_history()))
                print("English: " + str(results[result].get_is_english()))
                print()
                
                
  
  results = search_controller.sort_by_date_button()
  for result in range(len(results)):
        print(results[result])
 


 

   
if __name__ == "__main__":
    test_main()