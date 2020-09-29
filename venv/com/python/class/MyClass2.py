#  《装饰器：类方法，静态方法》

'''
使用@classmethod 修饰类方法，说明方法是一个类方法
使用@staticmethod 修饰静态方法，说明方法是一个静态方法

类方法与默认成员方法区别：类方法属于类，默认成员方法属于类实例对象：
1、类方法第一个参数必须是cls(用来指代该类)
2、默认成员方法第一个参数必须是self（用来指代该类的实例对象）
3、调用类方法使用 类名.类方法名
3、调用默认成员方法使用 该类的实例对象.类方法名

4、静态方法调用: 使用 该类的实例对象.静态方法名 或者 类名.静态方法名 (第一个方法参数不需要传入cls 或者 self)，独立于整个类

@@@@ 类成员方法的3个类型方法在派生的时候也可以生效，子类可以调用父类的成员方法！！！
'''

class Apple:

    def getColor(self):
        return "red"

    @classmethod
    def getName(cls):
        return "apple"

    # 不需要传入cls 或者 self
    @staticmethod
    def getAddress():
        return "china"

apple=Apple()
print(apple.getName())
print(apple.getColor())

print(Apple.getName())
# print(Apple.getColor()) #报错，不是类方法

print(Apple.getAddress())
print(apple.getAddress())



