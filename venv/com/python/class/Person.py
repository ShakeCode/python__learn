class Person:
    '''Person类'''

    # 类方法
    @classmethod
    def run(self):
        print("run ...")

    # 静态方法
    @staticmethod
    def eat():
        print("eat ...")

    # 类方法
    def sing(self):
        print("sing ...")

    # __new__
    # 通常用于控制生成一个新实例的过程。它是类级别的方法。先于init执行
    # 依照Python官方文档的说法，__new__方法主要是当你继承一些不可变的class时(比如int, str, tuple)， 提供给你一个自定义这些类的实例化过程的途径。还有就是实现自定义的metaclass。
    def __new__(cls, *args, **kwargs):
        print("call new ...")
        # 类对象属性，所有实例都会带有
        cls.address = "东莞"
        # 返回类实例
        return super(Person, cls).__new__(cls)

    # __init__
    # 通常用于初始化一个新实例，控制这个初始化的过程，比如添加一些属性， 做一些额外的操作，发生在类实例被创建完以后。它是实例级别的方法。
    def __init__(self, name, age):
        print("call init ...")
        self.age = age
        self.name = name

    def str(self):
        '''打印对象'''
        return '<Person:%s,%s>' % (self.name, self.age)


if __name__ == '__main__':
    a = Person('lijun', 20)

    a.eat()
    a.run()
    a.sing()

    Person.eat()

    print("注释说明：", a.__doc__)
    print("实例属性字典：", a.__dict__)
    print("对象属性字典：", Person.__dict__)
    print("目录：", a.__dir__())
    print("模块：", a.__module__)
    print("打印对象属性：", a.str())
    print(a.__repr__())
    print(a.__str__())
    print(a.__class__)
    print("是否a是1的实例：", a is 1)
    print(a.address, Person.address)
    # print(Person.name,Person.age) 报错，没有这2个属性


class PositiveInteger(int):
    '''继承一些不可变的class时(比如int, str, tuple)，自定义实例化'''
    def __new__(cls, value):
        return super(PositiveInteger, cls).__new__(cls, abs(value))


i = PositiveInteger(-3)
print("整数：", i)


# __new__实现单例
class Singleton(object):
    '''单例模式'''
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


obj1 = Singleton()
obj2 = Singleton()
obj1.name = "单例模式"
print(obj1.name, obj2.name)
print(obj1 is obj2)


class Boy(Person):
    '''男孩对象'''
    def eat(self):
        print("boy eat ...")

b=Boy("boy",26)
b.eat()
print(b.str())

print(b is Person)
