import json
import logging
import uuid
from datetime import datetime
from app.utils import config, helpers


def handler(event, context):
    data = json.loads(event['body'])

    if 'text' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the todo item.")
    
    timestamp = str(datetime.utcnow())
    date = str(datetime.utcnow().date())
    ddb_resource = helpers.get_ddb_resource(context)
    table = ddb_resource.Table(config.ddb_tbl_name)

    item = {
        'id': str(uuid.uuid1()),
        'text': data['text'],
        'checked': False,
        'createdAt': date,
        'updatedAt': timestamp,
    }

    table.put_item(Item=item)
    logging.info("record created: "+str(item))
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item, cls=helpers.DecimalEncoder)
    }

    return response
