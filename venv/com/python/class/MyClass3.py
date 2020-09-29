'''
《类变量与实例变量的区别》
1、类变量：指的是类的属性和方法，类似一种静态数据。类变量在定义类时定义，类的所有实例都共享类变量
2、实例变量：指的是一种动态数据，只有在实例化时 系统才会为该实例指定它特有的数据
'''


class Person:
    '''a person class'''
    # 类变量,类对象和实例都可访问的属性
    JOB = "scientist"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def toString(self):
        return self.name, self.age


per = Person("小米", 12)
print(per.toString())
print(per.JOB)
print(Person.JOB)

# 通过修改一个类变量可以使得这个类的所有实例的对象的属性都可以被统一修改。但是当实例变量和类变量同名时
# 系统会以实例变量优先，导致类变量实现，使得无法批量修改实例化后的类属性
# 例如：
perA = Person("小米", 12)
perA.JOB = "winer"
Person.JOB = "teacher"
print(per.JOB)  # teacher
print(perA.JOB)  # winer


# 《销毁类实例化对象》
# 1、实例化对象：调用内置方法, __init__
# 2、销毁对象：调用方法, __del__

class Pear:
    '''a pear'''

    def __init__(self, name, age):
        '''初始化对象'''
        self.name = name
        self.age = age

    def __del__(self):
        '''销毁对象'''
        print(self.__class__.__name__, "del finish!")

pear = Pear("pear",12)
del pear



