import bson
from datetime import datetime

def convert_to_bson(obj):
    """
    Converts a given Python dictionary into a BSON format which is used by MongoDB.
    Useful for ensuring the data format is compatible with MongoDB's requirements.
    """
    try:
        return bson.BSON.encode(obj)
    except Exception as e:
        raise ValueError(f"Error converting to BSON: {str(e)}")

def parse_datetime_from_string(date_string, date_format="%Y-%m-%d %H:%M:%S"):
    """
    Converts a date string into a Python datetime object based on the specified format.
    This is useful for converting date strings from user input into datetime objects that MongoDB can store.
    """
    try:
        return datetime.strptime(date_string, date_format)
    except ValueError as e:
        raise ValueError(f"Invalid date format: {str(e)}")

def validate_document_schema(document, required_keys):
    """
    Validates that a given document (dict) includes all required keys.
    This can be used to prevent insertion of invalid documents into the database.
    """
    missing_keys = [key for key in required_keys if key not in document]
    if missing_keys:
        raise KeyError(f"Missing keys in document: {', '.join(missing_keys)}")
    return True

def log_operation_details(operation_type, details):
    """
    Generic utility to log details of various operations, customizable for different use cases.
    This function can be enhanced to include more sophisticated logging based on needs.
    """
    print(f"Operation: {operation_type}, Details: {details}")  # Placeholder for actual logging
