from app.utils import config, helpers


def handler(event, context):
    ddb_resource = helpers.get_ddb_resource(context)
    table = ddb_resource.Table(config.ddb_tbl_name)

    table.delete_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    response = {
        "statusCode": 200
    }

    return response
