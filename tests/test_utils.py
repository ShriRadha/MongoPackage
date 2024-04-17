import unittest
from source.utils import convert_to_bson, parse_datetime_from_string, validate_document_schema

class TestUtils(unittest.TestCase):
    def test_convert_to_bson(self):
        # This is a simple representation test
        data = {"name": "John Doe", "age": 30}
        bson_data = convert_to_bson(data)
        self.assertTrue(bson_data)

    def test_parse_datetime_from_string(self):
        date_string = "2021-01-01 12:00:00"
        result = parse_datetime_from_string(date_string)
        self.assertEqual(result.year, 2021)
        self.assertEqual(result.month, 1)
        self.assertEqual(result.day, 1)

    def test_validate_document_schema(self):
        document = {"name": "John Doe", "age": 30}
        self.assertTrue(validate_document_schema(document, ["name", "age"]))
        with self.assertRaises(KeyError):
            validate_document_schema(document, ["name", "age", "address"])

