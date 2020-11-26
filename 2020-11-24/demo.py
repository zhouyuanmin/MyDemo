with open('file.txt', 'r')as f:
    t = f.readlines()
    for i in range(len(t) - 1):
        t[i] = t[i][:-1]

    t = set(t)
    t = list(t)
    # print(t)

with open('new_file.txt', 'w')as f1:
    for i in t:
        f1.write(i)
        f1.write('\n')