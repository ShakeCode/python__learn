# 函数：内置，自定义,函数的本质是对象，都会继承可调用方法call, 使用callable 检查函数是否可以被调用
def printInput(name, age):
    '''该函数返回用户的姓名、年龄'''
    return name, age


# 打印函数说明
print(printInput.__doc__)
# 修改函数说明
printInput.__doc__ = '返回用户的name,age'
print(printInput.__doc__)

# 字典接收函数属性
print('函数属性:', printInput.__dict__)
printInput.attr = 'pseron'
print('函数属性:', printInput.__dict__)
print('函数属性:', printInput.attr)

print('函数是否能被调用: ', callable(printInput))

# 2个变量分别接收
name, age = printInput('lijun', 12);
print(name, age)

# 直接打印为元组
print(printInput('lijun', 12))
print(printInput('lijun', 12)[0])
print(printInput('lijun', 12)[1])

# _表示不接收返回值
personname, _ = printInput('jack', 29);
print('名字:', personname)


# 形参默认赋值
def hello(age, name='jackson'):
    print('输出默认参数:', name, age)


# 按照形参顺序传参
hello(190, '你好')

# 按照指定形参传承，确定参数赋值,默认的参数必须在没有默认值参数的后面
# hello(name='你好!!!!!',12)  报错
hello(144, name='你好!!!!!')


# 多个形参使用*表示
# 有多少个形参，就传进去多少个实参，但有时候会不确定有多少个参数，则此时第三种方式就比较有用，它以一个*加上形参名的方式来表示这个函数 的实参个数不定，可能为0个也可能为n个。注意一点是，不管有多少个，在函数内部都被存放在以形参名为标识符的tuple中。元组参数不能被修改
def hi(bb, *a):
    # 多个a参数赋值,打印元组
    print("元组接收参数:", bb, a, a[0], a[1], sep=',')
    return bb, a


# 接收返回值：
_, xxxx = hi('hello', 'world', 'hahha')

print('打印参数元组:', xxxx)

# 使用list列表传参, 使用*引用list
li = ['time', 'address']
hi('list传参数', *li)


# 形参名前加俩个*表示，参数在函数内部将被存放在以形式名为标识符的dictionary中，这时调用函数的方法则需要采用arg1=value1,arg2=value2这样的形式,传参即指定了参数的名称与赋值。
def dayin(**a):
    print('字典参数入参:', a, a['math'], a.get('chiness'))


dayin(math='math', chiness='chiness')
dayin(math=1)

# 引用字典数据,使用**
dic = {'math': 'java', 'chiness': 'go'}
dayin(**dic)


# 星号方式定义参数，代表调用时，在星号后面的参数都必须要指定参数名称
def recoder(name, *, age):
    print('姓名:', name, '年纪:', age)


# 实际调用:
recoder('python', age=12)


# 以下传参数会报错，无指定参数
# recoder('python', 12)

# 混合使用
def recoder(*person1, **person2):
    # 元组参数传入
    if len(person1) != 0:
        print('姓名：', person1[0], '年纪:', person1[1])
    # 字典参数传入
    if len(person2) != 0:
        print('姓名：', person2['name'], '年纪:', person2['age'])

# 不指定k-v，由元组接收
recoder('xiaoming',888)
# 指定k-v,由字典类型接收
recoder(name='小红',age=9999)

# 指定形参，不指定形参传入,元组和字典都接收
# 指定参数接收的必须在后面
recoder('xiaoming',888,name='小红',age=9999)



# 普通函数:def
# 匿名函数,lambda 表达式
# 偏函数: partial定义
# 可迭代函数，递归函数
