import urllib.parse

class Article:

    def __init__(self):
        self.__id = ""
        self.__title = ""
        self.__split_title = []
        self.__isPartOf = ""
        self.__publicationYear = 0
        self.__url = ""
        self.__creator = ""
        self.__publisher = ""
        self.__keyphrase = []
        self.__queryMatch = 0
        self.__is_computer_science = False
        self.__is_math = False
        self.__is_biology = False
        self.__is_english = False
        self.__is_physics = False
        self.__is_history = False
        


    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id



    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = str(title)
        # Update __split_title when setting the title
        self.__split_title = self.__title.split()

    def get_split_title(self):
        return self.__split_title



    def get_isPartOf(self):
        return self.__isPartOf

    def set_isPartOf(self, isPartOf):
        self.__isPartOf = isPartOf



    def get_publicationYear(self):
        return self.__publicationYear

    def set_publicationYear(self, publicationYear):
        self.__publicationYear = publicationYear



    def get_url(self):
        return self.__url

    def set_url(self, url):
        if url == None:
            self.__url = "ERROR: URL NOT FOUND"
        else:
            self.__url = url



    def get_creator(self):
        return self.__creator

    def set_creator(self, creator):
        if creator == None:
            self.__creator = "ERROR: CREATOR NOT FOUND"
        else:
            self.__creator = creator



    def get_publisher(self):
        return self.__publisher

    def set_publisher(self, publisher):
        self.__publisher = publisher



    def get_keyphrase(self):
        return self.__keyphrase

    def set_keyphrase(self, keyphrase):
        # Handle cases where keyphrase is None
        if keyphrase == None:
            self.__keyphrase = []
        else:
            # Split keywords and remove ";" character
            split_keywords = str(keyphrase).split()
            for keyword in range(len(split_keywords)):
                split_keywords[keyword] = split_keywords[keyword].replace(";", "")
            self.__keyphrase = split_keywords



    def set_queryMatch(self, queryMatch):
        self.__queryMatch = queryMatch
        
    def get_queryMatch(self):
        return self.__queryMatch
        
        
        
    def set_is_computer_science(self, bool):
        self.__is_computer_science = bool
    
    def get_is_computer_science(self):
        return self.__is_computer_science    
    
    

    def set_is_math(self, bool):
        self.__is_math = bool
    
    def get_is_math(self):
        return self.__is_math   
    
    
    def set_is_biology(self, bool):
        self.__is_biology = bool
    
    def get_is_biology(self):
        return self.__is_biology  
        
        
    def set_is_physics(self, bool):
        self.__is_physics = bool
    
    def get_is_physics(self):
        return self.__is_physics   
        
        
    def set_is_english(self, bool):
        self.__is_english = bool
    
    def get_is_english(self):
        return self.__is_english   

    
    def set_is_history(self, bool):
        self.__is_history = bool
        
    def set_is_history(self, bool):
        return self.__is_history

   
        
        

    def __str__(self):
        line =  "Title: " + self.get_title() + "\n" + "Author: " + self.get_creator() + "\n" + "Date published: " + str(self.get_publicationYear()) + "\n" + "URL: " + self.get_url() + "\n" + "\n"
        return line

