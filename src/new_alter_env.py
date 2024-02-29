import boto3

class LambdaEnvironmentUpdater:
    def __init__(self, function_name='upload_poc', region='us-east-1'):
        self.function_name = function_name
        self.lambda_client = boto3.client('lambda', region_name=region)

    def update_lambda_environment(self, variable_name, variable_value):
        response = self.lambda_client.get_function_configuration(FunctionName=self.function_name)

        existing_environment = response.get('Environment', {})
        existing_variables = existing_environment.get('Variables', {})

        existing_variables[variable_name] = variable_value

        update_response = self.lambda_client.update_function_configuration(
            FunctionName=self.function_name,
            Environment={'Variables': existing_variables}
        )

        print(update_response)

# Example usage:
# Replace 'upload_sandbox' with your actual Lambda function name.
# Replace 'project_bucket' with the environment variable key.
# Replace 'security-release-review-automation-sandbox' with the new value for the environment variable.
updater = LambdaEnvironmentUpdater()
updater.update_lambda_environment(variable_name='project_bucket', variable_value='security-release-review-automation-poc')
