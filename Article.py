import urllib.parse
import urllib.request


class Article:

    def __init__(self):
        self.__id = ""
        self.__title = ""
        self.__split_title = None
        self.__isPartOf = ""
        self.__publicationYear = 0
        self.__url = None
        self.__creator = ""
        self.__publisher = ""
        self.__keyphrase = []
        self.__queryMatch = 0
        self.__view_bool = False




    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title
        # Update __split_title when setting the title
        self.__split_title = title.split()

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

    def get_hyperlinked_url(self):
        return f'<a href="{self.__url}" target="_blank">{self.__title}</a>'

    def set_url(self, url):
        self.__url = urllib.parse.quote(str(url))

    def get_creator(self):
        return self.__creator

    def set_creator(self, creator):
        self.__creator = creator

    def get_publisher(self):
        return self.__publisher

    def set_publisher(self, publisher):
        self.__publisher = publisher

    def get_keyphrase(self):
        return self.__keyphrase

    def set_keyphrase(self, keyphrase):
        # Handle cases where keyphrase is None
        if keyphrase is None:
            self.__keyphrase = []
        else:
            # Split keywords and remove ";" character
            split_keywords = keyphrase.split()
            for word in range(len(split_keywords)):
                split_keywords[word] = split_keywords[word].replace(";", "")
            self.__keyphrase = split_keywords

    def set_queryMatch(self, queryMatch):
        self.__queryMatch = queryMatch
        
    def get_queryMatch(self):
        return self.__queryMatch
        
    def open_url(self):
        urllib.request.urlopen(self.__url)

