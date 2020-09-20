# 生成器函数与迭代器函数区别：
# 1、迭代器是所有内容在内存，通过next函数依次遍历，比较浪费内存。时间优先
# 2、生成器函数不会把内容全部放在内存，每次调用next函数，返回的都是本次计算的元素，用完立马销毁，比较节约内存。空间优先

# 生成器函数-创建生成器对象的函数，使用yield语句返回，返回值是一个生成器对象

def reverse(data):
    '''反转字符串'''
    for id in range(len(data) - 1, -1, -1):
        yield data[id]


for c in reverse('python'):
    print(c, end=' ')

print("\n")

# for循环列表推导式 [ ]
list = [x * x for x in range(4)]
print('for循环列表推导式,生成0-3的平方数:', list)
for i in list:
    print(i)

# 生成器表达式 ( )
myGen = (x * x for x in range(3))
print('生成器表达式-生成0-2的平方数:', myGen)
for x in myGen:
    print(x)

