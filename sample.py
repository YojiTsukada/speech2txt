import io
import os
import time

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

client = speech.SpeechClient()

operation = client.long_running_recognize(
     audio=speech.types.RecognitionAudio(
         uri='gs://backet20171122/english_mono.flac',
     ),
     config=speech.types.RecognitionConfig(
         encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
         language_code='en-US',
         sample_rate_hertz=44100,
     ),
 )


operation.result()

retry_count = 100


while retry_count > 0 :
     retry_count -= 1
     time.sleep(10)
     operation.poll()  # API call

for result in operation.results:
     for alternative in result.alternatives:
         print('=' * 20)
         print(alternative.transcript)
         print(alternative.confidence)
