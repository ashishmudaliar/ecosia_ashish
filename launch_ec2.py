import sys
import boto3
import argparse

parser = argparse.ArgumentParser(description='AWS EC2 Launch Instance parser')
parser.add_argument('-a','--access_key_id', help='Access key id',required=True)
parser.add_argument('-s','--secret_access_key', help='Secret Access Key',required=True)
parser.add_argument('-r','--aws_region', help='AWS Region',required=True)
parser.add_argument('-i','--instance_type', help='Instance Type',required=True)

args = parser.parse_args()
AWS_ACCESS_KEY_ID = args.access_key_id
AWS_SECRET_ACCESS_KEY = args.secret_access_key
AWS_REGION = args.aws_region
INSTANCE_TYPE = args.instance_type

client = boto3.resource('ec2',
                      aws_access_key_id = AWS_ACCESS_KEY_ID,
                      aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
                      region_name = AWS_REGION)

instance = client.create_instances(
    ImageId = 'ami-e22aaa8d',
    MinCount=1,
    MaxCount=1,
    InstanceType=INSTANCE_TYPE
)
print("Instance launched")
print("Instance Launch Time")
print(instance[0].launch_time)
