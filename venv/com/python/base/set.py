# 无序不可重复集合
myset = {1, 3, 4, 4, 1.3, 'hello'}
print(myset)

li = [1, 2, 3, 3]
print('列表转为set集合:', set(li))

tu = (1, 3, 4, 4, True, False)
print('数组转换为set:', set(tu))

# 创建空set,不可使用{ },系统默认创建为字典类型
set1 = set()
print(set1)
set1.add(123)
print(set1)

ss = '123'
x = '234'
set1 = set(ss)
set2 = set(x)
print('字符串转set:', set1)
print('字符串转set:', set2)
print('he' in set(ss))

print('差集:', set1 - set2)
print('交集:', set1 & set2)
print('并集:', set1 | set2)
print('对称差集（除去2个集合的唯一元素组成的新集合）:', set1 ^ set2)

set3 = set()
set3.add('str')
set3.add((1, 2, 3))
set3.add(3.14)
# 随机删除一个元素
set3.pop()
print(set3)

# 删除指定元素，不存在即报错
# set3.remove(3)

# 存在即删除
set3.discard(3.143)
print(set3)

# 添加列表的元素进入Set
set3.update(['hello', 999])
print(set3, '长度:', len(set3))

print(123 not in set3)

set4 = {123, 567, 999}

print('是否包含元素:', set4.__contains__(123))
# 判断是否子集
print(set3.issubset(set4))
print(set3.issuperset(set4))

print("并集:", set4.union(set3))
print("交集:", set4.intersection(set3))
print("差集:", set4.difference(set3))
print("对称差集:", set4.symmetric_difference(set3))

# 转换不可变集合
tu11 = (1, 2, 3, 'ptr', 1)
set99 = frozenset(tu11)
print(set99)
