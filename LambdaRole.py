{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "dynamodb:PutItem",
                "dynamodb:DeleteItem",
                "s3:ListJobs",
                "dynamodb:Query",
                "dynamodb:UpdateItem",
                "s3:ListBucket",
                "dynamodb:DeleteTable",
                "s3:PutObject",
                "s3:GetObject",
                "s3:ListAllMyBuckets",
                "cloudwatch:*",
                "dynamodb:GetItem",
                "dynamodb:UpdateTable",
                "s3:GetObjectVersion"
            ],
            "Resource": "*"
        }
    ]
}
