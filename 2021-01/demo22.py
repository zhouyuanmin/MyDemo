import itsdangerous
import time
from itsdangerous import SignatureExpired

salt = 'salt'  # 加盐
t = itsdangerous.TimedJSONWebSignatureSerializer(salt, expires_in=30)  # 过期时间600秒

info = {'username': 'yang', 'user_id': 1}

# =========加密token============
res = t.dumps(info)
token = res.decode()  # 指定编码格式
print(token)

time.sleep(2)
# =========解密token============

res = t.loads(token)
print(res)

# 当超时或值有误则会报错
time.sleep(1)
t = itsdangerous.TimedJSONWebSignatureSerializer(salt)  # 过期时间600秒
try:
    res = t.loads(token)
    print(res)
except SignatureExpired as e:
    print(e.message)
    print(e.date_signed)
    pass

"1.2.3"
