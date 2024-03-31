"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket(
    'my-bucket',
    bucket="honglab-pulumi-test",
    tags={
        "Name": "어쩌고",
        "Env": "저쩌고"
    }
)

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)
