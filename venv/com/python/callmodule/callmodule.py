# 同包下引入模块py
# import getEnv
# from getEnv import *
# 相同函数名
def getENV():
    print("打印系统信息...")

def showEnv():
    print("系统信息如下：")
    getENV()   #覆盖模块函数getEnv()

# 放置后面，模块函数会覆盖本类函数，说明python的符号生效规则是‘就近原则’
from getEnv import *

showEnv()
