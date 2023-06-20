import os
import boto3

sns = boto3.client("sns")
SNS_TOPIC_ARN = os.environ.get("SNS_TOPIC_ARN")


def handler(event, context):
    for record in event["Records"]:
        payload = record["body"]
        print(payload)
        sns.publish(TopicArn=SNS_TOPIC_ARN, Subject="Hello from Lambda", Message=payload)
