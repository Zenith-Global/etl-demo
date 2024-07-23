import json
from database import Database

def lambda_handler(event, context):
    db = Database()
    
    query_args = {"table_name": "dizCodiceIVA"}
    db.perform_query(db_name="gaia_test", query_name="example", query_args=query_args)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
