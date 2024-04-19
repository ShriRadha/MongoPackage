import os  # Import the os module to access environment variables

def get_config():
    """
    Retrieves the MongoDB connection URI and database name from environment variables.

    This function encapsulates the environment settings for MongoDB connectivity,
    allowing the database connection details to be set outside of the application code.
    Using environment variables for this purpose enhances security and flexibility, 
    as it separates sensitive information from the codebase and enables easy adjustments
    without code changes.

    Returns:
        tuple: A tuple containing the URI and database name.
            - uri (str): MongoDB URI used to connect to the database. Defaults to
                         "mongodb://localhost:27017" if not specified in the environment.
            - dbname (str): The name of the database to use. Defaults to "test" if not
                            specified in the environment.
    """
    # Fetch the MongoDB URI from environment variables, with a default fallback
    uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    
    # Fetch the database name from environment variables, with a default fallback
    dbname = os.getenv("MONGO_DBNAME", "test")
    
    return uri, dbname  # Return the database URI and name as a tuple
