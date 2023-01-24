import logging
import boto3
from botocore.exceptions import ClientError
REGION = 'us-east-1'
topic_name = 'week15_sns2'
# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')
sns_client = boto3.client('sns', region_name=REGION)

def create_topic(name):
    """
    Creates a SNS notification topic.
    """
    try:
        topic = sns_client.create_topic(Name=name)
        logger.info(f'Created SNS topic {name}.')
    except ClientError:
        logger.exception(f'Could not create SNS topic {name}.')
        raise
    else:
        return topic

if __name__ == '__main__':
    logger.info(f'Creating SNS topic {topic_name}...')
    topic = create_topic(topic_name)