from flask import Flask
import os
import boto3
import json
import random
import string
import pymongo
import config
import ssl
import datetime

from pymongo import MongoClient
app = Flask(__name__)
mongoclient = pymongo.MongoClient(config.MONGO_CLIENT_URL, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
s3client = boto3.client('s3')
db = mongoclient['data']

@app.route('/')
def hello_world():
    return 'Hello, World!'

s3 = boto3.resource('s3')
image_folder = os.getcwd()

# Generates a random string with alphanumeral 10 digit
def randomStringDigits(stringLength=10):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

# Uploads image to s3 bucket
def upload_image(key):
    s3.meta.client.upload_file(image_folder + '/image/2.png', 'freebee-beanpot', key)
    return "Upload success"

# Passes image to AWS Rekognition and returns objects within the image
def detect_labels(bucket, key, max_labels=10, min_confidence=90, region="us-east-1"):
    rekognition = boto3.client("rekognition", region)
    response = rekognition.detect_labels(
        Image = {
			    "S3Object": {
				"Bucket": bucket,
				"Name": key,
            }
		},
		MaxLabels=max_labels,
		MinConfidence=min_confidence,
	)
    print(response['Labels'])
    list_of_items = {}
    for obj in response['Labels']:
        if obj['Name'] not in list_of_items:
            list_of_items[obj['Name']] = 1
        else:
            continue
    return list_of_items


@app.route('/process')
def upload_and_process():
    key = randomStringDigits()
    bucket = 'freebee-beanpot'
    # uploads image with random key genereated
    upload_image(key)

    # passes the image into rekognition api
    result = detect_labels(bucket, key)

    # store result in the database
    collection = db['info']
    post = {
        "info": result,
		"date": datetime.datetime.utcnow(),
        "location": 0
    }
    x = collection.insert_one(post).inserted_id
    print(x)
    return "done!"

@app.route('/buckets')
def list_buckets():
    response = s3client.list_buckets()
    print(response)
    return 'it works!'

if __name__ == '__main__':
   app.run()
