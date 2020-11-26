import math

s = []
string = ""
with open('reports.txt', 'r') as f:
    s = f.readlines()

sum1, sum2, sum3 = 0, 0, 0

for i in range(1, len(s)):
    li = s[i].replace('\n', '').split("\t")
    sum1 += int(li[1])
    sum2 += int(li[2])
    sum3 += int(li[3])

l = len(s) - 1

avg1 = math.ceil(sum1 / l)
avg2 = math.ceil(sum2 / l)
avg3 = math.ceil(sum3 / l)

ss = '\n平均分\t' + str(avg1) + '\t' + str(avg2) + '\t' + str(avg3)
re = string + ss
# print(re)
with open('new_reports.txt', 'w') as ff:
    ff.write(re)
