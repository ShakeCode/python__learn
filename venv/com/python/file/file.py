import os;

# filePath=input("请输入文件路径：")
file = open("d:/python-note.txt", "r+")
# str=input("请输入需要记录的内容:")
# file.writelines("\n"+str)
print("循环读取文件内容:")
for line in file:
    # print("写入的文件内容为: ",file.readlines())
    print(line)
file.close()
