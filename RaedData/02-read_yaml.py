import yaml


def read_yaml():
    with open('../DataPool/read_yaml.yaml','r',encoding='utf-8') as f:
       return yaml.load(f)

print(read_yaml())
