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
            aws_access_key_id='',
            aws_secret_access_key='',
            region="eu-"
        )
        self.dynamodb = boto3.resource(
            'dynamodb',
            aws_access_key_id='',
            aws_secret_access_key= '',
        )
        ddb_exceptions = self.client.exceptions

