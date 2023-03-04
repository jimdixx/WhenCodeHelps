import io

import boto3

class Cloud:

    def __init__(self, bucket_name, region_name, aws_access_key_id, aws_secret_access_key):
        self.s3_client = None
        self.bucket_name = bucket_name
        self.region_name = region_name
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key

    def connect(self):
        self.s3_client = boto3.resource(
            's3',
            region_name=self.region_name,
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key
        ).Bucket(self.bucket_name)

    def upload(self, fName, userName=None):
        fo = io.BytesIO(fName)
        if userName != None:
            self.s3_client.upload_fileobj(fo, self.bucket_name, fName)
        else:
            self.s3_client.upload_fileobj(fo, self.bucket_name, userName + "_" + fName)
