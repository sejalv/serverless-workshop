import json, logging, os, time
from datetime import datetime

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def update(event, context):
    data = json.loads(event['body'])
    if 'task' not in data or 'isCompleted' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't update the todo item.")
        return

    timestamp = str(datetime.utcnow())

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # update the todo in the database
    result = table.update_item(
        Key={
            'id': event['pathParameters']['id']
        },
        ExpressionAttributeNames={
          '#todo_task': 'task',
        },
        ExpressionAttributeValues={
          ':task': data['task'],
          ':isCompleted': data['isCompleted'],
          ':updatedAt': timestamp,
        },
        UpdateExpression='SET #todo_task = :task, '
                         'isCompleted = :isCompleted, '
                         'updatedAt = :updatedAt',
        ReturnValues='ALL_NEW',
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Attributes'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
