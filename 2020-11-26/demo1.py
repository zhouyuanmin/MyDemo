class Base(object):
    def __init__(self):
        print("enter Base")
        print("leave Base")

    def __del__(self):
        print('调用 Base del')


class A(Base):
    def __init__(self):
        print("enter A")
        super(A, self).__init__()
        print("leave A")

    def __del__(self):
        print('调用 A del')


class B(Base):
    def __init__(self):
        print("enter B")
        super(B, self).__init__()
        print("leave B")

    def __del__(self):
        print('调用 B del')


class C(A, B):
    def __init__(self):
        print("enter C")
        super(C, self).__init__()

    def __del__(self):
        print('调用 C del')
        super(C, self).__del__()


c = C()
print('ok')
# del c
c.__del__()
print('ok2')
# 解析顺序
# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <class 'object'>]
