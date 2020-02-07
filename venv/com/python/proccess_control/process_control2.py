# 实现列表推导式，一种创建列表的方法，应用场景：对一个序列的数据的每一个元素做操作，产生的结果
# 作为一个新的序列
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

t = [(r[0], r[1], r[2]) for r in m]
print(t)

Y = [1, 0, 1, 3, 3, 4, 5, 0]
colors = ['r' if item == 0 else 'b' for item in Y[:]]
print(colors)

# 99乘表法
for x in range(1, 10):
    # 存储所有乘法式子
    l = ['%s*%s=%-2s' % (y, x, x * y) for y in range(1, x + 1)]
    # 循环打印存储的乘法式子
    for i in range(len(l)):
        print(l[i], end=' ')
    print('')

print('join打印99乘表法:')
for x in range(1, 10):
    # 存储所有乘法式子
    l = ['%s*%s=%-2s' % (y, x, x * y) for y in range(1, x + 1)]
    # 循环打印存储的乘法式子
    print(' '.join(l[i] for i in range(len(l))))

print('2个join打印99乘表法:')
print('\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x * y) for y in range(1, x + 1)])
                 for x in range(1, 10)]))

# 迭代器原理,使用iter内置函数，返回一个迭代器对象
x = [1, 2, 3]
it = iter(x)
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# 无元素后抛出异常
# print(it.__next__())

print(next(it))
print(next(it))
print(next(it))
# print(next(it))

for i in range(len(x)):
    print('循环打印：', x[i])

for i in x:
    print('打印：', i)

for i, t in enumerate(x):
    print('索引：', i, '数据：', t)

ii = len(x)
index = 0
while index < ii:
    print('数据：', x[index])
    index += 1
