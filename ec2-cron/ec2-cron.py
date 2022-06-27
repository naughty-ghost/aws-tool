import boto3

def lambda_handler(event, context):
  region = event['Region']
  instances = event['Instances']
  ec2 = boto3.client('ec2', region_name=region)
  if event['Action'] == 'start':
    ec2.start_instances(InstanceIds=instances)
  elif event['Action'] == 'stop':
    ec2.stop_instances(InstanceIds=instances)
  else:
    return 1
  return 0