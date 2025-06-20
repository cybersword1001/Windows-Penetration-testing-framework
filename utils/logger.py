"""
Logging utility for the penetration testing tool
"""

import logging
import sys
from datetime import datetime

def setup_logger(verbose=False):
    """Setup main logger"""
    level = logging.DEBUG if verbose else logging.INFO
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Create console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    
    # Create file handler
    file_handler = logging.FileHandler(f'pentest_{datetime.now().strftime("%Y%m%d")}.log')
    file_handler.setFormatter(formatter)
    
    # Setup root logger
    logger = logging.getLogger()
    logger.setLevel(level)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

def get_logger(name):
    """Get logger for specific module"""
    return logging.getLogger(name)
