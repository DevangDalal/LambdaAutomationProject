Prerequisites -
- Create a Lambda function LambdaProjectFunc (name it anything you like).
- Create an IAM role with the necessary permissions for Lambda to access S3, DynamoDB and CloudWatch and assign the role to our Lambda function.
- Create a DynamoDB Table LambdaProjDB and set the partition key to ID.
- Create an s3 bucket lambdaprojbucket.

Execution -
- Test the Lambda function to check if it's pushing the logs to CloudWatch Logs.
- Edit the default Lambda code to TestLambdaCode.py.
- The execution result should show the keys and the values of the test file.
- Add an S3 trigger to the function to execute it as soon as a .json object is put into the bucket and choose the lambdaprojbucket.
- Upload a sample.json file to the s3 bucket.
- Go to CloudWatch logs to check if a new log stream is created.
- Copy the .json dump from the execution log of the function triggered by  file upload and paste it in the test function in lambda.
- This json will provide us everything required in out Boto3 code.
- Benefit of updating the contents of the test function is that we wont have to upload a .json file to our s3 bucket again and again. We can directly test it.

Function - 
- We have to first get the object, ie, as soon as the file is uploaded we want to fetch the contents of the object, process the contents and then push them into our DynamoDB table.
- We updated our LambdaCode.py to fetch the object information.
- By testing you'll get the metadata of the object you uploaded to the bucket.
- Now, inside the json metadata we're interested in the "Body" segment of the code.
-  The response to testing the functions is going to show the contents of the .json file you uploaded to your s3 bucket.
- Now, we have to convert the json str into dict because when we're going to use the put_item in DynamoDB, in the method the argument that we have to pass has to be a dict. Have to import ast module in the code to use the literal_eval function to covert str into dict.

Pushing the data into DynamoDB -
- We're going to use the resource table method to push the data.
- For the resource section we're going to use the table = dynamodb.Table('Name')
- And then we'll pass the put_item method to put the item into DynamoDB table. the item should be a dictionary.
                   table.put_item(Item = file_reader)
- After executing the function check the table and there would be a new entry in the table with the contents of sample.json file that you uploaded to your s3 bucket.


Imp - Don't forget to delete all the resources you created for this project to not incur charges.
