"""
25. 定义一个名为isLeapYear(year)的函数，参数为一个年份，如果该年份是闰年，则返回值为True，
否则，返回值为False。在同一源文件中，使用键盘输入年份，验证该函数是否能够正确返回该年份是否为闰年。
"""


def isLeapYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("{0}是闰年".format(year))  # 整百年能被400整除的是闰年
            else:
                print("{0}不是闰年".format(year))
        else:
            print("{0}是闰年".format(year))  # 非整百年能被4整除的为闰年
    else:
        print("{0}不是闰年".format(year))


year = int(input("输入一个年份: "))
isLeapYear(year)
