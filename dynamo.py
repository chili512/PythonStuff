import boto3


def batch():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Books')
    response = table.get_item(Key={
        'Isbn': '46456-8987898'
    })

    print(response)

    with table.batch_writer() as batch:
        for i in range(50):
            batch.put_item(
                Item={
                    'Isbn': str(i * 999),
                    'Author': 'write' + str(i),
                    'Title': 'title' + str(i),
                    'Cost': i,
                    'Edition': i,
                    'Published': 2019
                }
            )


batch()
