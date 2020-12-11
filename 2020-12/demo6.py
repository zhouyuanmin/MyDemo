class Person():  # 创建一个类
    def __init__(self, name):  # 定义初始化信息。
        self.name = name

    __slots__ = ('name', 'age')


li = Person('李')  # 实例化Person('李'),给变量li
li.age = 20  # 再程序没有停止下，将实例属性age传入。动态语言的特点。
Person.age = None  # 这里使用类名来创建一个属性age给类，默认值是None。Python支持的动态属性添加。
li.ss = 222