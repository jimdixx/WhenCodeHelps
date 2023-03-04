import boto3

class Database:
    def __init__(self, table_name, region_name, aws_access_key_id, aws_secret_access_key):
        self.table_name = table_name
        self.region_name = region_name
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.client = None
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key

        self.table = None

    def connect(self):
        self.table = boto3.resource(
            'dynamodb',
            region_name=self.region_name,
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key
        ).Table(self.table_name)

    def put_item(self, item):
        try:
            self.table.put_item(Item=item)
            return True
        except self.client.exceptions.ConditionalCheckFailedException as e:
            print(e)
            return False

    def get_item(self, key):
        try:
            response = self.table.get_item(Key=key)
            return response.get('Item')
        except self.client.exceptions.ClientError as e:
            print(e.response['Error']['Message'])
            return None

if __name__ == "__main__":


    # Retrieve an item by its primary key
    key = {'id': 'your_key_value'}
    item = db.get_item(key)
    print(item)

"""
autorizace služby v aws:
    - IAM služba (Identity access manegement)

musím se autorizovat jako nějaký uživatel
"""