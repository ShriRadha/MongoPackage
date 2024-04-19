import bson
from datetime import datetime  # Import datetime to work with date and time data.

def convert_to_bson(obj):
    """
    Converts a given Python dictionary into a BSON format which is used by MongoDB.
    This is essential for ensuring the data format is compatible with MongoDB's requirements.

    Args:
        obj (dict): A Python dictionary to be converted into BSON format.

    Returns:
        The BSON formatted data.

    Raises:
        ValueError: If the object cannot be encoded into BSON due to incompatible format.
    """
    try:
        bson_data = bson.BSON.encode(obj)
        return bson_data
    except Exception as e:
        raise ValueError(f"Error converting to BSON: {str(e)}")

def parse_datetime_from_string(date_string, date_format="%Y-%m-%d %H:%M:%S"):
    """
    Converts a date string into a Python datetime object according to a specified format.
    This conversion is useful for handling date strings from user input or external sources,
    ensuring they can be used with MongoDB or other datetime utilities in Python.

    Args:
        date_string (str): The date string to convert.
        date_format (str): The format string used to interpret the date string.
                           Defaults to "%Y-%m-%d %H:%M:%S".

    Returns:
        datetime.datetime: The datetime object parsed from the string.

    Raises:
        ValueError: If the date_string does not match the expected format.

    """
    try:
        return datetime.strptime(date_string, date_format)
    except ValueError as e:
        raise ValueError(f"Invalid date format: {str(e)}")

def validate_document_schema(document, required_keys):
    """
    Validates that a given document (dictionary) includes all required keys.
    This function is particularly useful for ensuring that data integrity is maintained
    when inserting data into a database.

    Args:
        document (dict): The document to validate.
        required_keys (list of str): A list of keys that must be present in the document.

    Returns:
        bool: True if the document is valid and contains all required keys, False otherwise.

    Raises:
        KeyError: If any required keys are missing in the document.
    """
    missing_keys = [key for key in required_keys if key not in document]
    if missing_keys:
        raise KeyError(f"Missing keys in document: {', '.join(missing_keys)}")
    return True

def log_operation_details(operation_type, details):
    """
    Logs details of various operations. This function is a utility to help log operational events,
    which can be customized to fit different logging needs.

    Args:
        operation_type (str): A brief description of the operation type (e.g., "Insert", "Update").
        details (str): Detailed information about the operation.
    """
    print(f"Operation: {operation_type}, Details: {details}")  # This is a placeholder for actual logging
