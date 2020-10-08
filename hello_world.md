A) Create a new boilerplate (with provider=aws, runtime=python3)
```
my-serverless-project>$ serverless create --template aws-python3 --name <my-serverless-project>
```

Params
* `--name` or shorthand `n`: Name of the new service/project to be created
* `--template` or shorthand `-t` flag: Code template. We use `aws-python3` as a default standard, but not restriced to a language.
* `--path` or shorthand `-p`: location to be created with the template service files.


B) Directory structure and auto-generated files:

Default contents of directory:
```
my-serverless-project>$ ls
```
```
.
├── .gitignore
├── handler.py
└── serverless.yml
```

Default contents of `serverless.yml`:
```
my-serverless-project>$ cat serverless.yml
```
```
provider:
  name: aws
  runtime: python3.6
functions:
  hello:
    handler: handler.hello
```

Change file to add following options:
* `--stage` or `-s`: Name of the stage in service, eg. `dev`.
* `--region` or `-r`: Name of the AWS region to deploy into, eg. `eu-west-1`.


Default contents of `handler.py`:
```
my-serverless-project>$ cat handler.py
```
```
import json
def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }
response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
return response
# Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
 ```

### Step 3: (optional) Test the default service 

A) Deploy service:
```
my-serverless-project>$ serverless deploy
# or
my-serverless-project>$ sls deploy
```

Deployment trace:
```
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Creating Stack...
Serverless: Checking Stack create progress...
.....
Serverless: Stack create finished...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service .zip file to S3 (390 B)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
................
Serverless: Stack update finished...
Service Information
service: hello-world
stage: dev
region: eu-west-1
stack: hello-world-dev
api keys:
  None
endpoints:
  None
functions:
  hello: hello-world-dev-hello
```

Or
```
my-serverless-project>$ serverless deploy -v
# or
my-serverless-project>$ sls deploy -v
```
`--verbose` or shorthand `-v`: Shows all stack events during deployment

```
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service .zip file to S3 (390 B)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
CloudFormation - UPDATE_IN_PROGRESS - AWS::CloudFormation::Stack - hello-world-dev
CloudFormation - CREATE_IN_PROGRESS - AWS::ApiGateway::RestApi - ApiGatewayRestApi
CloudFormation - UPDATE_IN_PROGRESS - AWS::Lambda::Function - HelloLambdaFunction
CloudFormation - CREATE_IN_PROGRESS - AWS::ApiGateway::RestApi - ApiGatewayRestApi
CloudFormation - UPDATE_COMPLETE - AWS::Lambda::Function - HelloLambdaFunction
CloudFormation - CREATE_COMPLETE - AWS::ApiGateway::RestApi - ApiGatewayRestApi
CloudFormation - CREATE_IN_PROGRESS - AWS::ApiGateway::Resource - ApiGatewayResourceHello
CloudFormation - CREATE_IN_PROGRESS - AWS::Lambda::Permission - HelloLambdaPermissionApiGateway
CloudFormation - CREATE_IN_PROGRESS - AWS::ApiGateway::Resource - ApiGatewayResourceHello
CloudFormation - CREATE_IN_PROGRESS - AWS::Lambda::Permission - HelloLambdaPermissionApiGateway
CloudFormation - CREATE_COMPLETE - AWS::ApiGateway::Resource - ApiGatewayResourceHello
CloudFormation - CREATE_IN_PROGRESS - AWS::ApiGateway::Method - ApiGatewayMethodHelloGet
CloudFormation - CREATE_IN_PROGRESS - AWS::ApiGateway::Method - ApiGatewayMethodHelloGet
CloudFormation - CREATE_COMPLETE - AWS::ApiGateway::Method - ApiGatewayMethodHelloGet
CloudFormation - CREATE_IN_PROGRESS - AWS::ApiGateway::Deployment - ApiGatewayDeployment1534113893559
CloudFormation - CREATE_IN_PROGRESS - AWS::ApiGateway::Deployment - ApiGatewayDeployment1534113893559
CloudFormation - CREATE_COMPLETE - AWS::ApiGateway::Deployment - ApiGatewayDeployment1534113893559
CloudFormation - CREATE_COMPLETE - AWS::Lambda::Permission - HelloLambdaPermissionApiGateway
CloudFormation - UPDATE_COMPLETE_CLEANUP_IN_PROGRESS - AWS::CloudFormation::Stack - hello-world-dev
CloudFormation - UPDATE_COMPLETE - AWS::CloudFormation::Stack - hello-world-dev
Serverless: Stack update finished...
Service Information
service: hello-world
stage: dev
region: eu-west-1
stack: hello-world-dev
api keys:
  None
endpoints:
  GET - https://x7o0xwsbkd.execute-api.eu-west-1.amazonaws.com/dev/hello
functions:
  hello: hello-world-dev-hello
Stack Outputs
HelloLambdaFunctionQualifiedArn: arn:aws:lambda:eu-west-1:778443482073:function:hello-world-dev-hello:1
ServiceEndpoint: https://x7o0xwsbkd.execute-api.eu-west-1.amazonaws.com/dev
ServerlessDeploymentBucketName: hello-world-dev-serverlessdeploymentbucket-qqgrblrjprhu
```

What this does:
1. `serverless` creates a CloudFormation template based on the `serverless.yml`
2. Compresses the CloudFormation template and your `lambda-func.py` into a zip archive
3. Creates an S3 bucket on `AWS-Postman-Staging` account and uploads the zip archive to it
4. Executes the CloudFormation template, which includes configuring an AWS Lambda function and pointing it to the S3 zip archive


B) Invoke deployed function (test default function):
```
sls invoke -f hello
```

`--function` or shorthand `-f`: name of the function to call

`hello` is the label of the function `handler.hello` configured in `serverless.yml`

```
{
    "statusCode": 200,
    "body": "{\"message\":\"Go Serverless v1.0! Your function executed successfully!\",\"input\":{}}"
}
```



#### References

https://serverless.com/framework/docs/providers/aws/guide/quick-start/
https://serverless.com/framework/docs/providers/aws/examples/hello-world/python/
https://medium.com/faun/aws-lambda-serverless-framework-python-part-1-a-step-by-step-hello-world-4182202aba4a
