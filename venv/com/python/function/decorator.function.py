
'''
装饰器;
1、作用：扩展原有功能，最大化利用现有代码
2、实现：在原有函数的外面再封装一封函数，使得新的函数返回原有函数之前实现一些其他功能
3、本质：是一个闭合函数，该闭合函数的自由变量是一个函数，是原有代码扩展功能的利器
'''

def checkParams(fn):
    '''装饰器函数，参数是被修饰的函数，相当于闭合函数，定义一个检查参数的函数'''
    def wrapper(strname):
        # 检查是不是字符串参数
        if isinstance(strname, str):
            # 是的话返回fn(strname)函数返回计算结果
            return fn(strname)
        print("参数类型不是字符串类型")
        return
    # 被修饰后的函数返回
    return wrapper

def wrapperfun(strname):
    def recoder(age):
        print('姓名:', strname, '年龄:', age)
    return recoder

# 对wrapperfun进行修饰，即自由变量设置为wrapperfun函数，得到带有参数校验的闭合函数
wrapperfun2=checkParams(wrapperfun)
# wrapperfun2为带有参数校验的闭合函数
fun=wrapperfun2('anna')
# 为age赋值
fun(37)
fun=wrapperfun2(38)

'''
@修饰符
作用：在定义函数时就可以为其指定修饰器函数，好处是使得修饰器与被修饰函数的关系更加明显。使得修饰的函数在第一时间得到修饰，降低编码的出错性
使用语法：
在@后面添加被修饰的函数，同时在其下一行添加被修饰函数的定义
'''

def checkParams(fn):
    '''装饰器函数，参数是被修饰的函数，相当于闭合函数，定义一个检查参数的函数'''
    def wrapper(strname):
        # 检查是不是字符串参数
        if isinstance(strname, str):
            # 是的话返回fn(strname)函数返回计算结果
            return fn(strname)
        print("参数类型不是字符串类型")
        return
    # 被修饰后的函数返回
    return wrapper

# 使用@修饰符实现对wrapperfun函数的修饰
@checkParams
def wrapperfun(strname):
    def recoder(age):
        print('姓名:', strname, '年龄:', age)
    return recoder

# wrapperfun为一个带有参数校验的闭合函数
fun=wrapperfun('kevin')
fun(37)
fun=wrapperfun(37)

# 多参数校验的通用参数修饰器
def checkParams(fn):
    '''装饰器函数，参数是被修饰的函数，相当于闭合函数，定义一个检查参数的函数'''
    # 元组和字典的解包参数作为形参
    def wrapper(*args,**kwargs):
        # 检查是不是字符串参数
        if isinstance(args[0], str):
            # 是的话返回fn(strname)函数返回计算结果
            return fn(*args,**kwargs)
        print("参数类型不是字符串类型")
        return
    # 被修饰后的函数返回
    return wrapper

#可接收参数的通用修饰器
def isAdmin(userid):
    def checkParams(fn):
        '''装饰器函数，参数是被修饰的函数，相当于闭合函数，定义一个检查参数的函数'''
        # 元组和字典的解包参数作为形参
        if userid !='admin':
            print('is not admin user')
        def wrapper(*args, **kwargs):
            # 检查是不是字符串参数
            if isinstance(args[0], str):
                # 是的话返回fn(strname)函数返回计算结果
                return fn(*args, **kwargs)
            print("参数类型不是字符串类型")
            return

        # 被修饰后的函数返回
        return wrapper
    return checkParams

@isAdmin(userid='admin1')
def wrapperfun(strname):
    def recoder(age):
        print('姓名:', strname, '年龄:', age)
    return recoder

fun=wrapperfun('hevin')
fun(37)
fun=wrapperfun(37)

def wrapperfun2(strname):
    def recoder(age):
        print('姓名:', strname, '年龄:', age)
    return recoder
# 执行isAdmin(userid='user')返回checkParams函数，并传入函数wrapperfun2函数
wrapperfun2=isAdmin(userid='user')(wrapperfun2)

