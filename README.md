# fixerio_scrape
Scrape Fixio rates everyday at 9am


## Set up repo
```
./scripts/bootstrap.sh
```

## Run tests
```
./scripts/run_tests.sh
```

## Set up
Download (AWS CLI)[https://docs.aws.amazon.com/cli/latest/userguide/installing.html]


## Build zip file
The application will run inside a lambda function. We use docker to build the packages required for running on lambda.
```
./scripts/build_zip.sh
```

## Create S3 bucket
```
aws s3api create-bucket --bucket fixerio-example --region us-west-2 --create-bucket-configuration LocationConstraint=us-west-2
```

## Create IAM role
The lambda function will need access to the s3 bucket created above. We need to create an IAM role to associate it with the lambda role. 
```
aws iam create-role --role-name fixerio-lambda * To Be Finished *
```

## Create Lambda function
Create the lambda on aws
```
aws lambda create-function \
--region us-west-2 \
--function-name fixerio \
--zip-file fileb://build/fixerio_scrape.zip \
--handler app.handler \
--role fixerio-lambda \
--runtime python3.6 \
--environment Variables="{ACCESS_KEY=$ACCESS_KEY,S3_BUCKET=$S3_BUCKET}"
```

## Create cloudwatch event
AWS cloudwatch events will be used to trigger the lambda function every weekday.
```
* To be finished *
```
