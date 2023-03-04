import boto3

class Database:
    ASAK = ""
    ASKI = ""

    def __init__(self):
        self.db = boto3
        self.client = None
        self.db = None

    def connect(self):
        self.client = boto3.client(
            'dynamodb',
            aws_access_key_id='AKIAZW5Y5IATVYH5VLH7',
            aws_secret_access_key='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',
            region="eu-west-1"
        )
        self.dynamodb = boto3.resource(
            'dynamodb',
            aws_access_key_id='',
            aws_secret_access_key= '',
        )
        ddb_exceptions = self.client.exceptions