# 打印wrapper，说明修饰器在修饰函数的同时，改变了函数本身的名称
print(wrapperfun2.__name__)


# 对修饰器返回函数的名称修复
# 在函数被修饰完后，对函数的名字属性再一次赋值，将函数的名称恢复过来
# 修改：
def isAdmin(userid):
    def checkParams(fn):
        '''装饰器函数，参数是被修饰的函数，相当于闭合函数，定义一个检查参数的函数'''
        # 元组和字典的解包参数作为形参
        if userid !='admin':
            print('is not admin user')
        def wrapper(*args, **kwargs):
            # 检查是不是字符串参数
            if isinstance(args[0], str):
                # 是的话返回fn(strname)函数返回计算结果
                return fn(*args, **kwargs)
            print("参数类型不是字符串类型")
            return

        # 被修饰后的函数返回
        # 将函数的名称恢复fn的名称
        wrapper.__name__=fn.__name__
        return wrapper
    return checkParams

# 内置修饰器函数 functools.wraps
# 作用：将修饰的函数名称还原并赋值给修饰后的返回函数
#可修改为：
import functools
def isAdmin(userid):
    def checkParams(fn):
        '''装饰器函数，参数是被修饰的函数，相当于闭合函数，定义一个检查参数的函数'''
        # 元组和字典的解包参数作为形参
        if userid !='admin':
            print('is not admin user')
        # 将函数的名称恢复fn的名称
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            # 检查是不是字符串参数
            if isinstance(args[0], str):
                # 是的话返回fn(strname)函数返回计算结果
                return fn(*args, **kwargs)
            print("参数类型不是字符串类型")
            return

        # 被修饰后的函数返回
        return wrapper
    return checkParams

# 组合修饰-- 多个修饰器的联合使用
# 载入顺序是从下往上的，执行顺序是从上往下的
def logging(userid):
    print('in logging')
    '''可接收参数的通用修饰器，用于打印日志'''
    def checkParams(fn):
        print('in checkParams')
        def wrapper(*args, **kwargs):
            print('in checkParams wrapper')
            print('用户名：',userid,end='！\n')
            return fn(*args, **kwargs)
        return wrapper
    return checkParams

# 组合修饰：
@logging(userid='admin')
@checkParams
def wrapperfun(strname):
    def recoder(age):
        print('姓名:', strname, '年龄:', age)
    return recoder

fun=wrapperfun('组合修饰')
fun(37)

# 解决同作用域下默认参数被覆盖的问题
# 案例:
def recoder(strname,age):
    print('姓名:', strname, '年龄:', age)

def makerRecoders():
    '''批量生产工厂函数'''
    acts=[]
    for i in ['hello','world']:
        # ！！！循环过程中该循环体作用域下的默认参数值会被循环值覆盖，导致所有在这个循环中产生的函数都会有相同的默认值
        # 生产的函数放进列表里面
        acts.append(lambda age:recoder(i,age))
    return acts

for a in (makerRecoders()):
    a(age=32)

# 得到：
# 姓名: world 年龄: 32
# 姓名: world 年龄: 32

# 解决：循环生产工厂函数的过程中，就不能将默认值放到作用域空间存储，必须将默认值当作参数传入原函数recoder
def recoder(strname,age):
    print('姓名:', strname, '年龄:', age)

def makerRecoders():
    '''批量生产工厂函数'''
    acts=[]
    for i in ['hello','world']:
        # ！！！循环过程中该循环体作用域下的默认参数值会被循环值覆盖，导致所有在这个循环中产生的函数都会有相同的默认值
        # 生产的函数放进列表里面
        acts.append(lambda age,i=i:recoder(i,age))
    # 返回批量函数
    return acts

for a in (makerRecoders()):
    a(age=32)

# 输出：
# 姓名: hello 年龄: 32
# 姓名: world 年龄: 32