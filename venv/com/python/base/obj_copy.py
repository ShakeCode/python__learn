# 浅拷贝--创建一个新对象，内容还是原对象元素的引用
# 产生场景：切片，工厂，对象copy，copy模块copy函数

# 等号赋值，对象不会重新创建，只有重新创建对象并赋值，才会发生浅拷贝

tt = ['hello', [1, 2]]
aa = tt
print(id(tt), id(aa))
aa = list(tt)
print(id(tt), id(aa))

for x, y in zip(aa, tt):
    print('x-内存ID', id(x), 'y-内存地址:', id(y))

# 深拷贝，创建一个对象并赋值，原对象的所有元素都会在新对象重新创建一次

import copy

tt = ['hello', [1, 2, 3]]
aa = copy.deepcopy(tt)
print(id(tt), id(aa))
for x, y in zip(aa, tt):
    print('x-内存ID', id(x), 'y-内存地址:', id(y))
