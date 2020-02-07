#输出语句
'''
年后
'''

"""
年前
"""
print("hello,world")

"""
#变量声明
a=12
b=True
s="你好"+"我是俊"
f=1000.0
print(a)
print(b)
print(s*2)
print(f)
print(s[0])

#字符串截取
str="123456"
print(str+"7")
print(str[0:-1])
print(str[0])
print(str[1:5])
print('------------------------------')
print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义


# input("\n\n按下 enter 键后退出。")
import sys; x = 'runoob'; sys.stdout.write(x + '\n')

print( "x", end="ssss" )
print( "y", end="aa" )

import sys
print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)
print(sys.api_version);

print("是否正确:",True)

from sys import argv, path  # 导入特定的成员
print('================python from import===================================')
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path

a=b=2
print(a)

a,b,c,d=1,True,1001.0,4+3j
print(c)
print(type(c),type(d),isinstance(a,int)) #查看数据类型
print(True+1)

print(2**3)
print(2//3)
print(2/3)

"""

"""
list=["a,","b","c","d"]
print(list[0])
print(list[1:3])
print(list[:])
print(list)
print(list[:2])
print(list[2:])
print(list*2)
print(list+list)
list[0]=1
print( type(list[1]))
print(list[1][:])

tuple=("a",1,True,["a",100.0,False])
print(tuple)
"""

"""
set={}
set1=("1","2","3")
print(set)
print(set1)

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')

a={1,2,1}
print(a)
b={2,3}
print(b)
print(a-b)  #差集
print(a|b)  #并集
print(a&b)  #交集
print(a^b)  #互相没有的元素
"""

dict ={"age":"年龄","name":"名字"}
# dict[age]="年龄"   #已声明，不可继续加同名元素
print(dict)
print(dict["age"])
print(dict["name"])
print(dict.keys())
print(dict.values())
print(type(str(dict)))  #转为str





