class Base(object):
    def __init__(self):
        print("enter Base")
        print("leave Base")


class A(Base):
    def __init__(self):
        print("enter A")
        super(A, self).__init__()
        print("leave A")


class B(Base):
    def __init__(self):
        print("enter B")
        super(B, self).__init__()
        print("leave B")


class C(A, B):
    def __init__(self):
        print("enter C")
        super(C, self).__init__()


c = C()
print(C.mro())
# 解析顺序
# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <class 'object'>]
