"""7. 使用round(x, y)函数，可以将浮点数x保留y位小数。
使用键盘，输入两个非零数，求这两个数的商，结果保留两位小数。
输出的时候，请注意使用“➗”（十进制Unicode编码：10135）作为连接符表示除号。"""
num1 = float(input("请输入第一个数:"))
num2 = float(input("请输入第二个数:"))
num3 = num1 / num2
num3 = round(num3, 2)
print(str(num1) + chr(10135) + str(num2) + "=" + str(num3))
