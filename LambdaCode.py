import json
import boto3
import ast #to convert json str into dict
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    # first fetch the bucket name
    bucket = event['Records'][0]['s3']['bucket']['name']
    print("Bucket Name = " + bucket)
    
    # Fetch object name
    object = event['Records'][0]['s3']['object']['key']
    json_object = s3_client.get_object(Bucket=bucket, Key=object)
    print("Before decoding" + str(type(json_object))) #Decoding the object
    file_reader = json_object['Body'].read().decode("utf-8")
    print(type(file_reader))
    print(file_reader)
    file_reader = ast.literal_eval(file_reader) #Changing the json str into dict
    print(type(file_reader))
    print(file_reader)
    table = dynamodb.Table('LambdaProjectDB') #Specifying the table to put the object in
    table.put_item(Item = file_reader) #Pushing the object
    return "Success"
