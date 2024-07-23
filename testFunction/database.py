from settings import DATABASES, LOGGERS
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, MetaData


def init_connections():
    load_dotenv()

    engines = []
    LOGGERS.get("console_logger").info("Preparing connection towards Databases")
    
    for each_db in DATABASES:
        
        db = DATABASES[each_db]
        LOGGERS.get("console_logger").info(f"Considering database {each_db}")
        LOGGERS.get("console_logger").info(f"USER: {db['USER']}")
        LOGGERS.get("console_logger").info(f"NAME: {db['NAME']}")
        LOGGERS.get("console_logger").info(f"HOST: {db['HOST']}")
        LOGGERS.get("console_logger").info(f"DRIVER: {db['DRIVER']}")
        LOGGERS.get("console_logger").info(f"SECRET_KEY: {db['SECRET_KEY']}")
        LOGGERS.get("console_logger").info(f"Trust connection: {db['Trusted_Connection']}")

        connection_string = f"mssql+pyodbc://{db['USER']}:{db['SECRET_KEY']}@{db['HOST']}/{db['NAME']}?driver={db['DRIVER']}&TrustServerCertificate={db['Trusted_Connection']}"
        new_engine = create_engine(connection_string)
        engines.append({"name": each_db, "engine": new_engine})

    return engines
    # metadata = MetaData()