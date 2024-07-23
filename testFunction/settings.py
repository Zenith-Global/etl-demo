import logging
import yaml
from pathlib import Path


BASE_PATH = Path(__file__).resolve().parent
QUERIES_FOLDER = BASE_PATH / "queries"
RESOURCES_FOLDER = BASE_PATH / "resources"
CONFIG_FILE = BASE_PATH/"config.yaml"


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

with open(CONFIG_FILE, 'r') as file:
    config = yaml.safe_load(file)

db_configs = config.get('databases', {})

DATABASES = {}

for db_name, db_settings in db_configs.items():
    DATABASES[db_name] = {
        'ENGINE': db_settings.get('ENGINE', ''),
        'NAME': db_settings.get('NAME', ''),
        'USER': db_settings.get('USER', ''),
        'SECRET_KEY': db_settings.get('SECRET_KEY', ''),
        'HOST': db_settings.get('HOST', ''),
        'PORT': db_settings.get('PORT', ''),
        'DRIVER': db_settings.get('DRIVER', ''),
        'TRUSTED_CONNECTION': db_settings.get('TRUSTED_CONNECTION', ''),
        'OPTIONS': {
            'TIMEOUT': db_settings.get('OPTIONS', {}).get('TIMEOUT', '')}
    }

