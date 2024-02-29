import boto3
import time

def check_lambda_logs(lambda_function_name, error_string, time_range_minutes=2):
    # Create a CloudWatch Logs client
    cloudwatch_logs = boto3.client('logs', region_name='us-east-1')


    # Calculate the start time for the query (last N minutes)
    start_time = int((time.time() - (time_range_minutes * 60)) * 1000)

    # Execute the filter query
    response = cloudwatch_logs.filter_log_events(
        logGroupName=f'/aws/lambda/{lambda_function_name}',
        startTime=start_time,
        limit=15,
        interleaved=True
    )


    # Check if the error string exists in any log event
    for event in response['events']:
        if error_string in event['message']:
            print(f"Error string '{error_string}' found in logs. Timestamp: {event['timestamp']}")
            return True

    print(f"Error string '{error_string}' not found in logs within the last {time_range_minutes} minutes.")
    return False

if __name__ == "__main__":
    # Replace these values with your Lambda function name and the error string you're looking for
    lambda_function_name = 'review_poc'
    error_string = "'Severity' key Not found, possibly file is corrupted or trivy schema is changed"

    # Call the function
    check_lambda_logs(lambda_function_name, error_string)