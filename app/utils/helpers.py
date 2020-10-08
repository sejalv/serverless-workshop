import boto3
import decimal
import json
from app.utils import config


# This is a workaround for: http://bugs.python.org/issue16535
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)


def get_ddb_resource(context):
    if context.aws_request_id == 'test':
        return boto3.resource(
            'dynamodb',
            endpoint_url=config.local_url,
            region_name=config.region_name
        )
    return boto3.resource('dynamodb')
