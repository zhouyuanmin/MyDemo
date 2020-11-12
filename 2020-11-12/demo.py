import requests

url = 'http://127.0.0.1:8101/3d/v1/baseRun/createModule'
data = {
    "code": "aW1wb3J0IGNhZHF1ZXJ5IGFzIGNxCm1vZGVsID0gY3EuV29ya3BsYW5lKCJYWSIpCm1vZGVsID0gbW9kZWwuc3BoZXJlKDIwKQpzaG93X21vZGVsKG1vZGVsLCBjcSk="
}
res = requests.post(url=url, data=data)

print(res.status_code)
print(res.json())
print(res.text)
