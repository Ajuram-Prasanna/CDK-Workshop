import boto3

client = boto3.client('codepipeline')

response = client.list_pipelines()

print(response)