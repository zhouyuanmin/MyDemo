import requests
from bs4 import BeautifulSoup

base_url = 'https://www.runoob.com/cprogramming/c-exercise-example{}.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
}
for i in range(50, 101):
    url = base_url.format(i)
    res = requests.get(url, headers=headers)
    html = res.text
    print(html)
    soup = BeautifulSoup(html, "html.parser")

    code_html = soup.select("#content > pre:nth-child(9)")
    print(code_html)
    break
