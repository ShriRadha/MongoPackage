from pymongo import MongoClient as PymongoClient
import logging
from .logger import configure_logger

class MongoClient:
    """
    This class handles the connection to a MongoDB database. It provides methods to connect to
    and disconnect from a MongoDB instance, as well as to access the database directly.

    Attributes:
        uri (str): MongoDB URI string used to connect to the database.
        client (MongoClient): A PyMongo MongoClient object. This is the actual client connection to the MongoDB.
        db (Database): The database object from PyMongo that is currently connected.
    """

    def __init__(self, uri):
        """
        Initializes the MongoClient object with a MongoDB URI.

        Args:
            uri (str): A MongoDB URI string defining how to connect to the database.
                       Example: "mongodb://localhost:27017" for connecting to a locally hosted database.
        
        This constructor sets up the logger configuration and initializes the client
        attribute but does not actually establish the database connection.
        """
        configure_logger()  # Set up the logging configurations for this instance
        self.uri = uri
        self.client = None
        self.db = None

    def connect(self, dbname):
        """
        Establishes a connection to a MongoDB database specified by the dbname argument.

        Args:
            dbname (str): The name of the database to connect to.

        Raises:
            Exception: Propagates any exceptions raised by PyMongo's MongoClient, typically related
                       to issues in connecting to the database (e.g., network issues).

        Upon a successful connection, the method logs this event and the database object is stored
        in the `db` attribute. If the connection fails, an error is logged and the exception is raised.
        """
        try:
            self.client = PymongoClient(self.uri)  # Attempt to create a client connection
            self.db = self.client[dbname]  # Access the specific database
            logging.info(f"Connected to MongoDB database: {dbname} at {self.uri}")
        except Exception as e:
            logging.error(f"Failed to connect to MongoDB database: {dbname} at {self.uri} - {str(e)}")
            raise  # Re-raise the caught exception to handle it further up the call stack

    def get_database(self):
        """
        Retrieves the database object to which the client is currently connected.

        Returns:
            pymongo.database.Database: The database object currently connected to. This object
                                       allows performing database operations (insert, read, etc.).

        This method can be used to perform direct operations on the database object if required.
        """
        return self.db

    def close(self):
        """
        Closes the connection to the MongoDB database if it is open.

        This method safely closes the connection to the MongoDB if it is active and logs this event.
        It's crucial to close the connection to release resources and avoid potential memory leaks.
        """
        if self.client:
            self.client.close()  # Close the MongoDB connection
            logging.info("MongoDB connection closed.")
