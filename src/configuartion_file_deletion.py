import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

class S3FileChecker:
    def __init__(self, bucket_name, s3_path):
        self.bucket_name = bucket_name
        self.s3_path = s3_path
        self.s3_client = boto3.client('s3')

    def generate_file_path(self, *components):
        """
        Generate the file path using the provided components.

        Parameters:
        - components (str): Components of the file path.

        Returns:
        - str: The generated file path.
        """
        file_path = '/'.join(components)
        return file_path

    def check_id_in_summary_html(self, id_to_check):
        """
        Check if the specified ID is present in the 'summary.html' file in the S3 bucket.

        Parameters:
        - id_to_check (str): The ID to check in the 'summary.html' file.

        Returns:
        - bool: True if the ID is present, False otherwise.
        """
        # Specify the components for the 'summary.html' file path
        components = [self.s3_path]

        # Generate the file path for 'summary.html'
        desired_file_path = self.generate_file_path(*components)

        # Download the content of 'summary.html' from S3
        response = self.s3_client.get_object(Bucket=self.bucket_name, Key=desired_file_path)
        html_content = response['Body'].read().decode('utf-8')

        # Check if the specified ID is present in the HTML content
        return id_to_check in html_content

# Example usage:
if __name__ == "__main__":
    # Replace 'your_bucket_name' and 'your_s3_path' with the actual values
    bucket_name = 'security-release-review-automation-poc'
    s3_path = 'report/summary_results/SECP-398_summary.html'

    # Create an instance of the S3FileChecker class
    s3_checker = S3FileChecker(bucket_name, s3_path)

    # Specify the ID to check
    id_to_check = 'CVE-2019-5827'

    # Check if the ID is present in 'summary.html'
    result = s3_checker.check_id_in_summary_html(id_to_check)

    # Explicit True/False return statement
    print(result)
