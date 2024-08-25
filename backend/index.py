from flask import Flask, request, jsonify, send_file, Response # type: ignore
from flask_cors import CORS # type: ignore
import pyaudio # type: ignore
import json


from boto3 import Session # type: ignore
import boto3 # type: ignore
from botocore.exceptions import BotoCoreError, ClientError # type: ignore
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir
import speech_recognition as sr # type: ignore

app = Flask(__name__)
CORS(app)



# Create a client using the credentials and region defined in the [adminuser]
# section of the AWS credentials file (~/.aws/credentials).
polly = boto3.client("polly", 
                     aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                     aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                    region_name=os.getenv('AWS_REGION')) # type: ignore

lambda_client = boto3.client("lambda", 
                     aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                     aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                    region_name=os.getenv('AWS_REGION')) # type: ignore



def invoke_lambda(text):
    event_payload = {
        "user_q": text,
    }

    response = lambda_client.invoke(
        FunctionName=os.getenv('FUNCTION_NAME'),
        InvocationType='RequestResponse',
        Payload=json.dumps(event_payload)
    )

    response_payload = response['Payload'].read().decode('utf-8')
    result = json.loads(response_payload)
    message = json.loads(result['body'])['message']


    return message

recognizer = sr.Recognizer()
MICROPHONE_DEVICE_INDEX = int(os.getenv('MICROPHONE_DEVICE_INDEX', 0))


#@app.route('/synthesize', methods=['POST'])
def synthesize_speech(text):
    response = polly.synthesize_speech(
        Text=text,
        OutputFormat="pcm",  # Use PCM format for direct audio stream
        VoiceId="Joanna"
    )

    # Check if the response contains the audio stream
    if "AudioStream" in response:
        # Use PyAudio to play the audio directly
        audio_stream = response['AudioStream'].read()

        # Initialize PyAudio
        p = pyaudio.PyAudio()

        # Open a stream to play the PCM audio
        stream = p.open(format=p.get_format_from_width(2),  # 16-bit audio
                        channels=1,                         # Mono audio
                        rate=16000,                         # 16kHz sampling rate
                        output=True)

        # Play the audio
        stream.write(audio_stream)

        # Cleanup
        stream.stop_stream()
        stream.close()
        p.terminate()
    else:
        print("Error: No AudioStream in response")

@app.route('/activate', methods=['POST'])
def activate_assistant():
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = recognizer.listen(source)
            query = recognizer.recognize_google(audio)
            print(f"User said: {query}")
            response = {'response': query}
            print(response)
            synthesize_speech(invoke_lambda(query.lower()))
            return response
    except Exception as e:
        return {'error': str(e)}, 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
