import json

def lambda_handler(event, context):
    menu = [
        {"id": 1, "name": "Chicken Shawarma", "price": 10.99},
        {"id": 2, "name": "Beef Shawarma", "price": 12.99}
    ]
    
    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",  # This allows requests from any origin
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET"  # Allow specified methods
        },
        "body": json.dumps(menu)
    }
    
    return response