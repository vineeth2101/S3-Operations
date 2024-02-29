import boto3

s3 = boto3.client('s3')

# Replace 'security_release_review_automation_bucket' with your actual bucket name
bucket_name = 'security-release-review-automation-poc'

components = ['comment', 'report']

for component in components:
    # Delete files in the json_pointers folder
    json_pointers_key = f'{component}/json_pointers/'
    json_pointers_files = ['SECP-398_piper.json']
    for file_key in json_pointers_files:
        response_json_pointers = s3.delete_object(
            Bucket=bucket_name,
            Key=f'{json_pointers_key}{file_key}'
        )
        print(response_json_pointers)

    # Delete files in the scan_results folder
    scan_results_key = f'{component}/scan_results/'
    scan_results_files = ['SECP-398_collect_verify_SNYK.json', 'SECP-398_collect_verify_TRIVY.json','SECP-398_collect_verify.json']  # Add the actual file names
    for file_key in scan_results_files:
        response_scan_results = s3.delete_object(
            Bucket=bucket_name,
            Key=f'{scan_results_key}{file_key}'
        )
        print(response_scan_results)

    # Delete files in the summary_results folder
    summary_results_key = f'{component}/summary_results/'
    summary_results_files = ['SECP-398_summary.html', 'SECP-398_summary.json']
    for file_key in summary_results_files:
        response_summary_results = s3.delete_object(
            Bucket=bucket_name,
            Key=f'{summary_results_key}{file_key}'
        )
        print(response_summary_results)
