# import time
# import random
# seed = 1
# list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# temp =  random.randint(0, 25)
# count = 0

# for i in range(0,100):
#     if i % 9 == 0 and i <= 81:
#         print(str(i) + ':' + list1[temp], end="\t")
#         count += 1
#     else:
#         print(str(i) + ':' + list1[random.randint(0, 25)], end="\t")
#         count += 1
#     if count % 10 == 0:
#         print()

# print()
# print('请在脑海中想一个数字，将它减去十位上的数字，再减去个位上的数字，得到最终数字，并记住最终数字对应的字母')
# s = input('记住字母后按回车开始读心！')
# for i in range(5, 0, -1):
#     print(i)
#     time.sleep(1)

# print("你心中的字母是：" + list1[temp])


# 任务一：
import random

list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']
temp = random.randint(0, 25)

print(list1)
print(temp)

# 任务二：
import random

list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']
temp = random.randint(0, 25)

count = 0
for i in range(0, 100):
    if i % 9 == 0 and i <= 81:
        print(str(i) + ':' + list1[temp], end="\t")
        count += 1
    else:
        print(str(i) + ':' + list1[random.randint(0, 25)], end="\t")
        count += 1
    if count % 10 == 0:
        print()

# 任务三：
import time
import random

seed = 1
list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']
temp = random.randint(0, 25)
count = 0

for i in range(0, 100):
    if i % 9 == 0 and i <= 81:
        print(str(i) + ':' + list1[temp], end="\t")
        count += 1
    else:
        print(str(i) + ':' + list1[random.randint(0, 25)], end="\t")
        count += 1
    if count % 10 == 0:
        print()

print()
print('请在脑海中想一个数字，将它减去十位上的数字，再减去个位上的数字，得到最终数字，并记住最终数字对应的字母')
s = input('记住字母后按回车开始读心！')

print("你心中的字母是：" + list1[temp])

# 最终代码
import time
import random

seed = 1
list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']
temp = random.randint(0, 25)
count = 0

for i in range(0, 100):
    if i % 9 == 0 and i <= 81:
        print(str(i) + ':' + list1[temp], end="\t")
        count += 1
    else:
        print(str(i) + ':' + list1[random.randint(0, 25)], end="\t")
        count += 1
    if count % 10 == 0:
        print()

print()
print('请在脑海中想一个数字，将它减去十位上的数字，再减去个位上的数字，得到最终数字，并记住最终数字对应的字母')
s = input('记住字母后按回车开始读心！')
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

print("你心中的字母是：" + list1[temp])