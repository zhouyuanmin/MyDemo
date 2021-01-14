# -*- coding:utf-8 -*-
import requests
import random

# 错误代码
ERROR_DICT = {
    '2': '后端连接超时请重试',
    '52001': '请求超时请重试',
    '52002': '系统错误请重试',
    '52003': '未授权用户',
    '52004': '输入解析失败',
    '52005': '输入字段有误',
    '52006': '输入文本长度不超过5',
    '52007': '输入文本包含政治&黄色内容',
    '52008': '后台服务返回错误请重试',
    '54003': '访问频率受限',
    '54100': '查询接口参数为空',
    '54102': '无写诗结果请重试'
}


# 获取 token
def get_token_key():
    token_key = ''
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    client_id = '7g8aoTy711jgt1ZXzVk8hji2'
    client_secret = 'mKcz1LekI3sL1QupRKrm8QzTfYDKkENu'

    url = f'https://aip.baidubce.com/oauth/2.0/token?' \
          f'grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}'
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    response = requests.get(url=url, headers=headers)
    token_info = response.json()
    if token_info:
        token_key = token_info['access_token']

    return token_key


# 调用百度 AI 智能春联和智能写诗接口
def nlp_result(text, token_key, index=0, way='poem'):
    """
    调用该函数返回生成的春联或者七言诗
    :param text: 春联或诗的主题（官方限制不超过 5 个字符）
    :param token_key: 通过调用 get_token_key() 获取的 token
    :param index: 不同的 index 会输出不同的春联和诗
    :param way: 通过传入该参数确认是生成对联还是生成诗，“poem”为写七言诗，“couplets”为写春联
    :return: 获取的数据
    """
    assert way in ['poem', 'couplets'], 'type should be poem or couplet'
    access_token = token_key
    url = f'https://aip.baidubce.com/rpc/2.0/creation/v1/{way}?access_token={access_token}'
    params = {
        'text': text,
        'index': index
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url=url, params=params, headers=headers)
    data = response.json()
    print(f'[debug]{data}')
    return data


# 解析生成的春联
def parse_couplets(data):
    """
    解析调用智能春联生成的数据
    :param data: 调用智能春联生成的有效数据
    :return: 横批（center）、上联（first）和下联（second）
    """
    center = data['couplets']['center']
    first = data['couplets']['first']
    second = data['couplets']['second']
    # print(f'上联：{first}')
    # print(f'下联：{second}')
    # print(f'横批：{center}')
    return center, first, second


# 解析生成的诗句
def parse_poem(data):
    """
    解析调用智能写诗生成的数据
    :param data: 调用智能写诗生成的有效数据
    :return: 诗的题目（title）和诗的内容（content）
    """
    title = data['poem'][0]['title']
    poem = data['poem'][0]['content'].replace('\t', '\n')
    # print(title)
    # print(poem)
    return title, poem


# 解析是否调用接口错误，如果有返回对应的提示，没有返回None
def parse_error(data):
    """
    解析是否调用接口错误
    :param data: 调用接口生成的数据
    :return: 如果出错，返回对应的错误信息，否则返回None
    """
    if 'error_code' in data:
        code = data['error_code']
        error = ERROR_DICT[str(code)]
        return error
    return None


# 带有错误处理的调用智能写诗接口（样例）
def test_get_poem():
    token_key = get_token_key()
    index = random.randint(0, 10)
    data = nlp_result('春节建行卡', token_key, index)
    error = parse_error(data)
    if error:
        print(f'错误：{error}')
    else:
        title, content = parse_poem(data)
        print(title)
        print(content)


if __name__ == '__main__':
    test_get_poem()
