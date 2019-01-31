import json
import os

import boto3
from PlayerTransactionApi import PLAYER_ACC_ID
from PlayerTransactionApi import TRANSACTION_ID


def lambda_handler(event, context):

    requestBody = event['body']
    playerTransactionDto = json.loads(requestBody)

    client = boto3.resource('dynamodb')

    table = client.Table(os.environ['DB_TABLE'])

    item_dict = {
        PLAYER_ACC_ID: playerTransactionDto[PLAYER_ACC_ID],
        TRANSACTION_ID:  playerTransactionDto[TRANSACTION_ID]
    }

    del playerTransactionDto[PLAYER_ACC_ID]
    del playerTransactionDto[TRANSACTION_ID]

    for key, value in playerTransactionDto.items():
        item_dict[key] = value

    try:
        table.put_item(Item=item_dict)

    except KeyError:
        print('Invalid Request Body: '.join(playerTransactionDto));

        return {
            "statusCode": 400,
            "body": json.dumps('Invalid Request Body.')
        }

    return {
        "statusCode": 200,
        "body": json.dumps('Successfully recorded transaction.')
    }
