def process(event):
    print(event)


def say_hello():
    return "Hello World!"


def lambda_handler(event, context):
    process(event)
    return {'statusCode': 200,
            'body': say_hello()}
