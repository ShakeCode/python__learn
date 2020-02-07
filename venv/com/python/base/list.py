li = [12, 3.44, 'hello', True, ["jun", 234]]

# 数据类型可互不相同，相互嵌套
print(li)

li = []

print(li)

# 尾部添加元素
li.append("hello")

print(li)
li[len(li):] = 'world'

# 将list添加到自己尾部
li.extend(["my", "dear"])
print(li)

# 指定索引位置插入数据
li.insert(0, "hahaha")
print(li)

# 移除某元素内容，不存在会报错
# li.remove("aaa")

# 指定索引位置移除列表
li.pop(0)
print(li)

# 移除最后一个元素
print("移除元素:")
li.pop()
print(li)

li.__delitem__(0)
# li.__add__(["nihao"])
print(li)

# 清除列表
# li.clear()
# del li[:]
# print(li)

# 返回元素出现次数
print(li.count('o'))

# 排序
li.sort()
print("排序后:", li)

# 逆序排列
li.reverse()
print(li)

# 添加列表至尾部
li[len(li):] = ["nihao"]
print(li)

li55 = li + ["mama"]
print(li55)

# extend效率高于+,内存地址不改变

# 删除指定位置元素
del li55[-1]
print(li55)

# 列表复制，内存地址不变
li2 = li55
print("li2 is :", li2)

print(id(li55), id(li2))

# 删除变量，list还可以访问，内存地址指向的数据还没有删除，只是传递内存地址
# del 只删除变量，不会删除指向的数据
del li2
print(li55)

# 删除数据,内存指向的数据全部删除，在内存中只标记为无效数据，并未真正回收
li3 = li55
del li55[:]
print(li3)
print(li55)

# 回收内存
# import gc
# del  li55
# gc.collect()

# li55 嵌套，实际开发使用numpy包处理多维数组
li4 = [
    [True, 123, "nihao"],
    ["hello", 123],
    [1, 2, False, [123]],
]
print(li4)

# 实现队列(先进先出)，栈（后进先出）
queue = []
queue.insert(0, True)
queue.insert(1, "123")
queue.insert(2, 11)
print(queue)

print("取出第1个元素:", queue.pop())
print("取出第2个元素:", queue.pop())
print("取出第3个元素:", queue.pop())

print(queue)

stack = []
stack.append(True)
stack.append(False)
stack.append(123)
print(stack)

print("取出第1个元素:", stack.pop())
print("取出第2个元素:", stack.pop())
print("取出第3个元素:", stack.pop())

print(stack)

# deque: 2端存入读取，特殊list
from collections import deque

# 创建空结构体
queuestack = deque()
queuestack.append(1)
queuestack.append(2)
queuestack.append("hello")

print("转换为list：", list(queuestack))
# 队列方式读取数据 取出第一个元素，先进先出
print(queuestack.popleft())
# 堆栈方式读取数据 取出最后一个元素，后进先出
print(queuestack.pop())

print(queuestack)

# 切片[起始：结束：步长]
ll = [1, 2, 4, 3, 5, 1.2]
print("倒数第二位:", ll[-2])
print("倒数第一位:", ll[-1])
print(sorted(ll))
print(sorted(ll[0:]))
print(sorted(ll[1:]))
print(sorted(ll[1:3]))

# 列表数据可修改
ll[0]=11
print("修改后列表:",ll)

# 列表过滤函数:filter
score = [
    ("lijun", 50, 60, 90),
    ("chentao", 70, 70, 81),
    ("xiaohong", 40, 80, 100)
]


# 定义过滤器比较器:
def handle_filter(a):
    # 索引1开始切片排序
    s = sorted(a[1:])
    if s[-1] >= 90:
        return True
    return False


# 过滤出最后一科成绩大于等于90的人员
aa = list(filter(handle_filter, score))
print("过滤后成绩：", aa)

li66=[]

