"""18. 输出以下由“*”组成的图形"""
# 图一
for i in range(0, 5):
    print('*' * (i + 1))
# 图二
for i in range(0, 5):
    print(' ' * (5 - i - 1) + '*' * (i + 1))
# 图三
for i in range(0, 5):
    print(' ' * (5 - i - 1) + '*' * (i * 2 + 1))
