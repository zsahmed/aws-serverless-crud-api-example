# Objective
This repository is an example AWS Serverless CRUD API. This solution leverages the following services:

- API Gateway
- Lambda
- DynamoDB
- CloudFormation
- CloudWatch
- IAM
- S3

In addition, Docker images will be utilized to create the CloudFormation stack and deploy the Pythonic Lambda functions.

### Example Solution Overview
This solution was built from the perspective of a video game studio that needs an API to track the microtransactions within their game. 
This API needs to be able to write, read, and delete transactions sent via HTTPS.

# Setup
Before deploying this repository, you must have the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) and [Docker](https://www.docker.com/) installed and configured for your local machine.


# Deployment
The following command will build a Docker image using the Dockerfile in our repo. 
Once the image is created, Docker will package the Python code for a Linux environment 
(what AWS Lambda runs on) and deploy the code as well as the CloudFormation stack to your AWS account.

Before deploying the stack, you must first create an S3 bucket for your deployment package.  

The image requires 5 arguments: an AWS region, Access key / Secret key for the AWS IAM User responsible for deployments, 
an S3 bucket to place the packaged contents, and a stack name for your CloudFormation stack
```
docker build 
--build-arg AWS_DEFAULT_REGION="<YOUR_REGION>" 
--build-arg AWS_ACCESS_KEY_ID="<YOUR_ACCESS_KEY>" 
--build-arg AWS_SECRET_ACCESS_KEY="<YOUR_SECRET_KEY>" 
--build-arg DEPLOYMENT_BUCKET="<YOUR_S3_BUCKET>" 
--build-arg CF_STACK_NAME="<YOUR_STACK_NAME>" . --rm
```

# API 
The Lambda functions can be accessed via `playerTranApi` API Gateway proxy.

To update or create an item in Dynamo, use the `createPlayerTransaction` Resource. Here is an example JSON Body:

```
{
  "playerAccountId": "MumboJumbo_1",
  "transactionId": "12345",
  "usdAmount": "5.00",
  "gameItem": "Health Potion"
}
```

To GET an Item from Dynamo, use the `/{playerAccountId}/{transactionId}` Resource:

`https://gq6lioa994.execute-api.us-west-2.amazonaws.com/dev/MumboJumbo_1/12345`

The DELETE call also leverages the `/{playerAccountId}/{transactionId}` Resource:

`https://gq6lioa994.execute-api.us-west-2.amazonaws.com/dev/MumboJumbo_1/12345`