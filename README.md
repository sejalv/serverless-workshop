<!--
platform: AWS
language: Python
authorLink: 'https://github.com/sejalv'
authorName: 'Sejal Vaidya'
-->
# Serverless REST + DDB Workshop

## Workshops

1. [https://github.com/sejalv/serverless-workshop/blob/master/hello_world.md](**Hello World**): Basic project setup, test and deployment.
2. **Todos app**: CRUD application with a dockerized environment to test AWS services locally. Python for services and DynamoDB for database.

## Project Structure:

* Each CRUD operation (create, retrieve/get, update, delete) is performed by AWS Lambda, and associated with an API endpoint. Each of the lambda handlers are present in the `app` directory.
* Tests are present in the `app/tests/` directory. Also includes `conftest.py` for `pytest` *fixtures*, that help in mocking or configuring your environment. 

## Setup

```bash
npm install -g serverless
```

**Detailed Setup Instructions**: [https://github.com/sejalv/serverless-workshop/blob/master/setup.md](setup)

**Application/Service Configuration**: 

## Dev Env (Localstack + Docker)

```docker-compose build```

```docker-compose up``` 

### Tests
```docker-compose run app pytest tests/ -s -vv ```
On the container for `app`, all the tests located within the `app/tests/` directory will run. This will also generate the AWS environment locally, via `app/tests/conftest.py` (eg. `ddb_tbl` fixture creates the DDB table `serverless-workshop-rest-ddb-test`).

```aws --endpoint-url=http://localhost:4566 ddb select  serverless-workshop-rest-ddb-test```
Querying locally to check if the table is created. Also, creates an entry from the `test_create.py` test.


## Deploy

**Optional Setup**:

`aws sso login --profile <profile-name>`

`yawsso`


In order to deploy the endpoint simply run

```bash
serverless deploy --stage <dev/stg>
```

The expected result should be similar to:

```bash
Serverless: Packaging service…
Serverless: Uploading CloudFormation file to S3…
Serverless: Uploading service .zip file to S3…
Serverless: Updating Stack…
Serverless: Checking Stack update progress…
Serverless: Stack update finished…

Service Information
service: serverless-rest-api-with-dynamodb
stage: dev
region: eu-central-1
api keys:
  None
endpoints:
  POST - https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/todos
  GET - https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/todos
  GET - https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/todos/{id}
  PUT - https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/todos/{id}
  DELETE - https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/todos/{id}
functions:
  serverless-rest-api-with-dynamodb-dev-update: arn:aws:lambda:eu-central-1:XXXXXXX:function:serverless-rest-api-with-dynamodb-dev-update
  serverless-rest-api-with-dynamodb-dev-get: arn:aws:lambda:eu-central-1:XXXXXXX:function:serverless-rest-api-with-dynamodb-dev-get
  serverless-rest-api-with-dynamodb-dev-list: arn:aws:lambda:eu-central-1:XXXXXXX:function:serverless-rest-api-with-dynamodb-dev-list
  serverless-rest-api-with-dynamodb-dev-create: arn:aws:lambda:eu-central-1:XXXXXXX:function:serverless-rest-api-with-dynamodb-dev-create
  serverless-rest-api-with-dynamodb-dev-delete: arn:aws:lambda:eu-central-1:XXXXXXX:function:serverless-rest-api-with-dynamodb-dev-delete
```


## Usage

You can create, retrieve, update, or delete todos with the following commands:

**via API Endpoints:**

### Create a Todo

```bash
curl -X POST https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/todos --data '{ "text": "Learn Serverless" }'
```

No output

### List all Todos

```bash
curl https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/todos
```

Example output:
```bash
[{"text":"Deploy my first service","id":"ac90feaa11e6-9ede-afdfa051af86","checked":true,"updatedAt":},{"text":"Learn Serverless","id":"206793aa11e6-9ede-afdfa051af86","createdAt":,"checked":false,"updatedAt":}]%
```

### Get one Todo

```bash
# Replace the <id> part with a real id from your todos table
curl https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/todos/<id>
```

Example Result:
```bash
{"text":"Learn Serverless","id":"ee6490d0-aa11e6-9ede-afdfa051af86","createdAt":,"checked":false,"updatedAt":}%
```

### Update a Todo

```bash
# Replace the <id> part with a real id from your todos table
curl -X PUT https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/todos/<id> --data '{ "text": "Learn Serverless", "checked": true }'
```

Example Result:
```bash
{"text":"Learn Serverless","id":"ee6490d0-aa11e6-9ede-afdfa051af86","createdAt":,"checked":true,"updatedAt":}%
```

### Delete a Todo

```bash
# Replace the <id> part with a real id from your todos table
curl -X DELETE https://XXXXXXX.execute-api.us-east-1.amazonaws.com/dev/todos/<id>
```

**via local CLI:**

```serverless invoke --function create --stage dev```

No output

## Scaling

### AWS Lambda

By default, AWS Lambda limits the total concurrent executions across all functions within a given region to 100. The default limit is a safety limit that protects you from costs due to potential runaway or recursive functions during initial development and testing. To increase this limit above the default, follow the steps in [To request a limit increase for concurrent executions](http://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html#increase-concurrent-executions-limit).

### DynamoDB

When you create a table, you specify how much provisioned throughput capacity you want to reserve for reads and writes. DynamoDB will reserve the necessary resources to meet your throughput needs while ensuring consistent, low-latency performance. You can change the provisioned throughput and increasing or decreasing capacity as needed.

This is can be done via settings in the `serverless.yml`.

```yaml
  ProvisionedThroughput:
    ReadCapacityUnits: 1
    WriteCapacityUnits: 1
```

In case you expect a lot of traffic fluctuation we recommend to checkout this guide on how to auto scale DynamoDB [https://aws.amazon.com/blogs/aws/auto-scale-dynamodb-with-dynamic-dynamodb/](https://aws.amazon.com/blogs/aws/auto-scale-dynamodb-with-dynamic-dynamodb/)


## References:

* https://www.serverless.com
* https://serverless-stack.com
* https://github.com/localstack/localstack
