import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

response = table.get_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    }
)

ritem = response['Item']

for key, value in ritem.iteritems():
    print (str(key) + ":  " + str(value))

