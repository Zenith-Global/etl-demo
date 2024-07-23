from settings import DATABASES, LOGGERS
from sqlalchemy import create_engine


def init_connections():

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


        if db.get("SECRET_KEY") is None:
            LOGGERS.get("console_logger").error(f"SECRET_KEY is not defined")
            quit()
        LOGGERS.get("console_logger").info(f"SECRET_KEY: {db['SECRET_KEY']}")


        connection_string = (f"mssql+pyodbc://"
                            f"{db['USER']}:{db['SECRET_KEY']}@{db['HOST']}/{db['NAME']}")
        
        optional_parameters = []
        options = db.get('OPTIONS', {})
        if options is not None:
            connection_string += "?"
            LOGGERS.get("console_logger").info(f"Optional parameters are present, adding them to the connection string...")
            for key, value in options.items():
                LOGGERS.get("console_logger").info(f"Adding '{key}' parameter to the connection string")
                optional_parameters.append(f"{key}={value}")

        if optional_parameters:
            connection_string += "&" + "&".join(optional_parameters)
        
        LOGGERS.get("console_logger").info(f"Connection string for '{each_db}' is ready: '{connection_string}'")
        new_engine = create_engine(connection_string)

        engines.append({"name": each_db, "engine": new_engine})

    return engines
