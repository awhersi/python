import logging
import boto3
from botocore.exceptions import ClientError


# delcaring the name of the queue and the region it will be created in
QUEUE_NAME = 'my_sqs_queue'
REGION = 'us-east-1'


# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO, 
format='%(asctime)s: %(levelname)s: %(message)s')
sqs_resource = boto3.resource("sqs", region_name=REGION)


def create_queue(queue_name, ds, vt):
    #Creating a standard SQS queue
    try:
        response = sqs_resource.create_queue(QueueName=queue_name,
                                             Attributes={
                                                 'DelaySeconds': ds,
                                                 'VisibilityTimeout': vt
                                             })
    except ClientError:
        logger.exception(f'Could not create - {queue_name}.')
        raise
    else:
        return response
        

if __name__ == '__main__':
    # CONSTANTS

    ds = '0'
    vt = '60'
    output = create_queue(QUEUE_NAME, ds, vt)
    logger.info(
        f'{QUEUE_NAME} created. Queue URL - {output.url}')