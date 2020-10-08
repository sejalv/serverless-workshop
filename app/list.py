import json
from app.utils import config, helpers


def handler(event, context):
    ddb_resource = helpers.get_ddb_resource(context)
    table = ddb_resource.Table(config.ddb_tbl_name)

    result = table.scan()

    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'], cls=helpers.DecimalEncoder)
    }

    return response
