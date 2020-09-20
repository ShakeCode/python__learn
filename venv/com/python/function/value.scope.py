# 4种 变量的作用域
'''
L: 本地作用域，当前函数变量
E: 上一层结构def或者lambda本地作用域，函数嵌套情况
G:全局作用域，不被任何函数包括
B:内置作用域，是python的内部命名空间

优先级：L>E>G>B  俗称LEGB原则， 也就是一个变量会从4个域中寻找，匹配第一个停止，找不到则报错
'''

# 全局作用域
var = 1


def fun1():
    def fun2():
        # L作用域 自己函数内部作用域
        var = 3
        print(var)

    # E作用域 嵌套作用域
    var = 2
    # 内部调用fun2()
    fun2()


# 输出L域的var=3
fun1()

# <去掉fun2函数的var变量>

var = 1


def fun1():
    def fun2():
        print(var)

    var = 2
    fun2()


# 此时fun2函数没有变量了，在E作用域找到var=2
fun1()

# <去掉fun1函数的var变量>
var = 1


def fun1():
    def fun2():
        print(var)

    fun2()


# 在G 全局作用域找到var=1
fun1()

# 内置作用域查看
import builtins

print(dir(builtins))

# 《在L域或者E域对全局变量重新赋值》
a = 6


def func():
    # 获取全局变量a
    global a
    # 重新赋值全局变量
    a = 5


func()
# 输出5
print(a)

# 《nonlocal语句》
# 作用：在本地作用域以外按照优先级的顺序逐级去查询声明的变量，并引用该变量
a = 6


def func():
    # 获取全局变量a
    a = 7
    def nested():
        # 引用外层的a
        nonlocal a
        a += 1
    # 调用嵌套函数
    nested()
    print('本地：', a)


func()
print('全局：', a)

