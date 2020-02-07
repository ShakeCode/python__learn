# 所有的.py文件都被视为是一个模块
#
# 我们可以用import 文件名的方式把它导入自己的新文件所有的.py文件都被视为是一个模块
#
# 我们可以用import 文件名的方式把它导入自己的新文件

import platform
import sys
import os


def getENV():
    print("module3 里面函数调用 ...")
    print("当前系统:", platform.platform())
    print("安装路径：", sys.path)
    print("代码路径：", os.getcwd())
    print("版本信息:", sys.version_info)

    print(__name__)


# 单元测试:
if __name__ == '__main__':
    getENV()
