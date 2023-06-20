# apigw-sqs-lambda-sns

Build:

`sam build`

Deploy:

`sam deploy --guided`

Invoke:

`curl https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/submit -X POST -H 'Content-Type: application/json' -d '{"foo":"bar","baz":"qux"}'`
