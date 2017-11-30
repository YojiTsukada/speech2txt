import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
file_name = os.path.join(
    os.path.dirname("__file__"),
    'data',
    'english_mono.flac')

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=44100,
        language_code='en-US',
        enable_word_time_offsets=True)

print('File is loading...')
operation = client.long_running_recognize(config,audio)

print('Waiting for operation to complete...')
response = operation.result()


cnt = 0
for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))
    print('Confidence: {}'.format(result.alternatives[0].confidence))

    for word_info in result.alternatives[0].words:
        word = word_info.word
        start_time = word_info.start_time
        end_time = word_info.end_time
        cnt += 1
        #print('{}, start_time: {}, end_time: {}'.format(
        #        word,
        #        start_time.seconds + start_time.nanos * 1e-9,
        #        end_time.seconds + end_time.nanos * 1e-9))
    print('WordCount: {}'.format(cnt))
    print('TotalTime: {}'.format(end_time.seconds + end_time.nanos * 1e-9))
    print("")
