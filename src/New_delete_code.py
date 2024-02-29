import boto3

# Initialize the S3 client
s3 = boto3.client('s3')
bucket_name = 'security-release-review-automation-poc'  # Replace with your bucket name


def delete_files_in_folder(prefix):
    """
    Delete files in the specified folder
    """
    paginator = s3.get_paginator('list_objects_v2')
    for page in paginator.paginate(Bucket=bucket_name, Prefix=prefix):
        objects = [{'Key': obj['Key']} for obj in page.get('Contents', [])]
        if objects:
            s3.delete_objects(Bucket=bucket_name, Delete={'Objects': objects})
            print(f"Deleted files in {prefix}")

def create_placeholder_file(folder):
    """
    Create a placeholder file in the folder
    """
    s3.put_object(Bucket=bucket_name, Key=folder + '.keep', Body='')
    print(f"Created placeholder in {folder}")


# List the top-level folders (components) in the bucket
response = s3.list_objects_v2(Bucket=bucket_name, Delimiter='/')
folders = [content['Prefix'] for content in response.get('CommonPrefixes', [])]

# Folders to exclude from deletion
exclude_folders = ['global_config/', 'configurations/']

for folder in folders:
    if folder in exclude_folders:
        continue

    subfolders_to_delete = ['json_pointers/', 'scan_results/', 'summary_results/']
    for subfolder in subfolders_to_delete:
        prefix = folder + subfolder
        delete_files_in_folder(prefix)
        create_placeholder_file(prefix)

print("File deletion process completed.")