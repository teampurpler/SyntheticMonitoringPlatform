import os
import yaml

# Print current working directory
print(f"Current Working Directory: {os.getcwd()}")

# Define file path (relative or absolute)
file_path = 'config.yml'

# Check if file exists
if not os.path.isfile(file_path):
    print(f"File not found: {file_path}")
else:
    try:
        # Read the YAML file
        with open(file_path, 'r') as file:
            configuration = yaml.safe_load(file)
        print(configuration)
    except yaml.YAMLError as exc:
        print(f"Error in YAML file: {exc}")
    except Exception as e:
        print(f"An error occurred: {e}")
