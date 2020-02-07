# 单行字符串，单引号，或者双引号，作逻辑控制
a, b = 'line', "line2"
print(a, b)

# \连接下一行
c = 'string' \
    'string2'
print(c)

# 多行字符串，使用3个引号（单或者双）表示，"""xxx"""
# 每行隔开可使用回车分开,常用于函数描述
dd = """line
line2
line3"""
print(dd)

ee = '''
hello
world
'''
print(ee, type(ee))

# 转换字符串
aa = str(5)
print("\n", aa, type(aa))

print("first\tsecond")
# 关闭转义，字符串前面添加r 或者 R,使用函数repr()转换回原来的字符串
print(R"thrid\tfourth")
print(r"thrid\tfourth")
print("thrid\tfourth")

print(repr('thrid\tfourth'))
print(repr(R'thrid\tfourth'))

# 原字符串转为转义字符串
ccc = R'line\tline'
print(eval("'" + ccc + "'"))

# 打开文件规避转义字符问题,以为会出现转义错误
path = "c:\temp.txt"

# 改为：
path = "c:\\temp.txt"
path = r"c:\temp.txt"
path = "c:/temp.txt"
