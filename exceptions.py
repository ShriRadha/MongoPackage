class Error(Exception):
    """Base class for other exceptions"""
    pass

class DatabaseConnectionError(Error):
    """Raised when the database connection fails"""
    def __init__(self, message="Could not connect to the database"):
        self.message = message
        super().__init__(self.message)

class InsertionError(Error):
    """Raised when an insertion operation fails"""
    def __init__(self, message="Failed to insert data into the database"):
        self.message = message
        super().__init__(self.message)

class DocumentNotFoundError(Error):
    """Raised when a document is not found in query"""
    def __init__(self, message="No document found matching the query"):
        self.message = message
        super().__init__(self.message)

class UpdateError(Error):
    """Raised when an update operation fails"""
    def __init__(self, message="Failed to update the document"):
        self.message = message
        super().__init__(self.message)

class DeletionError(Error):
    """Raised when a deletion operation fails"""
    def __init__(self, message="Failed to delete the document"):
        self.message = message
        super().__init__(self.message)

