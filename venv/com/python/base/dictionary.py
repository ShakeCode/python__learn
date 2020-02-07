# 字典类型--无序键值对
di = {}
print(di, type(di), len(di))

# dict转换数组，list为字典类型
dd = dict([('name', 'hello'), ('age', 12)])
dd1 = dict([['name', 'world'], ('age', 34)])
dd2 = dict([['name', 'lijun'], ['age', 99]])
print(dd)
print(dd1)
print(dd2)
print('取对应键值:', dd2['name'])

# 取出对应键值后重新赋值
dd2['name'] = '小强'
print(dd2)

# 添加新键值对
dd2['address'] = '松山湖'
print(dd2)

# del 删除对应键值
del dd2['address']
print(dd2)

# 取出对应key,value
print(dd2.values())
print(dd2.keys())
print(dd2.items())
# 替换键值
dd2.update({'name': 'python'})
print('键值转换为list：', list(dd2.keys()))
print('排序key：', sorted(dd2.keys()))

print("dd2:", dd2)
print("key是否存在:", 'age1' in dd2)

# 引用字典占位！！！！！
dd = {'name': "lijun", 'age': 13, 'address': '松山湖'}
print('name is {name},age is {age},address is {address}'.format(**dd))

# 设置, 取值
dd.setdefault('distance', 123)
print(dd.get('name'), dd['name'], dd, '长度：', len(dd))

# 创建新字典，指定键
print(dd.fromkeys({'name', 'age'}))
