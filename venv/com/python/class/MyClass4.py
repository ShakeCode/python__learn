

# 《类变量私有化类属性》
# 通过修改一个类变量可以使得这个类的所有实例的对象的属性都可以被统一修改。但是当实例变量和类变量同名时
# 系统会以实例变量优先，导致类变量实现，使得无法批量修改实例化后的类属性

# 解决方案：给类变量加上一定的权限，不允许实例化之后的对象直接访问类变量，通过类变量隐藏起来，避免读取类变量失效的问题

# 一、公有化与私有化
# 1、公有化：public 默认的权限。所有对象都可以访问
# 2、私有化：private 加上私有化的类变量 等属性不能被该类的实例化对象直接访问，但类的内部成员函数是可以访问
# 如果类实例化对象想取得该类的私有化属性，可以通过调用该类的函数完成

# python中规定：以2个下划线开头的成员对象为私有化成员

class Orange:
    '''a orange'''
    # 私有类变量
    __color="green"
    # 公开类变量
    address="东莞"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def toString(self):
        return self.name, self.age

    def getColor(self):
        return self.__color

or1=Orange("orange1",12)
or2=Orange("orange2",20)

or2.__color="yellow" #此处无法修改私有变量的值
print(or2.getColor()) #green
print(or1.getColor()) #green

# 以下是类变量赋值无法批量影响实例变量
or2.address="深圳"
Orange.address="广州"
print(or2.address) #深圳
print(or1.address) #广州
print(Orange.address)#广州

print(or2.getColor()) #green 类变量属性
print(or2.__color) #yellow 实例化变量属性
# print(Orange.__color)
# print(or1.__color) #报错 实例化变量属性 ，说明私有化变量对于实例化对象是不可见的
or1.__color="black" #再次赋值
print(or1.__color) #不会报错，输出 black
