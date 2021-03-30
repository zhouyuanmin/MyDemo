import requests

url = "https://api.dingdangcode.com/ddc-port/play/userPraise?worksId=48359"

for i in range(2000):
    response = requests.get(url)
    print(i, "--> ", response.text)
