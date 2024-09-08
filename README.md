# env_variable_and_secrets
Environment_variable_test

This example shows how to use environment variables and secrets in a Python application.

# Defining an environment Variable
Can be used to store any data. It is a key-value pair. Environments variable are accessable in our workflow file. It can be defined in the workflow file (at workflow label or job labels) or in the repository settings.

Example:
```yaml

name: Environment Variable Example
on: [push]
env: # Define the environment variable at the workflow level, it will be available to all jobs and steps
  USER: "amishra"
  EMAIL: "amishkumar562@gmail.com"
  TEST_VAR: "This is a test variable"
jobs:
  build:
    runs-on: ubuntu-latest
    env:
      ENV_VAR: "Hello, World!" # Define the environment variable at the job level, it will be available to all steps in the job
      TEST_VAR: "This is a jon variable" # Define the environment variable at the job level, it will be available to all steps in the job. It will override the workflow level environment variable with the same name
    steps:
      - name: Print the value of the ENV_VAR environment variable
        run: echo $ENV_VAR ${{ env.USER }} ${{ env.EMAIL }} ${{ env.TEST_VAR }}
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Print the value of the ENV_VAR environment variable
        run: echo $ENV_VAR ${{ env.USER }} ${{ env.EMAIL }} ${{ env.TEST_VAR }}
      - name: Print the value of the TEST_VAR environment variable
        run: echo $ENV_VAR # This will print the value of the environment variable defined at the job level, since it is not defined at the step level, it will not be available to the step
```

# Defining a Secret
Secrets are encrypted environment variables that are defined in the repository settings. They are not accessible in the workflow file. They can be used to store sensitive data like passwords, tokens, etc.

Example:
```yaml
name: Secret Example
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Print the value of the SECRET environment variable
        run: echo ${{ secrets.MONGODB_USERNAME }} ${{ secrets.MONGODB_PASSWORD }} # Access the secret environment variable
```

# Using Environment Variables and Secrets in a Python Application
This example shows how to use environment variables and secrets in a Python application.

Example:
```python
import os
# Get MongoDB credentials from environment variables
username = os.getenv('MANGODB_USERNAME')
password = os.getenv('MANGODB_PASSWORD')
host = os.getenv('MANGODB_CLUSTER_ADDRESS', 'localhost')  # Default to localhost if not set
port = os.getenv('MONGODB_PORT', '3000')  # Default MongoDB port
database_name = os.getenv('MONGODB_DATABASE')

print(f"Connecting to MongoDB at {host}:{port}...")
print(f"Database: {database_name}")
print(f"Username: {username}")
print(f"Password: {password}")
```

# Conclusion
Environment variables and secrets can be used to store sensitive data and access them in a Python application. They can be defined at the workflow level, job level, or step level in the workflow file, or in the repository settings as secrets. They can be accessed in the Python application using the `os.getenv()` function.