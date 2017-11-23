# Google Speech
# Python

- google cloud sdk
- Python3


syncrecognize
```
$ curl -s -X POST -H "Content-Type: application/json" --data-binary @english.json "https://speech.googleapis.com/v1/speech:recognize?key={API_KEY}"
```


asyncrecognize
```
curl -s -X POST -H "Content-Type: application/json" --data-binary @async.json "https://speech.googleapis.com/v1/speech:longrunningrecognize?key={API_KEY}"

GET https://speech.googleapis.com/v1/operations/YOUR_OPERATION_NAME?key=YOUR_API_KEY

curl -s -X POST "https://speech.googleapis.com/v1/operations/2937039889255085091?key={API_KEY}"
```
