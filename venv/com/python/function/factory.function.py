# 设计思想-工厂函数
def recorder(strname, age):
    print('姓名:', strname, '年龄:', age)


def garyFun(age):
    # 实现偏函数的功能
    strname = 'Gary'
    return recorder(strname, age)


garyFun(age=32)


# 闭合函数--闭包函数，closure
# 实现：
# 将名字作为自由变量，将函数作为嵌套函数，通过函数封装
# 闭合函数，strname为变量
def wrapperfun(strname):
    # 定义嵌套函数
    def recoder(age):
        print('姓名:', strname, '年龄:', age)

    # 返回嵌套recoder函数
    return recoder


# fun函数相当于一个strname初始化后的recoder函数，为recoder的闭合函数。自由变量strname处于闭合函数之内
fun = wrapperfun('Ana')
fun(37)
fun2 = wrapperfun('John')
fun2(32)

# 闭合函数比普通函数多一个属性: __closure__,该属性会记录自由变量的参数的对象地址。当闭合函数被调用时，系统会根据该地址找到自由变量
# 完成整体函数的调用
# 输出:(<cell at 0x0112C7B0: str object at 0x0112C4E0>,)，为一个对象字符串。对象时fun中的自由变量strname的初始值
# __closure__属性的类型是一个元组，表明闭合函数可以支持多个自由变量的形式
print(fun.__closure__)

