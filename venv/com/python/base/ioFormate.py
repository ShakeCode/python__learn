a, b = 123, True
# 默认空格为分隔符
print(a, b)
print(a, b, sep=",")
print(a, b, sep=",", end="\n")
# 默认输出屏幕，可指定文件
print(a, b, sep=",", end="\n")
# 占位符
print("hello %s" % "world")

# %m.nf
# m-总长度，n小数点后位数

# 长度4小于7，空格补齐
print("%7.2f" % 23.45)
# 长度4小于7，空格补齐,小数位数不足4,补齐0
print("%7.4f" % 23.45)
# 总长度比实际长度短，总长度约束失效
print("%2.1f" % 23.45)

# 小数4位后，总长度6小于7，总长度失效
print("%6.4f" % 23.45)

x = 5
print(":", str(5).rjust(2), str(x * x).rjust(3), end=", ")
print(str(x * x * x * 10).rjust(4))

print(":", "%2d %3d %4d" % (x, x * x, x * x * x))

# 字符串模版格式化说明:
'''
{0: 2d}
大括号第一位用于维护与后面占位内容的对应关系
冒号后面 格式为: [补齐字符][对齐方式][宽度]
补齐字符：任意字符，但只能一个字符，没有就默认空格
对齐方式：左对齐 < 、  右对齐 >、 居中 ^
宽度：m.nf
'''
print(":", '{0:2d} {1:3d}, {2:4d} {0:4d}'.format(x, x * x, x * x * x))

print('{0:=>10d}'.format(5))
print('{0:=<10d}'.format(5))
print('{0:=^10d}'.format(5))

print('{0:&<10.3f}'.format(0.5))
print('{0:-^10}'.format("hello"))

s = 3
print(":", '{0} {1},{2} {0}'.format(s, s * s, s * s * s))

# 高级占位运用
# 引用列表，数组占位
list = [1, 2, 3, 4, True]
print(":", '{0} {1},{2} {3} {0},{4}'.format(*list))
tuple = (1, 2, True, "hello")
print(":", '{0} {1},{2} {3} {0}'.format(*tuple))
# 引用字典占位！！！！！
dd = {'name': "lijun", 'age': 13, 'address': '松山湖'}
print('name is {name},age is {age},address is {address}'.format(**dd))

print("ss ".strip())
print("      ss ".lstrip())
print(" ss     ".rstrip())

print("5" + "hello")
print("hello " * 3)

# 字符串的序列特性
print("hello"[0])
print("hello"[1])
print("hello"[2])

# 负数表示右边开始,索引从1开始
print("hello"[-1])

# 检索字符在字符串中的索引位置
print("hello".index('o'))
print("hello".index('e'))

# 切片[起始：结束：步长]
# 步长默认是1
print("切片:")
print("world"[:])
print("world"[1:4:2])
print("world"[1:4])
print("world"[1:5])

print("world"[::])
# 第一位开始，步长2
print("world"[::2])
# 反向读取，步长2
print("world"[::-2])

# 逆序读取
print("world"[::-1])
print("world"[-2::-1])
print("world"[:-0:-1])

# 字符串不能改变，以下报错：
# "hello"[3]='qq'

xxx = 'hello'
# 字符长度
print(len(xxx))
# 字符编码最大值，最小值
print(max(xxx))
print(min(xxx))

# 判断是否存在字符
print("he" in xxx)

print('1'.join('2'))
print('hello'.find('e'))
print('hello world'.split(" "))

# 检查单个字符的编码格式
print(ord("我"))

# 根据字符编码返回字符

print(chr(25105))

b = ['I', 'love', 'u']
# 将b列表按照空格连接
print(" ".join(b))

# 首字母转为大写
print("i love u py".title())


help("".title)