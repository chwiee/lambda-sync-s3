import boto3 json

s3 = boto3.resource(‘s3’)

def lambda_handler(event, context):
  origin_bucket   = s3.Bucket(os.environ.get('BUCKET_ORIGIN'))
  target_bucket   = s3.Bucket(os.environ.get('BUCKET_TARGET')) 
  for obj in bucket.objects.all():
    dest_key      = obj.key
    print(f'Moving - {dest_key} to s3://{target_bucket}')
    s3.Object(dest_bucket.name, dest_key).copy_from(CopySource = {‘Bucket’: obj.bucket_name, ‘Key’: obj.key})
