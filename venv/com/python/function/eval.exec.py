'''

内置函数:
eval（expression,globals=None,locals=None)
exec（expression,globals=None,locals=None)

expression --代码语句
globals 全局命名空间，可将当前系统的__buildins__复制到globals, 没有提供globals,则使用全局命名空间
locals, 局部命名空间，和globals重复时会覆盖globals. 没有提供时 以globals为准

联系：
都可以执行字符串形式的py代码，相当于py解释器

区别：
exec -无返回值
eval -有返回值, 第一个参数是字符串，且是可执行的字符串
'''

exec("print(\"I LOVE PY\")")
eval("print(\"I LOVE PY\")")

a = 1
exec("a=2")
print('重新赋值:', a)

# 无返回值，返回none
a = exec("2+3")
print(a)

# 有返回值
a = eval("2+4")
print(a)

# 报错，必须要有返回值
# b=eval("a=3")
# print(b)


dict = {}
dict['name'] = 3

print('keys:', dict.keys())

# 赋值
exec("a=4", dict)  # 作用域dict

print('keys:', dict.keys())
# 在dict作用域下执行exec语句，dict会加入2个新key, a和__buildin__(内建模块-存储系统内置key)
print('传入参数后：', dict)

print('内建模块values：', dict["__builtins__"])

# 作用域
dicX = {}
a = 2
exec('a=4', dicX)
print(a)
print('exec作用域：', dicX['a'], sep=' * ')

# eval作用域
dicY = {}
dicY['address'] = 20
dicY['id'] = 12
re = eval('id+address', dicY)
print('eval作用域：', re)

# 指定作用域
g = {'a': 1, 'b': 2, 'c': 3}
tt = {'d': 4, 'e': 5}
print('指定作用域', eval('a+b+e', g, tt))

# 可接受参数
ss = "hello"
XX = '"hello"'
print(eval('ss'))
print('repr转化：', eval(repr(ss)))
print(eval('XX'))

# repr （动态生成字符串）和str区别：
# 输出： 'hello'
print(repr(ss))
# 输出：hello
print(str(ss))


def obj2str(ss):
    '''对象转字符串'''
    a = str(ss)
    return a


def str2Obj(aa):
    '''字符串转对象'''
    b = eval(aa)
    return b


def str2Object(aa):
    '''字符串转对象'''
    b = eval(aa)
    print('字符串转化对象：', b)
    return b


a = ['age', "list", 'array']
print(obj2str.__doc__, obj2str(a), obj2str(a).__class__)

strx = "{'name':'小青','age':12}"
print(str2Obj.__doc__, str2Obj(strx), str2Obj(strx).__class__)
'''
输出：
象转字符串 ['age', 'list', 'array'] <class 'str'>
字符串转对象 {'age': 12, 'name': '小青'} <class 'dict'>
'''

# exec()批量调用函数
sx = ''
for i in range(1, 2):
    strx = "{'name':'野兽','type':'大猩猩'}"
    sx = 'str2Object(' + repr(strx) + ')'
    exec(sx)

print('a'.join(str(1)))

