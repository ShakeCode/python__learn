# 一、任意对象序列化--- 使用pickle, unpickle函数，实现对象和文本，二进制之间的转化

# 缺点: 不支持并发访问持久化对象

import pickle as pick

# 对象转换为二进制
# pick.dumps(obj==, protocol=None,*,fix_imports=True)

# obj -- 转换对象
# protocol -- 转码协议
# 0 - ascii码表示, 2为旧版本二进制协议，3-新的二进制协议，4-更新的二进制协议，为指定则默认为3

# 对象序列化二进制的对象，并写入文件
# pick.dump(obj=,file=,protocol=None,*,fix_imports=True)
# file 必须有write方法，支持二进制数据写入

# 从给定pickle 二进制对象数据中读取并返回对象
# pick.loads(data=,*,fix_imports=True,encoding='ASCII',errors='strict')

# 读取指定的序列化数据文件，并返回对象
# pick.load(file=,*,fix_imports=True,encoding='ASCII',errors='strict')
# file对象必须有read(),readline()方法


tupl = ('i love python', [1, 2, 3], None)
# 转为二进制对象
pl = pick.dumps(tupl)
# 二进制对象转为pyhon对象
p2 = pick.loads(pl)
print(p2)


def change(path, obj):
    '''二进制对象文件与对象互转'''
    with open(path, 'wb') as f:
        # 将对象转为二进制对象文件
        pick.dump(obj, f, pick.HIGHEST_PROTOCOL)

    with open(path, 'rb') as f:
        # 将二进制对象文件转为py对象
        t3 = pick.load(f)
        print(t3)


change('d:/c.pkl', tupl)

# 二、高并发访问持久化对象，使用ZODB模块
# ZODB-面向对象数据库系统，存储对象数据，支持事务，并发控制
