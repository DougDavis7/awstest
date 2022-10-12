# Testing out AWA Boto3 api

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




try:
    import boto3
    print("Module boto3 installed")
except ModuleNotFoundError:
    print("Module boto3 not installed")

from datetime import datetime
from datetime import timedelta

#
# Option 1: S3 client list of buckets with name and is creation date
#



cost = boto3.client('ce')

response = cost.get_cost_and_usage(
    TimePeriod={
        'Start': (datetime.today()-timedelta(days=30)).strftime('%Y-%m-%d'),
        'End': datetime.today().strftime('%Y-%m-%d')
    },
    Granularity='MONTHLY',
    Metrics=[
        'AmortizedCost',
    ]
)

print(response)

response = cost.get_cost_and_usage(
    TimePeriod={
        'Start': (datetime.today()-timedelta(days=30)).strftime('%Y-%m-%d'),
        'End': datetime.today().strftime('%Y-%m-%d')
    },
    Granularity='DAILY',
    Metrics=[
        'AmortizedCost',
    ]
)

print(response)

#EC2 Tests
ec2 = boto3.client('ec2')
#instance = ec2.instance('i-0d91723c63ee95f90')


response = ec2.describe_instances()
print(response)

#s3 Tests
s3 = boto3.client('s3')
#s3 = boto3.client('s3')
response = s3.list_buckets()['Buckets']
for bucket in response:
    print('Bucket name: {}, Created on: {}'.format(bucket['Name'], bucket['CreationDate']))
