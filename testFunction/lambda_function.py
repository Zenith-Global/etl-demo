import json
from database import Database

def lambda_handler(event, context):
    db = Database()
    
    db.perform_query("gaia_test", "example")

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
