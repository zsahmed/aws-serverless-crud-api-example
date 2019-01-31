import boto3
import os
import json

from PlayerTransactionApi import PLAYER_ACC_ID
from PlayerTransactionApi import TRANSACTION_ID


def lambda_handler(event, context):
    pathParams = event['pathParameters']
    client = boto3.resource('dynamodb')

    table = client.Table(os.environ['DB_TABLE'])

    response = table.delete_item(
        Key={
            PLAYER_ACC_ID: pathParams[PLAYER_ACC_ID],
            TRANSACTION_ID: pathParams[TRANSACTION_ID]
        }
    )

    print(response)

    return {
        "statusCode": 200,
        "body": json.dumps('Item deleted.')
    }
