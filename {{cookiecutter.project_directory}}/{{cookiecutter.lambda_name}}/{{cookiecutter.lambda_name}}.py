def process(event):
    print(event)


def lambda_handler(event, context):
    process(event)
    return {'statusCode': 200,
            'body': "Hello World!"}
