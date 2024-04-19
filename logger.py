import logging  # Import the built-in logging module

def configure_logger():
    """
    Configures the basic settings for the logging system.

    This function sets up the global logging configuration which will affect all logging calls. It specifies
    the lowest-severity log message a logger will handle, and the format that the log messages will have.

    The logging levels are set as follows:
    - DEBUG: Detailed information, typically of interest only when diagnosing problems.
    - INFO: Confirmation that things are working as expected.
    - WARNING: An indication that something unexpected happened, or indicative of some problem in the near future.
    - ERROR: Due to a more serious problem, the software has not been able to perform some function.
    - CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

    The chosen log level (INFO) and the format of the log messages will apply to all log messages handled
    by the root logger.

    Format:
        - %(asctime)s: The time of the log message (e.g., 2021-05-06 13:49:10,896).
        - %(levelname)s: The severity level of the log message (e.g., INFO, DEBUG).
        - %(message)s: The actual log message passed to the logger.

    Example of a log message:
        "2021-05-06 13:49:10,896 - INFO - This is an informational message"
    """
    logging.basicConfig(
        level=logging.INFO,  # Set the logging level to INFO. This means all INFO, WARNING, ERROR, and CRITICAL messages will be logged.
        format='%(asctime)s - %(levelname)s - %(message)s'  # Define the format of log messages.
    )
