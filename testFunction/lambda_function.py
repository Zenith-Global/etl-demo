import json
from database import Database
from settings import RESOURCES_FOLDER

def lambda_handler(event, context):
    db = Database()
    
    query_args = {"table_name": "dizCodiceIVA"}
    query_res = db.perform_query(db_name="gaia_test", query_name="example", query_args=query_args)
    file_name_export = "test.xlsx"
    query_res.to_excel(RESOURCES_FOLDER/file_name_export)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
