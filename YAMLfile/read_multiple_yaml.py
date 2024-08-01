import yaml


with open('multi_doc.yml', 'r') as file:
    docs = yaml.safe_load_all(file)

    for doc in docs:
        print(doc)
        