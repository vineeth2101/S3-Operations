import boto3


# Delete files in the json_pointers folder
s3 = boto3.client('s3')
json_pointers = s3.delete_object(
    Bucket='security-release-review-automation-poc',
    Key='report/json_pointers/SECP-398_piper.json'
)
print(json_pointers)

# Delete files in the scan_results folder
scan_results_files = [
    'SECP-398_collect_verify_SNYK.json',
    'SECP-398_collect_verify_TRIVY.json',
    'SECP-398_collect_verify.json'
]
for file_key in scan_results_files:
    response_scan_results = s3.delete_object(
        Bucket='security-release-review-automation-poc',
        Key=f'report/scan_results/{file_key}'
    )
    print(response_scan_results)


# Delete files in the summary_results folder
response_summary_results = [
    'SECP-398_summary.html',
    'SECP-398_summary.json'
]
for file_key in response_summary_results:
    response_summary_results = s3.delete_object(
        Bucket='security-release-review-automation-poc',
        Key=f'report/summary_results/{file_key}'
    )
    print(response_summary_results)

import boto3


# Delete files in the json_pointers folder
s3 = boto3.client('s3')
json_pointers = s3.delete_object(
    Bucket='security-release-review-automation-poc',
    Key='report/json_pointers/SECP-398_piper.json'
)
print(json_pointers)

# Delete files in the scan_results folder
scan_results_files = [
    'SECP-398_collect_verify_SNYK.json',
    'SECP-398_collect_verify_TRIVY.json',
    'SECP-398_collect_verify.json'
]
for file_key in scan_results_files:
    response_scan_results = s3.delete_object(
        Bucket='security-release-review-automation-poc',
        Key=f'report/scan_results/{file_key}'
    )
    print(response_scan_results)


# Delete files in the summary_results folder
response_summary_results = [
    'SECP-398_summary.html',
    'SECP-398_summary.json'
]
for file_key in response_summary_results:
    response_summary_results = s3.delete_object(
        Bucket='security-release-review-automation-poc',
        Key=f'report/summary_results/{file_key}'
    )
    print(response_summary_results)

