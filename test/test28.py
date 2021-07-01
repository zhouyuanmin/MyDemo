"""
28. 定义一个名为primeNumbers(number)的函数，参数为一个正整数。
通过使用这个函数，能够输出小于number的所有素数，输出的时候，每行10个素数。
在同一源文件中，使用键盘输入一个正整数，验证该函数的输出结果。
"""


def primeNumbers(number):
    num = []
    i = 2
    for i in range(2, 100):
        j = 2
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            num.append(i)
    for i, v in enumerate(num):
        print(v, end=" ")
        if i != 0 and i % 10 == 0:
            print()


number = int(input("请输入一个数字:"))
primeNumbers(number)
