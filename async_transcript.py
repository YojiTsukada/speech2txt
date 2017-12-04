import sys
import io
import os
import pymysql
import dbconfig

import time

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# check args file.
args = sys.argv


#if len(sys.argv) <= 1 :
#    print('you need to set audio file.')
#    sys.exit()

# Set filename
file_name = sys.argv[1]

# Debug mode
# The name of the audio file to transcribe
file_name = os.path.join(
    os.path.dirname("__file__"),
    'data',
    'english_mono.flac')



# Instantiates a client
client = speech.SpeechClient()


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


time_stamp = time.strftime('%Y-%m-%d %H:%M:%S')

# Connect Mysql
dbh = pymysql.connect(
    )


cnt = 0
for result in response.results:
    transcript = result.alternatives[0].transcript
    confidence = result.alternatives[0].confidence
    print('Transcript: {}'.format(transcript))
    print('Confidence: {}'.format(confidence))
#    print('Transcript: {}'.format(result.alternatives[0].transcript)," ")
#    print('Confidence: {}'.format(result.alternatives[0].confidence))

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


    # Insert処理
    with dbh.cursor() as cursor:
        sql = "INSERT INTO test (column1, create_date,update_date) VALUES (%s, %s, %s)"
        r = cursor.execute(sql, ( cnt, time_stamp,time_stamp))
        print(r)
        dbh.commit()



    # SQLを実行する
    with dbh.cursor() as cursor:
        sql = "SELECT * FROM test"
        cursor.execute(sql)

        # Select結果を取り出す
        results = cursor.fetchall()
        for r in results:
            print(r)

    dbh.close()
