import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ShawarmaOrders')  # Replace with your DynamoDB table name

def lambda_handler(event, context):
    body = json.loads(event['body'])
    shawarma_type = body['shawarma_type']
    quantity = body['quantity']
    customer_name = body['customer_name']
    
    order_id = hash(f"{shawarma_type}{quantity}{customer_name}")
    
    response = table.put_item(
        Item={
            'order_id': order_id,
            'shawarma_type': shawarma_type,
            'quantity': quantity,
            'customer_name': customer_name
        }
    )
    
    response_data = {
        "message": "Order placed successfully",
        "order_id": order_id
    }
    
    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",  # This allows requests from any origin
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "OPTIONS,POST"  # Allow specified methods
        },
        "body": json.dumps(response_data)
    }
    
    return response