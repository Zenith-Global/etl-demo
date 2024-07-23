import pandas as pd
import os
import logging
import yaml
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData, Table, Column, String
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import text
from pathlib import Path

load_dotenv()

file_logger = logging.getLogger('file_logger')
console_logger = logging.getLogger('console_logger')

file_logger.setLevel(logging.INFO)
console_logger.setLevel(logging.INFO)


log_file = 'debug.log'
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

file_logger.addHandler(file_handler)
console_logger.addHandler(console_handler)

LOGGERS = {
    'file_logger': file_logger,
    'console_logger': console_logger
}

DATABASES = {
    'gaia': { 
        'ENGINE': os.getenv("GAIA_DB_ENGINE", default=""),
        'NAME': os.getenv("GAIA_DB_NAME", default=""),
        'USER': os.getenv("GAIA_USER", default=""),
        'SECRET_KEY': os.getenv("GAIA_SECRET_KEY", default=""),
        'HOST': os.getenv("GAIA_HOST", default=""),
        'PORT': os.getenv("GAIA_PORT", default=""),
        'OPTIONS': {
                'query_timeout': 10,
            },
        'Trusted_Connection':os.getenv("GAIA_DB_TRUSTED_CONNECTION", default=""),
        'DRIVER': os.getenv("GAIA_DB_OPTIONS_DRIVER", default="")
    }
}

BASE_PATH = Path(__file__).resolve().parent
QUERIES_FOLDER = BASE_PATH / "queries"
print(QUERIES_FOLDER)

