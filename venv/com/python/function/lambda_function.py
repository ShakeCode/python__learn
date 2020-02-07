# 匿名函数，单行代码函数，简单功能封装，使用一次不再需要，名字也省略
# 以lambda 开头, lambda 参数1，参数2，... ： 表达式
# 不能存在return 关键字

r = lambda x, y: x + y
print(r(2, 3))


# 可在任何地方使用，相当于可传入参数的单一表达式
def sumfun(n):
    # 返回匿名函数
    return lambda x: x + n


# 得到匿名函数，函数体为x+15
f = sumfun(15)
print(f(5))  # 返回20

# 配合可迭代函数使用，可迭代函数式一种有循环迭代功能的内置函数，包括reduce，map,filter等
# 可迭代函数需要制定lambda  为处理函数

# def reduce(function, sequence, initial=None)
# map(function, *iterables) --> map object
# 1-100 求和
from functools import *

print(reduce(lambda x, y: x + y, range(1, 101)))

# map 迭代运行，求平方，返回序列，使用list，tuple 接收
print('单序列和map', list(map(lambda x: x ** 2, [1, 2, 3, 4])))

# 多序列,参数个数和序列个数对应，取最短序列运算
print('多序列和map：', list(map(lambda x, y: x + y, [1, 2, 3, 4], [1, 2, 3, 4, 5])))

# filter函数，对序列进行过滤
# filter(function,iterable)
# 过滤出序列中整除=2的数据
t = filter(lambda x: x % 2 == 0, [1, 2, 3, 4])
# print(list(t))

# 可迭代函数的返回值
# 每个可迭代函数的返回值都是一个生成器对象
# print(t.__next__())
# print(t.__next__())
# print(t.__next__())

# 等价于：
for a in t:
    print(a)


# 主要区别
# 1、生成器对象只能迭代一次，再次迭代输出为空
# 2、可迭代对象可迭代多次