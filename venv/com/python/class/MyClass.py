# 《声明使用类》
# 定义类
class MyClass:
    # 声明描述
    '''我是一个对象'''

    # 类成员变量
    name = "class a"

    # 定义类成员方法
    def say(self):
        '''定义类方法，需要声明默认第一个形参self,调用类方法时，不需要传入形参self'''
        return "i am saying ..."


# 实例化对象，赋值给my
my = MyClass()
# 调用类成员方法
print(my.say())
# 调用类成员变量
print(my.name)

# 《类的内置属性》
# 类名称
print(MyClass.__name__)
# 类文档字符串
print(MyClass.__doc__)
# 类定义所在的模块，之前运行当前类文件，该值为__main__
print(MyClass.__module__)
# 类的所有父类<class 'object'>列表，是一个tuple类型的对象
print(MyClass.__base__)
# 该类的所有属性（由类的数据属性组成）是一个dict类型的对象
print(MyClass.__dict__)


# 《类的动态属性定义》
# 1、使用: 实例化对象.属性名称，如果对象已存在则系统会读取器内容，否则自动为该对象加上这个属性
# 2、使用场景：读取文件，处理已知或者未知的结构体
# 声明一个空类
class Record:
    pass


anna = Record()
anna.age = 12  # 动态添加属性age
anna.name = '安娜'
print('年龄：', anna.age, '姓名：', anna.name)

# 《删除类的动态属性》
del anna.name


# 再次访问报错
# print(anna.name)

# 《限制类属性 __slots》

# __slots__ 是一个特殊变量，其值可以是元组的形式，元组的元素为该类所允许添加的属性名称，在一个类中，一旦为
# __slots__赋值。则该类的实例化对象就只能添加__slots__中所规定的属性
# 特殊的变量 __slots__ 在类的派生过程中仍然有效，即子类会继承父类的 __slots__ 内容
class RecordA:
    # 定义一个空类
    # 设置合法性属性name, age
    __slots__ = ('name', 'age')


kena = RecordA()
kena.name = 'Kena'
kena.age = 20
# 报错没有这个属性
# kena.age2 = 42





