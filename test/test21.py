"""21. 输出以下由数字组成的图形"""
for i in range(6):
    for j in range(i + 1):
        print(j + 1, end='')
    print()
#
for i in range(6, 0, -1):
    for j in range(6 - i):
        print(' ', end='')
    for j in range(i, 0, -1):
        print(j, end='')
    print()
#
for i in range(6):
    for j in range(5 - i):
        print(' ', end='')
    for j in range(i + 1):
        print(j + 1, end='')
    print()
