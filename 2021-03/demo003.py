import re

# 创建正则表达式对象 使用了前瞻和回顾来保证手机号前后不应该出现数字
pattern = re.compile(r'(?<=\D)1[3456789]\d{9}(?=\D)')
sentence = '''重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
不是15600998765，也是110或119，叮小马的手机号才是15600998765。'''
# *************在下面补充代码********************#
mylist = re.findall(pattern, sentence)
for temp in mylist:
    print(temp)
