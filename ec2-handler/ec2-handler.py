import json
import boto3

def lamda_handler(event, context):
  body = json.loads(event['body'])
  region = body['region']
  instances = body['instances']
  ec2 = boto3.client('ec2', region_name=region)
  if body['action'] == 'start':
    ec2.start_instances(InstanceIds=instances)
    return 0
  elif body['action'] == 'stop':
    ec2.stop_instances(InstanceIds=instances)
    return 0
  else:
    return 1