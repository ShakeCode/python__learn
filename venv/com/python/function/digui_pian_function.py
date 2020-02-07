# 偏函数，对原始函数二次封装，向原始函数添加默认参数，有点类似对象中的父类与子类的关系
# 关键字：partial(function,*arg,**keywords)
# function --- 需要封装的函数
# arg -- 一个元组或者列表的解包参数，代表传入原函数的默认值（可不指定参数名）
# keyword -- 字典解包参数，代表传入原函数的默认值（指定参数名）

# 本质：将函数式编程，默认参数和冗余参数结合在一起，通过偏函数传入的参数调用关系，与正常的参数调用关系是一致的

from functools import *


def recoder(strname, age):
    print('姓名：', strname, '年龄:', age)


# 定义偏函数
fun = partial(recoder, strname='Garry')

fun(age=32)

# 递归函数，自己调用自己，否则出现栈溢出，因所有函数的调用都是压栈的过程，每个函数分配了一定的栈空间
# 内置函数：eval(), exec(),执行一个字符串的Python代码，相当于python.解释器
# 区别：
# 1、exec() 不返回结果, 适合放置在没有运行结果的语句，
# 2、eval() 要返回结果，适合在有返回得语句中

# 都包含3个参数
'''
1、expression -- 需要执行的语句，字符串
2、globals -- 全局命名空间, 配套 内建模块：__builtins__, 无提供使用全局python 命名空间
3、locals -- 局部命名空间，和gloabls冲突时，以locals为准，没有提供，以globals为准
'''
exec('print(\'i love python\')')
a = 1
exec('a=2')
print(a)

a = exec('2+3')
print(a)

a = eval('2+3')
print(a)

# 放置一个无返回值得语句，报错
# a=eval('a=2')


dic = {}
# 添加元素b
dic['b'] = 3
print(dic.keys())  # 生成：dict_keys(['b'])
# 执行exec与后面的作用于dic
exec('a=4', dic)
print(dic.keys())  # 生成：dict_keys(['a', 'b', '__builtins__'])

# 取出__builtins__ 的value
# print(dic['__builtins__'])

# 作用域
dic = {}
a = 2
exec('a=4', dic)
print(a)
print(dic['a'])

# 表明 赋值a变量是新生成一个a 在字典里面

dic = {}
dic['a'] = 3
dic['b'] = 4
result = eval('a+b', dic)
# 取dic的a,b,找不到则报错
print(result)

# locals参数使用
a, b, c = 10, 20, 30
g = {'a': 6, 'b': 8}
t = {'b': 100, 'c': 10}
print(eval('a+b+c', g, t))

s = 'hello'
print(eval('s'))
print(eval(repr(s)))

print('repr:', repr(s))
print(str(s))
# 不可直接打印 eval(s),因为s 不是可执行语句

# 可改造为:
ss = '"hello"'
print(eval(ss))
