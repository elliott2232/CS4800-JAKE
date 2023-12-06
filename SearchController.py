from Article import *
from pymongo import MongoClient



class SearchController:

    def __init__(self):
        self.__article_list = []
        
        
        
        
        
        
    #Searches through all articles in database
    def search_all_button(self, query):
        
        self.__article_list.clear()
        
        #Collects articles from Computer Science, search_collection() does query comparisons
        list1 = self.search_collection("mongodb+srv://Allan123:School123@cluster0.gqdysfd.mongodb.net/Articles?retryWrites=true&w=majority", "Articles", "Computer Science", query)          
        for item in range(len(list1)):
            list1[item].set_is_computer_science(True)
            self.__article_list.append(list1[item])
        
        #Collects articles from Math, search_collection() does query comparisons
        list2 = self.search_collection("mongodb+srv://Allan123:School123@cluster0.gqdysfd.mongodb.net/Articles?retryWrites=true&w=majority", "Articles", "Math", query) 
        for item in range(len(list2)):
            list2[item].set_is_math(True)
            self.__article_list.append(list2[item])       
        
        
        
        self.sort_by_relevancy()
        
        return self.get_article_list()
        #self.print_list()
        
            
            
    
    
    
    
    
    #Function used to find matches between query and title/keywords
    def intersection(self, lst1, lst2):
        return [value for value in lst1 if value in lst2]
    
    
    
    
    
    
    
    #Function to connect to database
    def search_collection(self, uri, db_name, collection_name, query):
    
            #Connection block
            client = MongoClient(uri)
            database = client[db_name]
            collection = database[collection_name]
            

            search_query = query.split()
            article_list = []
          
            results = collection.find()
            for result in results:
                article = Article()
                article.set_id(result.get("_id"))
                article.set_title(result.get("title"))
                article.set_isPartOf(result.get("isPartOf"))
                article.set_publicationYear(result.get("publicationYear"))
                article.set_url(result.get("url"))
                article.set_creator(result.get("creator"))
                article.set_publisher(result.get("publisher"))
                article.set_keyphrase(result.get("keyphrase"))

                
                #Comparing query and article title/keywords
                keyphrase_intersection = self.intersection(search_query, article.get_keyphrase())
                title_intersection = self.intersection(search_query, article.get_split_title())
                pd_intersection = self.intersection(keyphrase_intersection, title_intersection)
                
                total_match = (len(keyphrase_intersection) + len(title_intersection) - len(pd_intersection))
                if (total_match > 0):
                
                    article.set_queryMatch(total_match)
                    article_list.append(article)
                    
            return article_list
        






    #Function to return and print all aricles in computer science collection
    def show_all_computer_science_button(self):
        client = MongoClient("mongodb+srv://Allan123:School123@cluster0.gqdysfd.mongodb.net/Articles?retryWrites=true&w=majority")
        database = client["Articles"]
        collection = database["Computer Science"]
        
        self.__article_list.clear()
        article_list = []
        
        results = collection.find()
        for result in results:
            article = Article()
            article.set_id(result.get("_id"))
            article.set_title(result.get("title"))
            article.set_isPartOf(result.get("isPartOf"))
            article.set_publicationYear(result.get("publicationYear"))
            article.set_url(result.get("url"))
            article.set_creator(result.get("creator"))
            article.set_publisher(result.get("publisher"))
            article.set_keyphrase(result.get("keyphrase"))
            self.__article_list.append(article)

        self.print_list()    

            






    #Function to return and print all aricles in math collection
    def show_all_math_button(self):
        client = MongoClient("mongodb+srv://Allan123:School123@cluster0.gqdysfd.mongodb.net/Articles?retryWrites=true&w=majority")
        database = client["Articles"]
        collection = database["Math"]
        
        self.__article_list.clear()
        article_list = []
        
        results = collection.find()
        for result in results:
            article = Article()
            article.set_id(result.get("_id"))
            article.set_title(result.get("title"))
            article.set_isPartOf(result.get("isPartOf"))
            article.set_publicationYear(result.get("publicationYear"))
            article.set_url(result.get("url"))
            article.set_creator(result.get("creator"))
            article.set_publisher(result.get("publisher"))
            article.set_keyphrase(result.get("keyphrase"))
            article.set_is_math(True)
            self.__article_list.append(article)

        self.print_list()     


            
            
     


     
            
    #Function to sort list by date
    def sort_by_date_button(self):
        self.__article_list.sort(key = lambda article: article.get_publicationYear(), reverse = True)
        self.get_article_list()
    
    
    
    #Function to sort list by relevancy
    def sort_by_relevancy_button(self):
        self.__article_list.sort(key = lambda article: article.get_queryMatch(), reverse = True)
        self.get_article_list()
        
   
   #Function to sort list by relevancy
    def sort_by_relevancy(self):
        self.__article_list.sort(key = lambda article: article.get_queryMatch(), reverse = True)
      
    
    
    
    #Prints list with matching results
    def print_list(self):
        for article in range(len(self.__article_list)):
            print(self.__article_list[article])
            
            #Use to te visibly test and compare query, title, and keyword
            #print(self.__article_list[article].get_keyphrase())
            
            
            #For testing
            '''
            if article == 25:
                break
            '''
    
    
    def filter_computer_science():
        pass
    
    
    def get_article_list(self):
        return self.__article_list
        
        
    
    
    
    
    
    
    
    
   
    