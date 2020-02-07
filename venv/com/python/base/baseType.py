'''
#多行注释使用 ''''''
a=6
b=3;c="123";d='ni'
print(a)
print(a,b,c,d)
'''

def fun():
    print("fun","函数",sep=",")  # 缩进表示函数体

#执行函数
fun()

#显示函数，类型，类库的帮助信息
# help(print)

# 引入time，sys包
import time,sys as s

from math import sqrt

# from datetime import *   易冲突


print(sqrt(12))
print(time.ctime())
print(time.time())
print(time.localtime(time.time()))
# help(time.time)
print(s.path)
# 临时添加路径
# sys.path.append("d://lib//python")

# 引入带空格模块
# sss=__import__("9-34 hello")

#名字
print(time.__name__)
# 详细说明
print(time.__doc__)
# 包名
print(time.__package__)
# 类名
print(time.__loader__)
# 简介
# print(time.__spec__)









