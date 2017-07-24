import boto3

client = boto3.client('lex-models')
response = client.put_intent(
    name='WikipediaBot',
    description='A bot to query wikipedia',
    slots=[
        {
            'name': 'name',
            'description': 'Query String',
            'slotConstraint': 'Required',
            'slotType': 'AMAZON.Actor',
            'slotTypeVersion': '1',
            'valueElicitationPrompt': {
                'messages': [
                    {
                        'contentType': 'PlainText',
                        'content': 'string'
                    },
                ],
                'maxAttempts': 123,
                'responseCard': 'string'
            },
            'priority': 123,
            'sampleUtterances': [
                'string',
            ],
            'responseCard': 'string'
        },
    ],
    sampleUtterances=[
        'I want to search for {name}',
        'Search wikipedia for {name}'
    ],
    confirmationPrompt={
        'messages': [
            {
                'contentType': 'PlainText',
                'content': 'string'
            },
        ],
        'maxAttempts': 123,
        'responseCard': 'string'
    },
    rejectionStatement={
        'messages': [
            {
                'contentType': 'PlainText',
                'content': 'string'
            },
        ],
        'responseCard': 'string'
    },
    followUpPrompt={
        'prompt': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML',
                    'content': 'string'
                },
            ],
            'maxAttempts': 123,
            'responseCard': 'string'
        },
        'rejectionStatement': {
            'messages': [
                {
                    'contentType': 'PlainText'|'SSML',
                    'content': 'string'
                },
            ],
            'responseCard': 'string'
        }
    },
    conclusionStatement={
        'messages': [
            {
                'contentType': 'PlainText'|'SSML',
                'content': 'string'
            },
        ],
        'responseCard': 'string'
    },
    dialogCodeHook={
        'uri': 'string',
        'messageVersion': 'string'
    },
    fulfillmentActivity={
        'type': 'ReturnIntent'|'CodeHook',
        'codeHook': {
            'uri': 'string',
            'messageVersion': 'string'
        }
    },
    parentIntentSignature='string',

    # When you create a new intent, leave the checksum field blank. If you specify a checksum you get a BadRequestException exception
    # When you want to update a intent, set the checksum field to the checksum of the most recent revision of the $LATEST version.
    checksum=''
)