"""
10. 空气污染指数api的取值与对应的空气质量关系如下：
0～50为优， 51～99为良，100～199为轻度污染，200～299为中度污染，300以上为重污染。
请编写程序，从键盘输入api值，并输出api值所对应的空气质量。
"""
api = int(input("请输入空气污染指数api:"))
if 0 <= api < 51:
    print("空气质量为优")
elif 51 <= api < 100:
    print("空气质量为良")
elif 100 <= api < 200:
    print("空气质量为轻度污染")
elif 200 <= api < 300:
    print("空气质量为中度污染")
elif 300 <= api:
    print("空气质量为重污染")