"""
27. 定义一个名为isPrime(number)的函数，参数为一个正整数。
通过使用这个函数，能够判断一个正整数，是否为素数，是素数则返回True，不是素数则返回False。
在同一源程序中，使用键盘输入一个正整数，验证该函数是否能够正确判断输入数为素数。
"""
import math


def isPrime(n):
    if n <= 1:
        return "不是素数"
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return "是素数"


num = int(input("请输入一个数字:"))
print(isPrime(num))
