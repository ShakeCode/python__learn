# 《实例化对象》

# 类的初始值方法

class Record:
    '''a class : record'''

    def __init__(self, name, age):
        '''类的初始化函数'''
        # 传入的参数赋值给成员变量
        self.name = name
        self.age = age

    def getRecord(self):
        '''返回类的属性'''
        # 打印格式：('record', '12')
        return self.name, self.age


re = Record("record", "12")
print(re.getRecord())


# 《隐藏调用类的初始化方法》
# 1、类的实例化时都会在内部调用初始化函数 __init__, 对于一个没有初始化函数的类，在实例化时 也会调用内部默认的__init__函数,内部已定义则调用已有自定义的
# 初始化函数的形参除了self，在实例化类时，都必须传入该参数，否则报错
class Apple:

    def __init__(self):
        print("i am apple!!")

    def getName(self):
        return "apple"


# 不传入形参也会打印i am apple!!
apple = Apple()

apple = Apple()
print(apple.getName())  # 实例化对象调用函数
print(Apple.getName(apple))  # 类对象调用函数 效果一样


# 《成员函数定义在类外面》
# 作用：提高函数给多个类使用，提高代码重用性
def fun(self):
    return 'have fun!'


class Orange:
    '''a class orange'''
    name = '橙子'
    haveFun = fun  # 类内部制度成员函数


orage = Orange()
print(orage.haveFun())


# 《类的成员互相访问》
class Pear:

    def __init__(self, name, age):
        '''类的初始化函数'''
        # 传入的参数赋值给成员变量
        self.name = name
        self.age = age

    def getAge(self):
        return self.age

    def getName(self):
        return self.name

    def getPear(self):
        # return self.name,self.age
        # 调用其他成员函数
        return self.getName(), self.getAge()


pear = Pear('pearA', 100)
print(pear.getPear())

# 获取元素类型
print(Pear.__class__)
print(type(Pear))
print(type('hello'))
print(type(('hello')))
print(type([1,2,3]))