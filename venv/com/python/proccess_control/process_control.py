# 内置函数: range, zip, enumerate
print('a' == 'a')
a = 2
if a >= 1 and a < 99:
    print('a>=1 and a<99')
elif 0 <= a < 1:
    print('0<=a<1')
elif a < 0 or a < -1:
    print('a<0 or a<-1')
else:
    print('未知...')

# str = input('请输入性别：')
# anstr = ['先生', '女士']['female' == str.strip()]
# print('尊敬的', anstr, '你好')

# while 循环
c = 4
while c > 0:
    print('输出:', c)
    c -= 1

for item in ['123', 124, True]:
    print(item)

# 输出大于0的序列
print(range(5))
print(list(range(5)))

# 输出小于0的序列
print(list(range(-5)))
print(list(range(-5, 0)))

# 加入步长
print(list(range(-5, 0, 2)))

for i in range(4):
    print('rang:', i)


# 冒泡排序
def sortMaoPao(a):
    print('原数据:', a)
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    print('排序后:', a)


n = [1, 3, 2, 7, 9, 5]
# sortMaoPao(n)

# 内置函数-zip，将任意多的序列类型数据结合起来，生成新的序列数据，生成的新序列数据中，每个元素都是一个元组
# 2个序列长度不同，以短的序列为主
x = [1, 2, 3, 4]
y = [3, 2, 'hello']
t = zip(x, y)
# 转换为元组，列表后自动销毁，不能重复使用
# print(tuple(t))
# 转换list
# print(list(t))
# 还原元组，*, 相当于unzip
print('还原元组:', *t)

x1 = [1, 2, 'hello', True]
x2 = [3, 4, 'world', False, 'yes']
for t1, t2 in zip(x1, x2):
    print('元组数据:', t1, t2)

# 使用enumerate 内置函数
t = enumerate(x1)
print(tuple(t))

for i, t2 in enumerate(x1):
    print('第', i + 1, '个数据:', t2)

# 流程控制:
# continue, 跳出此次循环
# break 跳出所有循环
# pass 什么都不做，用于维持程序结构的完整性

s = 4
while s > 0:
    if s == 1:
        continue
    elif s == 2:
        break
    else:
        print('数据：', s)
        pass
    s -= 1

aaa = [2, 5, 7, True]
for i, t in enumerate(aaa[:]):
    if i == 2:
        continue
    elif i == 3:
        break
    else:
        print('索引：', i, '数据：', t)
        pass
