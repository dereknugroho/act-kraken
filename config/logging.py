import logging
import os

from logging.handlers import RotatingFileHandler

DEBUG = logging.DEBUG
INFO = logging.INFO
WARNING = logging.WARNING
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL

LOG_DIR = os.path.join(os.path.dirname(__file__), '..', 'logs')

def setup_logger(name, logfile, level, max_bytes=5*1024*1024, backup_count=5):
    """Create a logger with a RotatingFileHandler."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = RotatingFileHandler(
            os.path.join(LOG_DIR, logfile),
            maxBytes=max_bytes,
            backupCount=backup_count
        )
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(name)s | %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
