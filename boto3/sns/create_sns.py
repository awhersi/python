import boto3
import logging
from botocore.exceptions import ClientError


# declaring the name of the topic and the region it will be created in
topic_name = 'my_sns'
region = 'us-east-1'


# configuring the logger
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')
sns_client = boto3.client('sns', region_name=region)


#creating a SNS topic.
def create_topic(name):
    try:
        topic = sns_client.create_topic(Name=name)
        logger.info(f'SNS: {name} created.')
    except ClientError:
        logger.exception(f'Could not create SNS topic {name}.')
        raise
    else:
        return topic


if __name__ == '__main__':
    logger.info(f'Creating SNS topic: {topic_name}...')
    topic = create_topic(topic_name)