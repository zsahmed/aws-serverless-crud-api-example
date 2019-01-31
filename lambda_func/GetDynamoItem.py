import boto3
from boto3.dynamodb.conditions import Key, Attr
import os
import json

from PlayerTransactionApi import PLAYER_ACC_ID
from PlayerTransactionApi import TRANSACTION_ID


def lambda_handler(event, context):
    pathParams = event['pathParameters']
    client = boto3.resource('dynamodb')

    table = client.Table(os.environ['DB_TABLE'])

    response = table.query(
        KeyConditionExpression=Key(PLAYER_ACC_ID).eq(pathParams[PLAYER_ACC_ID]) & Key(TRANSACTION_ID).eq(pathParams[TRANSACTION_ID])
    )

    if not response['Items']:
        print('Transaction not found for request: '.join(event['pathParameters']))
        return {
            "statusCode": 404,
            "body": json.dumps('Transaction not found.')
        }

    return {
        "statusCode": 200,
        "body": json.dumps(response['Items'])
    }
