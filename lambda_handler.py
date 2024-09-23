
import subprocess
import json
import os
import boto3
from botocore.exceptions import NoCredentialsError

# Initialize S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # Get inputs from environment variables
        account_number = os.environ.get('account_number', 'default_account_number')
        account_name = os.environ.get('account_name', 'default_account_name')
        path = os.environ.get('path', '/tmp')  # Using /tmp for temporary storage

        # Path to the Python script (assuming it’s in the same directory)
        script_path = os.path.join(os.path.dirname(__file__), 'terraform-plan.py')

        # Capture the output of your Python script
        result = subprocess.run(
            ['python3', script_path, account_number, account_name, path],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            output = result.stdout

            # S3 Bucket and Object (File) information
            bucket_name = 'terraform-s3-remote-backend-files'
            output_file_key = 'plan.json'

            # Upload output to S3
            upload_to_s3(bucket_name, output_file_key, output)

            return {
                'statusCode': 200,
                'body': json.dumps({
                    'message': 'Script executed and output uploaded to S3 successfully',
                    'output': output
                })
            }
        else:
            return {
                'statusCode': 500,
                'body': json.dumps({
                    'message': 'Script execution failed',
                    'error': result.stderr
                })
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'Error occurred',
                'error': str(e)
            })
        }

def upload_to_s3(bucket, key, data):
    try:
        s3.put_object(Bucket=bucket, Key=key, Body=data)
        print(f'Successfully uploaded to {bucket}/{key}')
    except NoCredentialsError:
        print("Credentials not available")
    except Exception as e:
        print(f"Failed to upload to S3: {e}")
