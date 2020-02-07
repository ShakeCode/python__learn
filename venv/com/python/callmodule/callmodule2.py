# 回到根目录，就可调用module3包
import sys
sys.path.append("../")

from module3.getEnv import *

getENV()