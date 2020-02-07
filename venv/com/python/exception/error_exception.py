'''
错误分类：
1、语法错误
2、运行时错误 a =1/0  也即是异常
'''
# ZeroDivisionError
# a = 1 / 0

# 异常产生后程序会停止，可捕捉异常

# 异常基本使用
"""
try:
    x = input('请输入一个被除数:')
    a = 30 / int(x)
# 捕捉单个异常
except ValueError:
    print('输入无效数据，请重新输入...')
# 捕捉多个异常
except (ZeroDivisionError, NameError):
    print('被除数不等于0，请重新输入')
# 其他异常：
except Exception as e:
    print('程序异常了...',e)
# 无发生异常执行：
else:
    print('30除以:', x, '等于', int(a))
"""

# 输出异常详细信息
# 使用sys模块的exe_info(以元组的形式返回), last_traceback 函数，或者使用traceback 模块的相关函数

import sys

try:
    x = 1 / 0
except:
    print(sys.exc_info())
    # 打印异常元组，最后一个为traceback对象，可以查看异常调用栈信息
    # ：(<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero',), <traceback object at 0x02093648>)
    print('异常了...')

# 查看traceback对象内容（包含：文件名，行数，模块名，代码）
'''
import traceback, sys
try:
    x = 2 / 0
except:
    traceback.print_tb(sys.exc_info()[2])
    # traceback.print_exception(*sys.exc_info())
    print('异常了...')
else:
    print('bye')
'''

# 使用print_exc
import traceback, sys

'''
try:
    x = 2 / 0
except:
    traceback.print_exc()
    # traceback.print_exception(*sys.exc_info())
    print('异常了...')
else:
    print('bye')
'''

# 创建异常，抛出异常
# raise [Exception [,args,[,traceback]]]
# Exception 异常类型，参数可选，默认none,
# traceback 可选，代表需要追踪的对象
'''
try:
    x = input('请输入一个被除数:')
    if int(x) == 0:
        raise ValueError('0不能做被除数')
except Exception as e:
    print(e)
except:
    print('其他异常')
else:
    print('您已输入：', int(x))
finally:
    print('成功输出！！！')
'''

# 异常的最终操作 finally，一般做清理内存，关闭io流功能

# 断言，校验自己的判断的对错,对则程序继续执行，错则报错
assert 1 == 1
# 指定抛出错误信息
# assert 1!=1 ,'1不等于1，报错'

