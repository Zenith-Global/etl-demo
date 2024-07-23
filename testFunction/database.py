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

        if db.get("USER") is None:
            LOGGERS.get("console_logger").error(f"USER is not defined")
            quit()
        LOGGERS.get("console_logger").info(f"USER: {db['USER']}")
        
        if db.get("NAME") is None:
            LOGGERS.get("console_logger").error(f"NAME is not defined")
            quit()
        LOGGERS.get("console_logger").info(f"NAME: {db['NAME']}")

        if db.get("HOST") is None:
            LOGGERS.get("console_logger").error(f"HOST is not defined")
            quit()
        LOGGERS.get("console_logger").info(f"HOST: {db['HOST']}")

        if db.get("DRIVER") is None:
            LOGGERS.get("console_logger").error(f"DRIVER is not defined")
            quit()
        LOGGERS.get("console_logger").info(f"DRIVER: {db['DRIVER']}")

        if db.get("SECRET_KEY") is None:
            LOGGERS.get("console_logger").error(f"SECRET_KEY is not defined")
            quit()
        LOGGERS.get("console_logger").info(f"SECRET_KEY: {db['SECRET_KEY']}")

        if db.get("TRUSTED_CONNECTION") is None:
            LOGGERS.get("console_logger").error(f"TRUSTED_CONNECTION is not defined")
            quit()
        LOGGERS.get("console_logger").info(f"Trust connection: {db['TRUSTED_CONNECTION']}")

        connection_string = (f"mssql+pyodbc://"
                            f"{db['USER']}:{db['SECRET_KEY']}@{db['HOST']}/{db['NAME']}"
                            f"?driver={db['DRIVER']}&TrustServerCertificate={db['TRUSTED_CONNECTION']}")
    
        new_engine = create_engine(connection_string)

        engines.append({"name": each_db, "engine": new_engine})

    return engines
