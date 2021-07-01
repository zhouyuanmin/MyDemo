"""6. 使用random.randint(a, b)方法，随机生成三个100以内的自然数，求三个数的和。"""
import random

num1 = random.randint(0, 100)
num2 = random.randint(0, 100)
num3 = random.randint(0, 100)
print("三个数的和:", num1 + num2 + num3)
