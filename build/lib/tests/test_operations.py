import unittest
from unittest.mock import MagicMock
from source.operations import MongoDBOperations

class TestMongoDBOperations(unittest.TestCase):
    def setUp(self):
        self.mock_client = MagicMock()
        self.ops = MongoDBOperations("mongodb://localhost:27017", "testdb")
        self.ops.db = MagicMock()

    def test_insert_document(self):
        # Setup
        self.ops.db['test_collection'].insert_one = MagicMock(return_value=MagicMock(inserted_id=1))

        # Action
        result = self.ops.insert_document('test_collection', {'name': 'John Doe'})

        # Assert
        self.assertEqual(result, 1)
    

    def test_find_documents(self):
        # Setup
        expected_documents = [{'name': 'John Doe'}]
        self.ops.db['test_collection'].find = MagicMock(return_value=expected_documents)

        # Action
        result = self.ops.find_documents('test_collection', {})

        # Assert
        self.assertEqual(result, expected_documents)

    def test_update_documents(self):
        # Setup
        self.ops.db['test_collection'].update_many = MagicMock(return_value=MagicMock(modified_count=1))

        # Action
        result = self.ops.update_documents('test_collection', {'name': 'John Doe'}, {'age': 30})

        # Assert
        self.assertEqual(result, 1)

    def test_delete_documents(self):
        # Setup
        self.ops.db['test_collection'].delete_many = MagicMock(return_value=MagicMock(deleted_count=1))

        # Action
        result = self.ops.delete_documents('test_collection', {'name': 'John Doe'})

        # Assert
        self.assertEqual(result, 1)
