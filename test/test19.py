"""19. 使用键盘输入10个数，求这10个数的平均数。"""
total = 0
for i in range(1, 11):
    num = float(input("请输入第" + str(i) + "个数字:"))
    total += num

print("这10个数的平均数:", total / 10)
