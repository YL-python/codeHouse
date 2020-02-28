import json

fill_path = 'E:\PyCharm2019\data-analysis\start_pandas\herolist.json'

data_str = open(fill_path, encoding='utf-8').read()

if data_str.startswith(u'\ufeff'):
    data_str = data_str.encode('utf-8')[3:].decode('utf-8')

data_list = json.loads(data_str, encoding='utf-8')

js = json.dumps(data_list, sort_keys=True, indent=4, separators=(',', ':'))

print(js)
