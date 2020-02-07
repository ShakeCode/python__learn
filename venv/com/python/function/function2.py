# 混合使用参数
# 1、元组参数在前面，单形参在后面
def recoder(*person, age):
    if len(person) != 0:
        print('姓名：', person[0], '年纪：', age)


# 指定元组形参在前面，单形参指定形参名称
recoder('wuhan', age=12)


# 2、元组参数在后面，单形参在前面
def recoder(age, *person):
    if len(person) != 0:
        print('姓名：', person[0], '年纪：', age)


# 可不指定形参名称
recoder(100, 'garry')


# 3、字典，元组解包参数，单形参混合, 字典参数必须在最后面！！！！！！
def recoder(age, *person, **dicPerson):
    if len(person) != 0:
        print('姓名：', person[0], '年纪：', age)
    if len(dicPerson) > 0:
        print(dicPerson)


# 保证字典参数在后面
recoder(300, 'naying')
recoder(200, 'jaychou', **{'math': 122, 'english': 999})


# 4、元组，单形参，字典参数
def recoder(*person, age, **dicPerson):
    if len(person) != 0:
        print('姓名：', person[0], '年纪：', age)
    if len(dicPerson) > 0:
        print(dicPerson)


# 指定参数名称，在后面
recoder(30000, age='2019')
recoder(168, age='2020', **{'year': 2020, 'month': 2})

# 5、字典参数没有在最后面报错：
'''
def recoder(*person, **dicPerson, age):
    if len(person) != 0:
        print('姓名：', person[0], '年纪：', age)
    if len(dicPerson) > 0:
        print(dicPerson)
'''
