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
        
    