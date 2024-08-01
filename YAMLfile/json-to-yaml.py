import yaml
import json

with open('config.json', 'r') as file:
    configuration = json.load(file)

with open('config.yaml', 'w') as yaml_file:
    yaml.dump(configuration, yaml_file)

with open('config.yaml', 'r') as yaml_file:
    print(yaml_file.read())