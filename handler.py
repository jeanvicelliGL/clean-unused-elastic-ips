import boto3
import logging

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

def cleanip(event, context):
    """ Cleanup elastic IPs that are not being used """
    client = boto3.client('ec2')
    addresses_dict = client.describe_addresses()
    for eip_dict in addresses_dict['Addresses']:
        if "InstanceId" not in eip_dict:
            LOGGER.info(eip_dict['PublicIp'] +
                   " doesn't have any instances associated, releasing" )
            client.release_address(AllocationId=eip_dict['AllocationId'])
