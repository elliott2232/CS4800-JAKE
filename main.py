
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from Article import *




cluster = "mongodb+srv://Allan123:School123@cluster0.gqdysfd.mongodb.net/Articles?retryWrites=true&w=majority"
def connect_to_cluster(cluster):


    # Create a new client and connect to the server
    client = MongoClient(cluster, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        #print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)







def search():

    #Connect to cluster, database, and collection
    newClient = MongoClient(cluster)
    database = newClient["Articles"]
    collection = database["Computer Science"]
    collection2 = database["Math"]

    
    #Takes the user's search query
    searchQuery = input("Search: ")
    split_query = searchQuery.split()
    

    #pulls all entries from database
    results = collection.find()
    
    
    
    for result in results:
    
        #Creates an article object for every result
        article = Article()
        
        article.set_id(result.get("_id"))
        article.set_title(result.get("title"))
        article.set_isPartOf(result.get("isPartOf"))
        article.set_publicationYear(result.get("publicationYear"))
        article.set_url(result.get("url"))
        article.set_creator(result.get("creator"))
        article.set_publisher(result.get("publisher"))
        article.set_keyphrase(result.get("keyphrase"))
        
        
        #Checks if split query words are in article keyphrases, or if none checks article titles
        if len(intersection(split_query, article.get_keyphrase())) > 0 or len(intersection(split_query, article.get_split_title())) > 0:
            print(article.get_title())
            print(article.get_keyphrase())
            print()
            print()
          
       
       
       
       
       
       
    '''  POOR SOLUTION FOR SEARCHING OTHER COLLECTION, DON'T RECOMMEND WE USE
    results2 = collection2.find()
    for result2 in results2:
    
        #Creates an article object for every result
        article = Article()
        
        article.set_id(result2.get("_id"))
        article.set_title(result2.get("title"))
        article.set_isPartOf(result2.get("isPartOf"))
        article.set_publicationYear(result2.get("publicationYear"))
        article.set_url(result2.get("url"))
        article.set_creator(result2.get("creator"))
        article.set_publisher(result2.get("publisher"))
        article.set_keyphrase(result2.get("keyphrase"))
        
        
        #Checks if split query words are in article keyphrases, or if none checks article titles
        if len(intersection(split_query, article.get_keyphrase())) > 0 or len(intersection(split_query, article.get_split_title())) > 0:
            print(article.get_title())
            print(article.get_keyphrase())
            print()
            print()   
    '''   
        
             




             
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3       
        
        
        
 



#//////////////////////////main////////////////////////////
search()














