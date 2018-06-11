def add_2(number: float):
    return number + 2


def say_hello():
    return "Hello World!"


def lambda_handler(event, context):
    return {'statusCode': 200,
            'body': say_hello()}
