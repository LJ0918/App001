import yaml

data =  {'Search_Data': {
          'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'},
          'search_test_001': {'expect': [4, 5, 6], 'value': 456}}}
def write_yaml():
    with open('../DataPool/write_yaml.yaml', 'w',encoding='utf-8') as f:
        yaml.dump(data, stream=f, encoding='utf-8', allow_unicode=True)


write_yaml()