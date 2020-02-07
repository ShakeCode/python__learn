# 函数中调用检查参数，使用函数：isinstance(obj,class_or_tuple)
# obj-待检查的对象
# class_or_tuple - 待检查的具体类型，类或者元组

def recoder(name, age):
    # 检查年龄参数的合法类型是：int , str
    if not isinstance(age, (int, str)):
        # 使用raise函数报错
        raise TypeError('bad operand type')
    print('name is:', name, 'age is', age)


# recoder('jack',age=12.23)

# 函数调用中的参数传递以及影响
# 1、不可变对象 -- 传值，不可改变实参的值
# 2、可变对象 -- 传引用，可以改变实参的值

def fun(arg):
    arg = 5  # 函数体通过形参赋值的方式改变形参


x = 1
fun(x)
print(x)


# 可变对象,形参传入一个list, 或是一个字典等允许被修改的对象时，就把该对象的值传递给形参，对象值也会因此发生改变
def fun1(arg):
    arg.append(3)


x = [1, 2]
fun1(x)
print(x)

# 解包参数与列表传值存在区别，元组不能解包不可修改

# 1、列表传值
mylist = ['gary', '34']


def recoder(person):
    person[0] = 'sss'
    print('姓名:', person[0], '年纪:', person[1])


recoder(mylist)
print(mylist)

# 2、解包传值,报错，提示元组不能被修改
'''
mylist=['gary','34']
def recoder(*person):
    person[0]='sss'
    print('姓名:',person[0],'年纪:',person[1])

recoder(mylist)
print(mylist)
'''


