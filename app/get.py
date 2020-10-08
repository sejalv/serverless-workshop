import json
from app.utils import config, helpers


def handler(event, context):
    ddb_resource = helpers.get_ddb_resource(context)
    table = ddb_resource.Table(config.ddb_tbl_name)

    # fetch rec from the database
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                           cls=helpers.DecimalEncoder)
    }

    return response
