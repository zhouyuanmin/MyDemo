import requests

headers = {
    'User-Agent': 'User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0'
}

list_page = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
detail_page = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"
for i in range(1, 3):
    form_data = {
        'on': 'true',
        'page': i,
        'pageSize': 15,
        'productName': '',
        'conditionType': 1,
        'applyname': '',
        'applysn': ''
    }
    # 请求列表页
    response = requests.post(url=list_page, headers=headers, data=form_data)
    json_data = response.json()
    json_data_list = json_data.get('list')
    for item in json_data_list:
        print('公司数据-列表页数据:', item)
        business_id = item.get('ID')
        form_data = {
            'id': business_id
        }
        # 请求详情页
        response = requests.post(url=detail_page, headers=headers, data=form_data)
        print('公司数据-详情页数据:', response.json())
