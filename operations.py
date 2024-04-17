from source.client import MongoClient
import logging

class MongoDBOperations:
    def __init__(self, uri, dbname):
        self.client = MongoClient(uri)
        self.client.connect(dbname)
        self.db = self.client.db

    def insert_document(self, collection_name, document):
        """Insert a single document into a collection."""
        try:
            result = self.db[collection_name].insert_one(document)
            logging.info(f"Inserted document with id {result.inserted_id} into collection {collection_name}")
            return result.inserted_id
        except Exception as e:
            logging.error(f"Failed to insert document into {collection_name}: {str(e)}")
            raise

    def find_documents(self, collection_name, query):
        """Find documents matching a query."""
        try:
            results = self.db[collection_name].find(query)
            documents = [doc for doc in results]
            logging.info(f"Found {len(documents)} documents in {collection_name} matching {query}")
            return documents
        except Exception as e:
            logging.error(f"Failed to find documents in {collection_name}: {str(e)}")
            raise

    def update_documents(self, collection_name, query, new_values):
        """Update documents matching a query with new values."""
        try:
            result = self.db[collection_name].update_many(query, {'$set': new_values})
            logging.info(f"Updated {result.modified_count} documents in {collection_name}")
            return result.modified_count
        except Exception as e:
            logging.error(f"Failed to update documents in {collection_name}: {str(e)}")
            raise

    def delete_documents(self, collection_name, query):
        """Delete documents matching a query."""
        try:
            result = self.db[collection_name].delete_many(query)
            logging.info(f"Deleted {result.deleted_count} documents from {collection_name}")
            return result.deleted_count
        except Exception as e:
            logging.error(f"Failed to delete documents from {collection_name}: {str(e)}")
            raise

    def close_connection(self):
        """Close the MongoDB connection."""
        try:
            self.client.close()
            logging.info("MongoDB connection closed.")
        except Exception as e:
            logging.error(f"Failed to close MongoDB connection: {str(e)}")
            raise
