#%%

# create a S3 Bucket

import boto3
import json

client = boto3.client("s3")

#%%

response = client.create_bucket(Bucket="smy-jnew-bbucket-stest-rboto3")

print(json.dumps(response, indent=4))