import json, logging, os, time, uuid
from datetime import datetime

import boto3
dynamodb = boto3.resource('dynamodb')


def create(event, context):
    data = json.loads(event['body'])
    
    if 'task' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the todo item.")
    
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    timestamp = str(datetime.utcnow())
    _id = str(uuid.uuid1())

    item = {
      'id': _id,
      'task': data['task'],
      'isCompleted': data.get('isCompleted',None),
      'createdAt': timestamp,
      'updatedAt': timestamp,
    }

    # write the todo to the database
    table.put_item(Item=item)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response
