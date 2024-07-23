import json
from settings import DATABASES, LOGGERS, QUERIES_FOLDER, RESOURCES_FOLDER
import yaml 
from database import init_connections
from sqlalchemy.sql import text
import pandas as pd

def lambda_handler(event, context):
    engines = init_connections()
    gaia_engine =  next((item["engine"] for item in engines if item['name'] == "gaia_test"), None)

    with open(QUERIES_FOLDER/"main_queries.yaml", 'r') as f:
        queries = yaml.safe_load(f)
    
    query = queries["example"].format(table_name="dizCodiceIVA")
    with gaia_engine.connect() as conn:
        result = conn.execute(text(query))
        fields = [row for row in result]
        df_columns = pd.read_sql(query, gaia_engine)
        file_name_export = "test.xlsx"
        df_columns.to_excel(RESOURCES_FOLDER/file_name_export)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
