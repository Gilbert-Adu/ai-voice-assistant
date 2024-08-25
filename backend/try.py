from boto3 import Session # type: ignore
import boto3 # type: ignore
from botocore.exceptions import BotoCoreError, ClientError # type: ignore
from contextlib import closing
import os
import sys
import subprocess
import json


lambda_client = boto3.client("lambda", 
                     aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                     aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                    region_name=os.getenv('AWS_REGION')) # type: ignore


def invoke_lambda(text):
    event_payload = {
        "user_q": text,
    }

    response = lambda_client.invoke(
        FunctionName='serverless-HelloWorldFunction-cKwdlvh8cl1q',
        InvocationType='RequestResponse',
        Payload=json.dumps(event_payload)
    )

    response_payload = response['Payload'].read().decode('utf-8')
    result = json.loads(response_payload)
    message = json.loads(result['body'])['message']

    print("message from Lambda: ", message)

invoke_lambda('hello')
