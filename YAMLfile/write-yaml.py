import yaml
names_yaml = """
- 'eric'
- 'justin'
- 'mary-kate'
"""
names = yaml.safe_load(names_yaml)

with open('names.yaml','w') as file:
    yaml.dump(names, file)
print(open('names.yaml').read())
