FROM amazonlinux:latest

# install required tools and libs
RUN yum update -y \
    && amazon-linux-extras install python3 \
    && curl -O https://bootstrap.pypa.io/get-pip.py \
    && python3 get-pip.py \
    && yum install -y zip \
    && yum install -y unzip \
    && pip3 install --upgrade awscli

RUN export AWS_PROFILE=default
ARG AWS_DEFAULT_REGION
ENV AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION

ARG AWS_ACCESS_KEY_ID
ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID

ARG AWS_SECRET_ACCESS_KEY
ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY

WORKDIR C:/Users/zakariya.ahmed/Documents/example-cf-stack
RUN pwd
COPY lambda_func/*.py ./
COPY Infastructure.yaml ./

RUN pip3 install -t . botocore  jmespath boto3 \
    && zip -r linux-lambda.zip ./

ARG CF_STACK_NAME
ARG DEPLOYMENT_BUCKET
RUN aws cloudformation package --template-file Infastructure.yaml --s3-bucket $DEPLOYMENT_BUCKET --output-template-file packaged.template
RUN aws cloudformation deploy --template-file packaged.template --capabilities CAPABILITY_NAMED_IAM --stack-name $CF_STACK_NAME
