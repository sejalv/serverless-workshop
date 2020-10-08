import os

ddb_tbl_name = os.environ.get(
    "DYNAMODB_TABLE", "serverless-workshop-rest-ddb-test"
)

local_url = os.environ.get("LOCALSTACK_HOST", "http://localhost")+":4566"
region_name = os.environ.get("AWS_DEFAULT_REGION", "eu-central-1")
