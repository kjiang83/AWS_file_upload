import boto3
import os
from dotenv import load_dotenv
import schedule
import time

# uploads file to specific aws bucket

"""""
def aws_updater():
"""
# load your env file to get your access keys
load_dotenv()

ACCESS_KEY_ID = os.getenv('ACCESS_KEY_ID')
SECRET_ACCESS_KEY = os.getenv('SECRET_ACCESS_KEY')

client = boto3.client(
    's3',
    aws_access_key_id = 'ACCESS_KEY_ID',
    aws_secret_access_key = 'SECRET_ACCESS_KEY',
)

client.upload_file(
    # local file name
    r"path to file you want to upload",
    # bucket name
    'your_bucket_name',
    # remote file name
    'name of remote file you upload',
)

""""
schedule.every().day.at('00:00').do(aws_updater)
while 1:
    schedule.run_pending()
    time.sleep(1)
"""