from pymongo import MongoClient as PymongoClient
import logging
from source.logger import configure_logger

class MongoClient:
    """
    This class manages the connection to the MongoDB database.
    It is designed to handle the connection logistics and to provide a MongoClient object.
    """
    def __init__(self, uri):
        """
        Initializes the MongoClient object with a MongoDB URI.
        """
        configure_logger()  # Setting up logging configurations
        self.uri = uri
        self.client = None

    def connect(self, dbname):
        """
        Connects to a MongoDB database specified by the dbname argument.
        This method initializes the database client and selects the database.
        """
        try:
            self.client = PymongoClient(self.uri)
            self.db = self.client[dbname]
            logging.info(f"Connected to MongoDB database: {dbname} at {self.uri}")
        except Exception as e:
            logging.error(f"Failed to connect to MongoDB database: {dbname} at {self.uri} - {str(e)}")
            raise

    def get_database(self):
        """
        Returns the database object to which the client is currently connected.
        This method can be used to perform operations directly using the database object if required.
        """
        return self.db

    def close(self):
        """
        Closes the connection to the MongoDB database.
        """
        if self.client:
            self.client.close()
            logging.info("MongoDB connection closed.")
