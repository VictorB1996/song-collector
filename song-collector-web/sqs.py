import os
import json
import boto3
import dotenv

dotenv.load_dotenv(override=True)

def send_queue_message(message_body):
    sqs = boto3.client(
        "sqs",
        region_name = os.environ["REGION_NAME"],
        aws_access_key_id = os.environ["AWS_ACCESS_KEY"],
        aws_secret_access_key = os.environ["AWS_SECRET_ACCESS_KEY"]
    )
    response = sqs.send_message(
        QueueUrl=os.environ["QUEUE_URL"],
        MessageBody=json.dumps(message_body)
    )