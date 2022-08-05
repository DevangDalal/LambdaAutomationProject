import json

def lambda_handler(event, context):
  print (json.dumps(event))
  return {
    'Status Code': 200,
    'Body': json.dumps("Hello from Lambda!")
  }
  
