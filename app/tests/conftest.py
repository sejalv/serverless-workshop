import os
import sys
import pytest
import boto3
import botocore.config

sys.path.append(os.path.abspath(os.path.dirname("__file__")))
from app.utils import config

tbl = config.ddb_tbl_name


@pytest.fixture(scope="package")
def ddb_resource():
    yield boto3.resource(
        'dynamodb',
        endpoint_url=config.local_url,
        region_name=config.region_name
    )


@pytest.fixture(scope="package")
def ddb_client():
    yield boto3.client(
        'dynamodb',
        endpoint_url=config.local_url,
        region_name=config.region_name
    )


@pytest.fixture(scope="package")
def ddb_tbl(ddb_resource, ddb_client):
    existing_tables = ddb_client.list_tables()['TableNames']
    if tbl not in existing_tables:
        response = ddb_resource.create_table(
            TableName=tbl,
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'
                }
            ],
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )
        response.wait_until_exists()
    yield ddb_resource.Table(tbl)


@pytest.fixture(scope="package")
def lambda_client():
    yield boto3.client(
        'lambda',
        endpoint_url=config.local_url,
        region_name=config.region_name,
        config=botocore.config.Config(retries={'max_attempts': 0})
    )


@pytest.fixture(scope="package")
def context():
    context_request = {
        'aws_request_id': 'test',
        'log_stream_name': '1f73402ad',
        'invoked_function_arn': 'arn:aws:lambda:region:1000:function:TestCFStackNam-TestLambdaFunctionResourceName-ABC-1234F',
        'client_context': None,
        'log_group_name': '/aws/lambda/TestCFStackName-TestLambdaFunctionResourceName-ABC-1234F',
        'function_name': 'TestCloudFormationStackName-TestLambdaFunctionResourceName--ABC-1234F',
        'function_version': '$LATEST',
        'identity': '<__main__.CognitoIdentity object at 0x1fb81abc00>',
        'memory_limit_in_mb': '128'
    }

    class Struct:
        def __init__(self, **entries):
            self.__dict__.update(entries)

    context = Struct(**context_request)

    yield context
