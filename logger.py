import logging

def configure_logger():
    """
    Configures the logging system to display log messages with certain properties.
    
    This function sets up the basic configuration for the logging system, which includes:
    - Setting the minimum level of log messages to display. In this case, INFO and higher level messages (INFO, WARNING, ERROR, CRITICAL) will be shown.
    - Defining the format of the log messages to ensure consistency and provide essential information at a glance. The format specified here includes:
        * Time and date of the log message (`asctime`)
        * Severity level of the message (`levelname`)
        * The actual log message text (`message`)
    """
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
