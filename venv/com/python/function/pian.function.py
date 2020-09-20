
#偏函數 - ,默认参数+动态参数+函数式编程
# 引入模块：functools
#  partial(func,*args,**keywords)
# 作用：为原函数指定默认的参数，调用该偏函数，相当于调用原函数，同时将默认的参数传入
# func-原始函数
# args-一个元组或者列表的解包参数，代表传入参数的默认值，可以不指定参数名
# keyword-字典的解包参数，代表传入原函数的默认值（指定参数名）

from functools import partial
def recorder(name,age):
    print('姓名：',name,'年纪',age)


#定义偏函数
myfun=partial(recorder,name='李俊')

myfun(age=32)

myfun(age=12,name="hello")