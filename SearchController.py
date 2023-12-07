from Article import *
from pymongo import MongoClient


#Allan Tornero 
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


        #Collects articles from Math, search_collection() does query comparisons
        list3 = self.search_collection("mongodb+srv://Allan123:School123@cluster0.gqdysfd.mongodb.net/Articles?retryWrites=true&w=majority", "Articles", "Biology", query) 
        for item in range(len(list3)):
            list3[item].set_is_biology(True)
            self.__article_list.append(list3[item])       


        #Collects articles from Math, search_collection() does query comparisons
        list4 = self.search_collection("mongodb+srv://Allan123:School123@cluster0.gqdysfd.mongodb.net/Articles?retryWrites=true&w=majority", "Articles", "English", query) 
        for item in range(len(list4)):
            list4[item].set_is_english(True)
            self.__article_list.append(list4[item])       


        #Collects articles from Math, search_collection() does query comparisons
        list5 = self.search_collection("mongodb+srv://Allan123:School123@cluster0.gqdysfd.mongodb.net/Articles?retryWrites=true&w=majority", "Articles", "Physics", query) 
        for item in range(len(list5)):
            list5[item].set_is_physics(True)
            self.__article_list.append(list5[item])

 #Collects articles from Math, search_collection() does query comparisons
        list6 = self.search_collection("mongodb+srv://Allan123:School123@cluster0.gqdysfd.mongodb.net/Articles?retryWrites=true&w=majority", "Articles", "History", query) 
        for item in range(len(list6)):
            list6[item].set_is_physics(True)
            self.__article_list.append(list6[item])                  
        
        
        
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
            article.set_is_computer_science(True)
            self.__article_list.append(article)

        return self.get_article_list()    

            

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

        return self.get_article_list()     


    def show_all_history_button(self):
        client = MongoClient("mongodb+srv://Allan123:School123@cluster0.gqdysfd.mongodb.net/Articles?retryWrites=true&w=majority")
        database = client["Articles"]
        collection = database["History"]
        
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
            article.set_is_history(True)
            self.__article_list.append(article)

        return self.get_article_list()
    

    def show_all_physics_button(self):
        client = MongoClient("mongodb+srv://Allan123:School123@cluster0.gqdysfd.mongodb.net/Articles?retryWrites=true&w=majority")
        database = client["Articles"]
        collection = database["Physics"]
        
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
            article.set_is_physics(True)
            self.__article_list.append(article)

        return self.get_article_list()     


    def show_all_english_button(self):
        client = MongoClient("mongodb+srv://Allan123:School123@cluster0.gqdysfd.mongodb.net/Articles?retryWrites=true&w=majority")
        database = client["Articles"]
        collection = database["Physics"]
        
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
            article.set_is_english(True)
            self.__article_list.append(article)

        return self.get_article_list()
    
    
    def show_all_biology_button(self):
        client = MongoClient("mongodb+srv://Allan123:School123@cluster0.gqdysfd.mongodb.net/Articles?retryWrites=true&w=majority")
        database = client["Articles"]
        collection = database["Physics"]
        
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
            article.set_is_biology(True)
            self.__article_list.append(article)

        return self.get_article_list()
    
            
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
    
    
    def get_article_list(self):
        return self.__article_list
        