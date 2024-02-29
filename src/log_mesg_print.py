import boto3

# Initialize the CloudWatch Logs client
cloudwatch_logs = boto3.client('logs',  region_name='us-east-1')

# Specify the log group
log_group_name = '/aws/lambda/review_poc'

try:
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
            if 'ERROR' in message:
                print(f"Latest Error in {latest_log_stream_name}: {message}")
                break  # Stop iterating after the first error message is found
    else:
        print(f"No log streams found in log group {log_group_name}.")

except Exception as e:
    print(f"Error: {str(e)}")
