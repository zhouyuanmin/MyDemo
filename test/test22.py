"""
22. 使用键盘输入一个年份，并在控制台输出这一年，每个月1日是星期几。
"""
import datetime

y = int(input('请输入年份'))


def get_weekday(y, m, d):
    lis = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    w = datetime.date(int(y), int(m), int(d))
    return lis[w.weekday()]


for m in range(1, 13):
    print(str(y) + "年" + str(m) + "月1日是" + get_weekday(y, m, 1))
