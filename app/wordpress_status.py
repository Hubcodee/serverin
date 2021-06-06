# Server - Controller Node initiation script (Login Script)
import boto3
import os
import time
from pathlib import Path
import boto3.session
import sys
#from loaders import BarLoader

#loader = BarLoader()


# Resolving windows path
p = Path("C:/Users/chaud/Downloads/serverin-aws.pem").resolve()
print(p)
# Subnet ID
subnetId = 'subnet-21212849'
# Security Group
securityGroup = 'sg-0b0f28c9e1c68b7be'
# Image Id
imageId = "ami-0e5554737119c59e7"
# Instace type
instanceType = 't2.micro'
# key name
keyName = 'serverin-aws'

aws_session = boto3.Session(profile_name='aws')

def status_check():
    
    print("Status Check AWS Controller............\n")
    #loader.start()
    conn = aws_session.resource('ec2')
    instances = conn.instances.filter(
        Filters=[{'Name': 'tag:Name', 'Values': ['WP']}])
    flag_run = 0
    for instance in instances:
        if instance.state["Name"] == "running":
            print('Instance exists\n')
            flag_run = 1
            return instance.id



# fetching public ip


def get_public_dns(instance_id):
    ec2_client = aws_session.client("ec2")
    reservations = ec2_client.describe_instances(
        InstanceIds=[instance_id]).get("Reservations")
    print(f"fetching ip of instance :{instance_id}\n\n")
    for reservation in reservations:
        for instance in reservation['Instances']:
            return(instance.get("PublicDnsName"))


# instance_id = status_check()
# PublicDnsName = get_public_dns(instance_id) 
# print(f"Fetched IP : {PublicDnsName}\n\n")
