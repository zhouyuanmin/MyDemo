import base64

from captcha.image import ImageCaptcha
import string, random

import io

# string.ascii_letters   包含所有英文字母
# string.digits          包含0-9的所有数字
token = string.digits + string.ascii_uppercase  # 拼接字符串
# token = string.ascii_uppercase
print(token)

cap = random.sample(token, 4)  # 随机字符，固定数量
print(cap)
token_str = ''.join(cap)  # 拼接字符串
print(token_str)
img = ImageCaptcha()  # 实例化ImageCaptcha类
# 这是ImageCaptcha自带的初始化内容width=160, height=60, fonts=None, font_sizes=None，可以在实例化时自己设置
# generate_image可以接收一个分散的字符列表，可以不拼接在一起
# image=img.generate_image(cap)
image = img.generate_image(token_str)
# image.save('验证码.png')
print(type(image))
img_byte = io.BytesIO()
image.save(img_byte, format='PNG')
binary_str = img_byte.getvalue()
img_str = base64.b64encode(binary_str)
print(img_str)
# print(binary_str)
# data:image/png;base64,
