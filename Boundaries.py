#written by: Allan Tornero
#Tested by: Allan Tornero
#Debugged by: Allan Tornero

#NOTE: THIS FILE WAS NOT USED IN THE FINAL SYSTEM

from SearchController import *
from Article import *



class Boundaries:
    

    def __init__(self):
        
        self.search_controller = SearchController()
    
    
    
    
    
    
    def search_all_button(self, query):
        self.search_controller.search_all(query)
        self.search_controller.print_list()
        

    def search_math_button(self):
        self.search_controller.search_math()
        self.search_controller.print_list()
        
        
    def search_computer_science_button(self):
        self.search_controller.search_computer_science()
        self.search_controller.print_list()
        
    
    def login_signup_button(self):
        pass
        
        
    def favorite_button(self):
        pass
        
        
    def view_favorites_button(self):
        pass
        
        
    def sort_by_date_button(self):
        self.search_controller.sort_by_date()
        self.search_controller.print_list()        
        
        
    def sort_by_relevancy_button(self):
        self.search_controller.sort_by_relevancy()
        self.search_controller.print_list()    
    