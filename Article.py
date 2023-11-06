
class Article:

  def __init__(self):
    self.__id = ""
    self.__title = ""
    self.__split_title = self.__title.split()
    self.__isPartOf = ""
    self.__publicationYear = 0
    self.__url = ""
    self.__creator = ""
    self.__publisher = ""
    self.__keyphrase = []


  
  def get_id(self):
    return self.__id

  def set_id(self, id):
    self.__id = id

  def get_title(self):
    return self.__title

  def set_title(self, title):
    self.__title = title

  
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
    self.__url = url

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
    
    #accounts for entries that have no keyphrase field
    if keyphrase == None:
        self.__keyphrase = "None"
    #splits keywords and removes ";" character
    else:
        split_keywords = keyphrase.split()
        for keyword in range(len(split_keywords)):
            if ";" in split_keywords[keyword]:
                split_keywords[keyword] = split_keywords[keyword].replace(";", "")
        self.__keyphrase = split_keywords


  #NOT FUNCTIONING
  def __str__(self):

            line = "ID: " + str(self.get_id()) + "\n Title: " + self.get_title() + "\n isPartOf: " + self.get_isPartOf()  + "\n Publication Year: " + str(self.get_publicationYear()) + "\n URL: " + self.get_url() + "\n Creator: " + self.get_creator() + "\n Publisher: " + self.get_publisher() + "\n Keyphrase: " + self.get_keyphrase()

            print()
            print()
          
            return line
















