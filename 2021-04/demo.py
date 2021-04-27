import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45'
}

# home_page_urls = ['http://www.netbian.com/1920x1080/'] \
#                  + [f'http://www.netbian.com/1920x1080/index_{i}.htm' for i in range(2, 907)]
#
# for url in home_page_urls:
#     print(url)
#     response = requests.get(url=url, headers=headers)
#     html = response.text
#     pattern = '<li><a href="(/desk/.*?)" title'
#     paths = re.findall(pattern=pattern, string=html)
#     sub_urls = [f"http://www.netbian.com{i}" for i in paths]
#     # print(sub_urls)
#     for sub_url in sub_urls:
#         response = requests.get(url=sub_url, headers=headers)
#         html = response.text
#         pattern = r'<div class="pic">.*?<img src="(.*?)" alt'
#         pic_urls = re.findall(pattern=pattern, string=html)
#         # print(pic_urls)
#         with open('pic_urls.txt', 'a') as f:
#             pic_url = pic_urls[0]
#             f.write(f"{pic_url}\n")

with open('pic_urls.txt', 'r') as f:
    pic_urls = [url.strip() for url in f.readlines()]
    # print(pic_urls)
    for index, pic_url in enumerate(pic_urls, 1):
        print(index, pic_url)
        response = requests.get(url=pic_url, headers=headers)
        with open(f'pic/{index}.jpg', 'wb+') as pf:
            pf.write(response.content)
