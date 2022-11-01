import json, csv, boto3, urllib
from datetime import datetime

s3 = boto3.resource('s3')
s3bucket = "formentries-ra"
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('test-table')
dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
   # Save file to S3 as a backup
   dt = datetime.now().strftime("%Y%m%d%H%M%S")
   uploaddate = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " UTC"
   filename = dt + "formentries.json"
   lambda_path = "/tmp/" + filename
   s3_path = "data/" + filename
   url = "https://finaltest-ra.s3.amazonaws.com/form.html"
   response = urllib.request.Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})
   urldata = urllib.request.urlopen(response).read()
   data = json.loads(urldata.decode())
   with open(lambda_path,'w') as outfile:
      json.dump(data, outfile)
   s3.meta.client.upload_file(lambda_path, s3bucket, s3_path)
  
  
  # Save information to dynamoDB table
    name = event['name']
    email = event['email']
    message = event['message']
    dynamodb.put_item(TableName='test-table', Item=
  {'name':{'S':name},'email':{'S':email}, 'message':{'S':message}})
    print(email)
