"""
9. 解一元二次方程组，ax** 2 + bx  + c = 0，时，有三种可能情况，分别为：
1、 有两个不等实根
2、 有两个相等实根
3、 无实根。
请使用键盘输入a, b, c的值，并输出一元二次方程的解。
"""
import math


def root_of_square(a, b, c):
    discr = pow(b, 2) - 4 * a * c
    if a != 0 and discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return x1, x2
    elif a != 0 and discr == 0:
        return -b / (2 * a)
    elif a == 0 and b != 0:
        return -c / b
    else:
        return "no solution"


if __name__ == "__main__":
    a = input("请输入a:")
    b = input("请输入b:")
    c = input("请输入c:")
    print(root_of_square(float(a), float(b), float(c)))
