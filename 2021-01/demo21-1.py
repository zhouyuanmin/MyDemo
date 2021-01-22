import requests
import json
from pprint import pprint

url = "http://httpbin.org/post"
params = {'access_token': "1234567890"}
headers = {'Content-Type': 'application/json'}
data = {'text': "text", 'index': "index"}

# 注意观察data的值到底去了哪里 data = {'text': "text", 'index': "index"}
res1 = requests.post(url=url, headers=headers, params=params, data=json.dumps(data)).json()

res2 = requests.post(url=url, headers=headers, params=params, data=data).json()

res3 = requests.post(url=url, params=params, data=data).json()

# print(res1)
# print(res2)
# print(res3)

# 去除headers参数
res1.pop('headers')
res2.pop('headers')
res3.pop('headers')

# 去除origin参数
res1.pop('origin')
res2.pop('origin')
res3.pop('origin')

# 去除url参数
res1.pop('url')
res2.pop('url')
res3.pop('url')

# 去除files参数
res1.pop('files')
res2.pop('files')
res3.pop('files')

pprint(res1)
pprint(res2)
pprint(res3)
