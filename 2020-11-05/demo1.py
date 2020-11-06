chars = [chr(i) for i in range(97, 97 + 26)]
print(chars)

# 4个
d4s = []
for i1 in chars:
    for i2 in chars:
        for i3 in chars:
            for i4 in chars:
                d4s.append(f'{i1}{i2}{i3}{i4}.cn')
with open('d4.txt', 'w') as f:
    f.write('\n'.join(d4s))

# 5个
d5s = []
for i1 in chars:
    for i2 in chars:
        for i3 in chars:
            for i4 in chars:
                for i5 in chars:
                    d5s.append(f'{i1}{i2}{i3}{i4}{i5}.cn')
with open('d5.txt', 'w') as f:
    f.write('\n'.join(d5s))
