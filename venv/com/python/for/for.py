list=[{"name":"lijun","age":12},{"name":"liming","age":20}]
print("遍历字典:")
for x in list:
    print(x)
    for k,v in x.items():
        print("key",k,"\tvalues:",v)
print("遍历字符串:")
for s in "sdf":
    if s=="d":
        break
    print(s)

print("遍历数字范围:")
for i in range(5):
    print(i)

print("遍历list:")
array=["apple","banana","pear",12]
for x in range(len(array)):
    print("索引：",x,"索引值:",array[x])

print("遍历元组:")
array1=("元组1",1)
for x in range(len(array1)):
    print("索引：",x,"索引值:",array1[x])

print("while循环:")
i=3
while i<5:
    print(i)
    i+=1
else:
    print("跳出循环")

'''迭代器'''
for i,e in enumerate(list):
    print("第",i+1,"个元素:",e)

list='python'
for i in(len(list),-1,-1):
    print(i)