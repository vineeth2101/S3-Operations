import boto3

def check_lambda_logs(lambda_function_name, error_string, region='us-east-1', time_range_minutes=20):
    # Initialize the CloudWatch Logs client
    cloudwatch_logs = boto3.client('logs', region_name=region)

    # Specify the log group for the Lambda function
    log_group_name = f'/aws/lambda/{lambda_function_name}'

    # Describe log streams and get the latest one
    response = cloudwatch_logs.describe_log_streams(
        logGroupName=log_group_name,
        orderBy='LastEventTime',
        descending=True,
        limit=1
    )

    # Check if any log streams are available
    if 'logStreams' in response and response['logStreams']:
        latest_log_stream_name = response['logStreams'][0]['logStreamName']

        # Fetch log events for the latest log stream
        log_events_response = cloudwatch_logs.get_log_events(
            logGroupName=log_group_name,
            logStreamName=latest_log_stream_name,
            limit=50,
            startFromHead=True
        )

        # Find and print the latest error message
        for event in log_events_response['events']:
            message = event['message']
            if error_string in message:
                print(f"Latest Error in {latest_log_stream_name}: {message}")
                return True  # Error string found

        print(f"No error matching '{error_string}' found in the latest logs.")
    else:
        print(f"No log streams found in log group {log_group_name}.")

    return False  # Error string not found

if __name__ == "__main__":
    # Replace these values with your Lambda function name, error string, and AWS region
    lambda_function_name = 'review_poc'
    error_string = 'Empty file read by review lambda from s3 bucket'
    aws_region = 'us-east-1'

    # Call the function
    check_lambda_logs(lambda_function_name, error_string, region=aws_region)
