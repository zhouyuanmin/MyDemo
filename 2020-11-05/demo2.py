import requests

with open('d4.txt', 'r') as f:
    d4s = [d.strip() for d in f.readlines()]

url = 'http://panda.www.net.cn/cgi-bin/check.cgi?area_domain={}' # Hold me
with open('d4nr.txt', 'a') as f:
    for d in d4s:
        # 210
        res = requests.get(url.format(d))
        if '210' in res.text:
            f.write(f'{d}\n')
            f.flush()
        elif '200' not in res.text:
            with open('error.txt', 'a') as f1:
                f1.write(f'NO {d}')
        else:
            print(f'NO {d}')




