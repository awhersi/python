import boto3


# create an SQS client
sqs = boto3.client('sqs')


# specify the SQS queue URL and the message
queue_url = 'https://sqs.us-east-1.amazonaws.com/019487536022/my_sqs_queue'
message = 'Hello again, world!'


# sending the message
response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody=message
)


# print the message confirmation
print(f'Message: "{message}"" sent')
