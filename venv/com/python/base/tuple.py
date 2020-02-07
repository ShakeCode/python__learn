tu = (1, 1.2, False, 'hello', [123, True, 1.98])
print("数据：", tu, "类型：", type(tu), "长度:", len(tu))
# 索引从0开始
print(tu[0])
print(tu[-1])
print(tu[-2])
print("切片数据：", tu[1:])
print("切片数据：", tu[1:4])

# 数组元素不可修改！！！！和列表类型不一样
# tu[0]=False

# 特殊规则，0个元素，使用小括号
tu1 = ()
print("0个元素数组:", tu1)

# 数组只是列表的只读版本，功能类似

