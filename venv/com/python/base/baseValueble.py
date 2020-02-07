# 基础数据类型：
# numbers, (int, float, bool, complex（复数）)
# string,
# tuple-数组,
#  sets 集合,
#  dictionary-字典

a, b, c, d, e, f, g, h, i, j = 2, '2', "3", True, 4 + 7j, [1, 2, "3", False], {"name": "test"}, None, (1, 2, 3, "4"), {
"111", 123, True}
print(a, b, c, d, e, f, g, h, i, j)

# 查询类型或者类型的所有属性
dir(int)

# 查询帮助文档
# help(list)

# 变量的本质就是对象，包含身份-内存地址, 类型，值
print("指针地址:", id(a), "类型:", type(a), "值:", a)
print("指针地址:", id(b), "类型:", type(b), "值:", b)
print("指针地址:", id(c), "类型:", type(c), "值:", c)
print("指针地址:", id(d), "类型:", type(d), "值:", d)
print("指针地址:", id(e), "类型:", type(e), "值:", e)
print("指针地址:", id(f), "类型:", type(f), "值:", f)
print("指针地址:", id(g), "类型:", type(g), "值:", g)
print("指针地址:", id(h), "类型:", type(h), "值:", h)
print("指针地址:", id(i), "类型:", type(i), "值:", i)
print("指针地址:", id(j), "类型:", type(j), "值:", j)

print(float("3.13"))
print(int(3.13))
print(int(True))

aa = 1
bb = 3
cc = None
dd = 5
print(aa < bb)
print("是否相等:", aa == bb)
print(aa != bb)
print(aa >= bb)
# 地址比较：is  is not
print(cc is None)
print(aa is bb)
print(aa is not bb)
# 链式比较
print(aa < bb < dd)

# 算术运算符>比较运算符
print(1.1 == 1.1 - 0.1)

aaa = -123
bbb = -123
print(aaa == bbb)
print("地址是否相等:", aaa is bbb)
print(id(aaa), id(bbb))

# 不同模块，创建对象存在不同缓存策略

# 布尔运算符
print(not True)
print(1>2 and 1>0)
print(1>2 or 1>0)
print(not 1>2)


