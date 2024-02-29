import boto3

class S3FileChecker:
    def __init__(self, bucket_name):
        """
        Initialize the S3FileChecker instance.

        Parameters:
        - bucket_name (str): The name of the S3 bucket.
        """
        self.bucket_name = bucket_name
        self.s3 = boto3.client('s3')

    def generate_file_path(self, component, folder, key):
        """
        Generate the file path using the provided components.

        Parameters:
        - component (str): The first component of the file path.
        - folder (str): The second component of the file path.
        - key (str): The third component (file name) of the file path.

        Returns:
        - str: The generated file path.
        """
        file_path = f"{component}/{folder}/{key}"
        return file_path

    def check_file_in_json_pointers(self, component, folder, key):
        """
        Check if the specified file exists in the S3 bucket.

        Parameters:
        - component (str): The first component of the file path.
        - folder (str): The second component of the file path.
        - key (str): The third component (file name) of the file path.
        """
        # Generate the file path using the provided components
        desired_file_path = self.generate_file_path(component, folder, key)

        # List objects in the specified bucket
        response = self.s3.list_objects_v2(Bucket=self.bucket_name)

        # Check if the desired file exists in the S3 bucket
        file_exists = any(obj['Key'] == desired_file_path for obj in response.get('Contents', []))

        print(f"File '{desired_file_path}' exists: {file_exists}")

if __name__ == "__main__":
    # Replace 'your_bucket_name' with the actual S3 bucket name
    bucket_name = 'security-release-review-automation-poc'

    # Create an instance of S3FileChecker
    s3_checker = S3FileChecker(bucket_name)

    # Replace the parameters with your desired values
    component = 'report'
    folder = 'scan_results/SECP-398_test/'
    key = 'SECP-398_test_collect_verify.json'

    # Check the file in S3
    check = s3_checker.check_file_in_json_pointers(component, folder, key)


