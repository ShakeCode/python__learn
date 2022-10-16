players = ['Kobe', 'Lebron', 'Stephen']
for (i, j) in enumerate(players):
    print(i, j)

## 展示一下enumerate函数的作用
print(list(enumerate(players)))

numbers = [12, 454, 123, 785, 65]
for n in iter(numbers):
    print(n)

l = 0
while l < len(numbers):
	print(numbers[l])
	l += 1

numbers = [12, 454, 123, 785, 65]
for i in range(len(numbers)):
    print(i, numbers[i])

for (i, j, k) in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
    print(i, j, k)

a = [1, 2, 3]
b = [4, 5, 6]
print(list(zip(a, b)))
[(1, 4), (2, 5), (3, 6)]
# 如果zip的两个数组长度不一致，则会按照短的进行zip
print(list(zip(a, b)))
[(1, 7), (2, 8)]

# 递归

numbers = [12, 454, 123, 785, 65]


def recursion(list, index):
    if index == len(list):
        return
    else:
        print(list[index])
        recursion(numbers, index + 1)


recursion(numbers, 0)