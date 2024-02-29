import boto3
from datetime import datetime, timedelta

# Create a CloudWatch Logs client
client = boto3.client('logs', region_name='us-east-1')

# Specify the log group name and other parameters
log_group_name = '/aws/lambda/review_poc'

# Calculate start time as 24 hours ago from the current time
start_time = int((datetime.utcnow() - timedelta(hours=24)).timestamp()) * 1000
end_time = int(datetime.utcnow().timestamp()) * 1000

# Filter log events, sort by timestamp in descending order, and limit to 1 event
response = client.filter_log_events(
    logGroupName=log_group_name,
    startTime=start_time,
    endTime=end_time,
    limit=1,
    orderBy='LastEventTime',
    descending=True,
    filterPattern='ERROR'
)
print(response)

# Print the latest error log message, if available
if 'events' in response and response['events']:
    latest_error_event = response['events'][0]
    print("Timestamp:", latest_error_event['timestamp'])
    print("Message:", latest_error_event['message'])
else:
    print("No error logs found.")
