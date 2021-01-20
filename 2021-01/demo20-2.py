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