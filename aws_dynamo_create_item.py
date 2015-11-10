import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

table.put_item(
   Item={
        'username': 'Jon',
        'first_name': 'John',
        'last_name': 'Doe',
        'age': 100,
        'account_type': 'webmaster',
        }
)

table.put_item(
   Item={
        'username': 'J',
        'first_name': 'Jack',
        'last_name': 'Smith',
        'age': 100,
        'account_type': 'webmaster',
        }
)
