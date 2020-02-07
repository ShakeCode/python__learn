# 内置函数对文件创立，读写，删除，修改权限

# 系统级操作：删除，修改权限
# 应用级操作：写入，读取

# 1、删除文件
import os


def removeFile(path):
    try:
        os.remove(path)
    except FileNotFoundError:
        print('找不到文件...')
    else:
        print('成功删除文件...')


# 2、文件的读写操作
# 2.1、打开文件，open 函数，返回文件对象
# 2.2、使用文件对象的read,write 等方法
# 2.3、使用文件对象的close方法

# open(文件名，mode)
# mode -- 读写，只读，只写，二进制等，默认只读模式
'''
r 只读，文件必须存在
w  只写，文件已存在会覆盖文件(清除原来文件内容)，不存在则重新创建文件
+ 读写 (不能单独使用)，使用rw+,r+,w+,a+,ab+,rb+,wb+
a 以只写的方式打开文件，用于文件已存在则追加文件内容，文件不存在则重新创建文件
b  以二进制模式打开

r+ 读写文件必须存在
w+ 读写，文件不存在则创建，已存在则清除已存在文件
a+ 读写，文件不存在则创建新文件，文件已存在则末尾追加内容

'''
# 只有 w,a 可以创建文件
'''
读取方式：
1、文本模式，utf-8, 

2、二进制模式，以字节对象形式读写

2者主要区别：
windows 系统，将行末标识符\r\n 在读取时转为\n, 写操作时\n 转为\r\n， 以文本模式打开二进制文件则会发生问题

linux/unix 系统，行末标识符\n，即文件以\n代表换行，二进制和文本模式没有区别
'''

# open()函数的返回值由打开模式决定
'''
文本模式，返回TextIOWrapper对象
读取二进制模式，即‘r+b’模式，返回bufferedReader对象
写入和追加二进制模式，即'w+b','a+b'模式，返回BufferedWritter对象
读写模式，即含有符号'+'的打开模式，返回BufferedRandom对象
'''


# 1、读取文件
def writeAndRead(path):
    # 清除文件已存在文件内容，写入内容，不存在文件则创建文件
    f = open(path, 'w', encoding='utf-8')
    f.write('你好')
    f = open(path, 'r', encoding='utf-8')
    # 一次性读取到内存
    t = f.read()
    print(t)
    # 关闭文件，正式将内容从缓存写入文件
    f.close()


path = 'd:\\p_file.txt'

writeAndRead(path)


def writeAndRead1(path, word):
    # 只写模式打开文件，向文件尾部写入内容
    f = open(path, 'a+', encoding='utf-8')
    f.write(word)
    f = open(path, 'r', encoding='utf-8')
    # 一次性读取到内存
    t = f.read()
    print(t)
    f.close()


writeAndRead1(path, '\r\n哈哈哈哈哈')

# 二进制形式打开的文件(不需要指定编码格式utf-8)，必须通过二进制写入,否则会报错，将字符串转为字节写入

import os


def binaryWriteReadFile(path, word):
    '''二进制读取文件，追加写入数据'''
    f = open(path, mode='ab+')
    # 转换字符串为字节
    # f.write(b'i love python')
    f.write(bytes(word, encoding='utf-8'))
    # 另一个程序正在使用此文件，进程无法访问
    # os.remove(path)
    f = open(path, 'r', encoding='utf-8')
    # 一次性读取到内存
    t = f.read()
    print(t)
    f.close()


binaryWriteReadFile(path, 'i love python')
# print(binaryWriteReadFile.__doc__)

# 文件对象操作方法
'''
1、read(size), 指定字节大小读取，不指定则读取全部文件内容
2、readline（），读取一行，并在字符串末尾留下换行符‘\n’，到达文件末尾，则返回空字符串
3、readlines（）,读取所有行，存储在列表里面，每个元素一行
4、write（string），将字符串写到文件，返回写入字符数，写二进制文件时需要转换字符串为bytes类型
5、tell(),返回文件对象当前所处位置，是从文件开头开始算起字节数
6、seek(offset,from_what),改变当前文件对象位置，offset-偏移量，from_what-参考位置，取值0（文件头，默认）
，1（当前位置），2（文件末尾）
'''

# 定位文件末尾：f.seek(0,2)
# 定位文件头：seek(0)

# 案例：迭代器读取文件对象

import traceback, os


def iteratorReadFile(path):
    '''文件对象使用迭代器读取文件数据'''
    try:
        print('正在打开文件...')
        f = open(path, 'wb+')
        print('正在写入数据...')
        f.write(b'i love u but u want to go\n')
        f.write(b'please do not go !!!\n')
        f.write(b'emmm... ok i will stay !!!')
    except Exception as e:
        print('写入文件发生异常', e)
        traceback.print_exc()
    else:
        print('成功写入文件内容...')
    finally:
        print('关闭文件...')
        f.close()

    print('\r\n')
    try:
        f = open(path, 'r+')
        '''
        filestr = f.readlines()
        for aa in range(len(filestr)):
            print('读取第', aa + 1, '行', '数据:', filestr[aa])
        '''
        print('开始读取文件:')
        for i, ss in enumerate(f):
            print('读取第', i + 1, '行', '数据:', ss)
        # print('读取所有行:', f.readlines()) #读取所有行: [],前面已经读取出来了
    except FileNotFoundError:
        print('文件不存在！！')
    except Exception as e:
        print('读取文件异常', e)
        traceback.print_exc()
    else:
        print('读取文件成功...')
    finally:
        print('关闭文件...')
        f.close()
        os.remove(path)


# iteratorReadFile('d:/a.txt')

# 简化文件操作流程，打开文件，读取文件，关闭文件,使用with 表达式 as 变量
# 原理：先调用__enter__, 后调用__exit__方法

# 常用做法：二进制形式保存，文本形式方式使用，有利于网络传输，磁盘存储

def withWriteFile(path, word):
    '''with 操作文件'''
    with open(path, 'wb+') as f:
        try:
            f.write(word)
        except Exception as e:
            print('写入文件异常...', e)
            f.write(bytes(word, encoding='utf-8'))

    with open(path, 'r+') as f:
        for line in f:
            print('写入数据为:', line)


# withWriteFile('d:\\b.txt','hello,python!!!')

b = bytes('Python', encoding='UTF-8')
# 输出:b'python';b'Python';Python
print(b'python', b, b.decode(), sep=';')
