# Updates pushed from GitHub repository
import json, csv, boto3, urllib
from datetime import datetime

s3 = boto3.resource('s3')
s3bucket = "finaltest-ra"
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('test-table')

def lambda_handler(event, context):
   # Save file to S3 as a backup
   dt = datetime.now().strftime("%Y%m%d%H%M%S")
   uploaddate = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " UTC"
   filename = dt + "_surveydata.json"
   lambda_path = "/tmp/" + filename
   s3_path = "data/" + filename
   url = "https://finaltest-ra.s3.amazonaws.com/form.html"
   response = urllib.request.Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})
   urldata = urllib.request.urlopen(response).read()
   data = json.loads(urldata.decode())
   with open(lambda_path,'w') as outfile:
      json.dump(data, outfile)
   s3.meta.client.upload_file(lambda_path, s3bucket, s3_path)
   # Save information to DynamoDB table
   objectpath = "https://" + s3bucket + ".s3.amazonaws.com/" + s3_path
   item = "{'uploaddate': {" + dt + "},'link': { " + s3_path + "}"
   item2 = "{'uploaddate': '34','link':  'microsoft'}"
   table.put_item(Item={'uploaddate': uploaddate ,'objectpath': objectpath })
   
