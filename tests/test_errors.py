import unittest
from unittest.mock import patch
from source.operations import MongoDBOperations
from source.client import MongoClient
from source.exceptions import (DatabaseConnectionError, InsertionError, DocumentNotFoundError, 
                        UpdateError, DeletionError)

class TestExceptionHandling(unittest.TestCase):
    @patch('client.PymongoClient')
    def test_database_connection_error(self, mock_connect):
        mock_connect.side_effect = DatabaseConnectionError("Failed to connect to database")
        with self.assertRaises(DatabaseConnectionError):
            ops = MongoClient("testdb")
            ops.connect("testdb")

    @patch('operations.MongoDBOperations.insert_document')
    def test_insertion_error(self, mock_insert):
        mock_insert.side_effect = InsertionError("Insertion failed")
        ops = MongoDBOperations("mongodb://localhost:27017", "testdb")
        with self.assertRaises(InsertionError):
            ops.insert_document('test_collection', {'data': 'test'})

    @patch('operations.MongoDBOperations.find_documents')
    def test_document_not_found_error(self, mock_find):
        mock_find.side_effect = DocumentNotFoundError("No documents found")
        ops = MongoDBOperations("mongodb://localhost:27017", "testdb")
        with self.assertRaises(DocumentNotFoundError):
            ops.find_documents('test_collection', {'query': 'none'})

    @patch('operations.MongoDBOperations.update_documents')
    def test_update_error(self, mock_update):
        mock_update.side_effect = UpdateError("Update failed")
        ops = MongoDBOperations("mongodb://localhost:27017", "testdb")
        with self.assertRaises(UpdateError):
            ops.update_documents('test_collection', {'name': 'test'}, {'data': 'new'})

    @patch('operations.MongoDBOperations.delete_documents')
    def test_deletion_error(self, mock_delete):
        mock_delete.side_effect = DeletionError("Deletion failed")
        ops = MongoDBOperations("mongodb://localhost:27017", "testdb")
        with self.assertRaises(DeletionError):
            ops.delete_documents('test_collection', {'name': 'test'})

