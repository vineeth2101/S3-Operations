import boto3

class ConfigUpload:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.s3_client = boto3.client('s3')

    def upload_file(self, component_name, file_path, local_file_path):
        # Construct the full key (object key) for the file
        key = f"{component_name}/{file_path}"

        # Upload the file to S3
        self.s3_client.upload_file(local_file_path, self.bucket_name, key)

        print(f"{local_file_path} uploaded to {key}")

# Example usage
if __name__ == "__main__":
    # Replace 'security_release_review_automation_bucket' with your actual bucket name
    bucket_name = 'security-release-review-automation-poc'

    # Create an instance of the S3FileManager class
    s3_file_manager = ConfigUpload(bucket_name)

    # Specify the component name, file path, and local file path for upload
    component_name = 'report'
    file_path = 'configurations/configuration.yaml'
    local_file_path = '/home/vineeth/Music/configuration.yaml'

    # Call the upload_file method
    s3_file_manager.upload_file(component_name, file_path, local_file_path)
