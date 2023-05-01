import logging

def get_logger() -> logging.Logger:
    """
    Return's logging.logger: descriptions 
    """
    logger = logging.getLogger('dataflow')
    logger.setLevel(logging.INFO)

    return logger

