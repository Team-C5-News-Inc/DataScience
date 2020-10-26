import pymongo

client = pymongo.MongoClient("mongodb+srv://OscarProject:Node12345@cluster0.33nuz.gcp.mongodb.net/news_inc?retryWrites=true&w=majority")
db = client.test