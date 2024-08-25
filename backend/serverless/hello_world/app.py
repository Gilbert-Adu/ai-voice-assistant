import json

# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    actions = {
    "hello": "Hello! How can I assist you today?"
,

    "what is your name": "My name is Gilbert. I am an example of the Gino's digital voice assistant."
,

    "how are you": "I'm doing great, thank you!"
,

    "exit": "Goodbye"
,

    "quit": "Goodbye"
,

    "what can you do": "I have very limited capabilities because I am only a pre-demo voice assistant but at the moment, I can answer questions regarding the capabilities of Gilbert the human and Gino's digital. Gilbert is a software developer with experience in building frontend and backend of software programs. He can build for web, mobile, VR, and custom hardware devices. He can build in Python, Node JS, and Java. Would you like to know more about Gino's digital?"
,
    "yes": "Gino's digital is a small non-incorporated software company that Gilbert runs out of his home office in Ithaca, NY. Hiring Gino's digital is the same as hiring Gilbert. I should mention though that Gilbert is open to fulltime Software developer roles. On-site or remote.",

    "what is gino's digital": "Gino's digital is a small non-incorporated software company that Gilbert runs out of his home office in Ithaca, NY. Hiring Gino's digital is the same as hiring Gilbert. I should mention though that Gilbert is open to fulltime Software developer roles. On-site or remote."
,

    "who is gilbert": "Gilbert is a pretty cool dude. He graduated from Cornell University in 2022 with a degree in Computer Science and Communication and can build anything with any tool required of him. He absolutely loves cloud computing especially with AWS, creating and orchestrating microservice architecture, and serverless applications. He's a lifelong learner and appreciates challenges with open arms so what new challenge do you have for the big guy huh?"
}

    result = actions[event['user_q']]


    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": result,
            # "location": ip.text.replace("\n", "")
        }),
    }
