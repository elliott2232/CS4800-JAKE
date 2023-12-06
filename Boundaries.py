from SearchController import *
from Article import *



class Boundaries:
    

    def __init__(self):
        
        self.search_controller = SearchController()
    
    
    
    
    
    
    def search_all_button(self, query):
        self.search_controller.search_all(query)
        

    def search_math_button(self):
        self.search_controller.search_math()
        
        
    def search_computer_science_button(self):
        self.search_controller.search_computer_science()
        
    
    def login_signup_button(self):
        pass
        
        
    def favorite_button(self):
        pass
        
        
    def view_favorites_button(self):
        pass
        
        
    def sort_by_date_button(self):
        self.search_controller.sort_by_date()
        
        
    def sort_by_relevancy_button(self):
        self.search_controller.sort_by_relevancy()
    
    