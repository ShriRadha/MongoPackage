import unittest
from unittest.mock import patch, MagicMock
from source.client import MongoClient

class TestMongoClient(unittest.TestCase):
    @patch("client.PymongoClient")
    def test_connect(self, mock_mongo_client):
        # Setup
        mock_client_instance = MagicMock()
        mock_mongo_client.return_value = mock_client_instance
        mock_client_instance.__getitem__.return_value = MagicMock()

        # Action
        client = MongoClient("mongodb://localhost:27017")
        client.connect("testdb")

        # Assert
        mock_mongo_client.assert_called_with("mongodb://localhost:27017")
        self.assertTrue(mock_client_instance.__getitem__.called)
        self.assertEqual(client.db, mock_client_instance.__getitem__.return_value)

    def test_close(self):
        # Setup
        client = MongoClient("mongodb://localhost:27017")
        client.client = MagicMock()

        # Action
        client.close()

        # Assert
        client.client.close.assert_called_once()

