import json
from datetime import datetime
import logging
from app.utils import config, helpers


def handler(event, context):
    data = json.loads(event['body'])

    ddb_resource = helpers.get_ddb_resource(context)
    table = ddb_resource.Table(config.ddb_tbl_name)
    orig_item = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )
    print(data)
    print(orig_item)
    if not orig_item or ('text' not in data and 'checked' not in data):
        logging.error("Validation Failed")
        raise Exception("Couldn't update the todo item.")
        return

    timestamp = str(datetime.utcnow())

    result = table.update_item(
        Key={
            'id': event['pathParameters']['id']
        },
        ExpressionAttributeNames={
          '#todo_text': 'text',
        },
        ExpressionAttributeValues={
          ':text': data.get('text', orig_item['Item']['text']),
          ':checked': data.get('checked', orig_item['Item']['checked']),
          ':updatedAt': timestamp,
        },
        UpdateExpression='SET #todo_text = :text, '
                         'checked = :checked, '
                         'updatedAt = :updatedAt',
        ReturnValues='ALL_NEW',
    )
    logging.info("record updated: " + str(result))
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Attributes'],
                           cls=helpers.DecimalEncoder)
    }

    return response
