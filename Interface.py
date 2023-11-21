<<<<<<< HEAD
from Article import *
from SearchController import *



class Interface:
    def search_button(click, query):
        if click:
            search_controller = SearchController()
            search_controller.search(query)
    
    def view_article_button(click):
        pass
        
    def login_button(click):
        pass
        
    def create_account_button(click):
        pass
        
    def favorite_button(click):
        pass
        
    def view_favorites_button(click):
        pass
        
=======
from SearchController import *



class Interface:



    @staticmethod
    def search_button(query):
        search_controller = SearchController()
        print(search_controller.search(query))
        
    
    def view_article_button(click):
        pass
        
    def login_button(click):
        pass
        
    def create_account_button(click):
        pass
        
    def favorite_button(click):
        pass
        
    def view_favorites_button(click):
        pass
        
>>>>>>> 46fd5b0d524256e3e87c05bdae7bcf18bae253d2
    