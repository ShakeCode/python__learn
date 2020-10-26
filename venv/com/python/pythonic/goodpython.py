# 链式运算
age = 16
if 12 < age < 18:
    print("young age")
else:
    print("old age")
# 同理
print(False == False == True)

# 三目运算
gender = 'male'
text = '男' if gender == 'male' else '女'
print(text)

# 真值判断
if ["a"]:
    print("hello")
if not "":
    print("world")

# 真假值对照表：
# 类型 False True
# 布尔 False （与0等价） True （与1等价）
# 字符串 ""（ 空字符串） 非空字符串，例如 " ", "blog"
# 数值 0, 0.0 非0的数值，例如：1, 0.1, -1, 2
# 容器 [], (), 至少有一个元素的容器对象，例如：[0], (None,), ['']
# None None 非None对象

# 字符串格式化
print("welcome to %s and following %s" % ("foofish.net", "vttalk"))
# pythonic
print("welcome to {blog} and following {wechat}".format(blog="foofish.net", wechat="vttalk"))
print("welcome to {0} and following {1}".format("foofish.net", "vttalk"))

# for 循环
for x in [1, 2, 3]:
    print(x)

for x in range([1, 2, 3].__len__()):
    print(x)

# 列表切片
li = ["a", "p", "p", "l", "e"]
# 第1到第4个元素的范围区间
print(li[1:4])
# 奇数
print(li[1::2])
# 倒叙
print(li[::-1])
# 复制
print(li[::], li[:])

# 获取字典元素
d = {'name': 'foo'}
if d.__contains__('name'):
    print(d['name'])
else:
    print('unkonw')
# pythonic
print(d.get("name", "unknow"))


# 多if判断返回
def getV(x):
    return {"apple": "red", "orange": "orange", "banana": "yellow"}.get(x, "0")


print(getV("banana"))

# 预设字典默认值
data = [('foo', 10), ('bar', 20), ('foo', 39), ('bar', 49)]
# 　第一种方式
groups = {}
for (key, value) in data:
    groups.setdefault(key, []).append(value)

# 第二种方式
from collections import defaultdict

groups = defaultdict(list)
for (key, value) in data:
    groups[key].append(value)

print(groups)

# 字典推导式
# 在python2.7之前，构建字典对象一般使用下面这种方式，可读性非常差
numbers = [1, 2, 3]
my_dict = dict([(number, number * 2) for number in numbers])
print(my_dict)  # {1: 2, 2: 4, 3: 6}
# pythonic
numbers = [1, 2, 3]
my_dict = {number: number * 2 for number in numbers}
print(my_dict)  # {1: 2, 2: 4, 3: 6}
# 还可以指定过滤条件
my_dict = {number: number * 2 for number in numbers if number > 1}
print(my_dict)  # {2: 4, 3: 6}

# 列表推导式
# 生成1-100的奇数
odd = [i for i in range(1, 100) if i % 2 == 1]
print("列推导式：", odd)
# 集合a，b分别去一个数，找出和大于100的所有组合
result = [(x, y) for x in [1, 2, 3] for y in [99, 100] if x + y > 100]
print("列推导式：", result)

student_names = [u"bob", u"peter", u"macy"]
# 查找出名字里面有 m字母的同学
that_people = [name for name in student_names if u'm' in name]
print(that_people)

# list去重
li = [10, 1, 2, 3, 4, 4, 3]
print(list(set(li)))
# 排序
li.sort()
print(li)

# 遍历2个for
l1 = ["江西", "广东", "江苏", "福建", "湖南"]
l2 = ["南昌", "广州", "南京", "福州", "长沙"]
for province, city in zip(l1, l2):
    print(province, city)

# izip为itertools中的一个方法。zip在内存中会生成一个新的列表，需要更多的内存。izip相比较于zip效率更高。在python 3.x中，izip更名为zip，替换了原来的zip成为了python 的内置函数。

d = {"province": "广东", "city": "深圳"}
for key, value in d.items():
    print(key, value)

# 需要将以下列表的元素以长度进行分组
l = ["red", "green", "blue", "yellow", "black", "pink", "grey"]
from collections import defaultdict

d = defaultdict(list)
for item in l:
    key = len(item)
    d[key].append(item)
print(d)

# 连接字符串
print("".join(["h", "e", "l", "l", "o"]))

# 需要将以下列表的元素进行增删操作:
from collections import deque

l = ["哈哈", "呵呵", "嘿嘿"]
l = deque(l)
del l[0]
l.popleft()
l.appendleft("哼哼")
print(l)


def readFile():
    global data
    f = open('a.txt')
    try:
        data = f.read()
    finally:
        f.close()
    # Pythonic
    with open('a.txt') as f:
        data = f.read()


# 文件读写带close
# 普通写法
# readFile()

# 解构赋值
student = [['Tom', (98, 96, 100)], ['Jack', (98, 96, 100)]]
for name, (first, second, third) in student:
    print(name, first, second, third)

# 序列解包
a, *middle, c = [1, 2, 3, 4]
# a = 1, middle = [2, 3], c = 4
print(a, middle, c)

# lambda 表达式
a = [3, 4, 5]
b = [i for i in a if i > 4]
print(b)
# Or:
b = filter(lambda x: x > 4, a)
print(list(b))
# map
a = [3, 4, 5]
a = [i + 3 for i in a]
# Or:
a = map(lambda i: i + 3, a)
print(list(a))

#使用占位符
filename = 'foobar.txt'
basename, _, ext = filename.rpartition('.')
print(basename,_,ext)
