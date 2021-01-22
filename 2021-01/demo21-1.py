import requests
import json
from pprint import pprint

url = "http://httpbin.org/post"
params = {'access_token': "access_token"}
headers = {'Content-Type': 'application/json'}
data = {123: 456}

# 注意观察headers不同的时候，data的值到底去了哪里 data = {123: 456}
res1 = requests.post(url=url, headers=headers, data=json.dumps(data)).json()

res2 = requests.post(url=url, headers=headers, data=data).json()

res3 = requests.post(url=url, data=data).json()

pprint(res1)
pprint(res2)
pprint(res3)

"""
总结
添加 contentType：“application/json“之后，向后台发送数据的格式必须为json字符串，
不添加 contentType：“application/json“的时候可以向后台发送json对象形式
json字符串和json对象的区别
"""
