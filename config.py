# Configuration settings for the MongoDB client
import os

def get_config():
    uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    dbname = os.getenv("MONGO_DBNAME", "test")
    return uri, dbname
