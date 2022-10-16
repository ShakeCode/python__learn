import base64
import os

from Crypto.Cipher import AES

filename = '1.key.txt'


# 把文件内容以byte字节形式读写到缓冲区中。
def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    f.close()
    return buf


print(list(read_into_buffer(filename)))
password = 'b1d10e7bafa44212'.encode()  # 秘钥，b就是表示为bytes类型
iv = base64.b64decode('AQIDBQcLDRETFx0HBQMCAQ==')  # iv偏移量，bytes类型
text = read_into_buffer(filename)  # 需要加密的内容，bytes类型
# AES.MODE_CBC 表示模式是CBC模式
aes = AES.new(password, AES.MODE_CBC, iv)  # CBC模式下解密需要重新创建一个aes对象
den_text = aes.decrypt(text)
print("明文：", list(den_text))
keys = list(den_text)
hex16 = []
for i in keys[:16]:
    hex16.append(i)


def print_bytes_hex(data):
    lin = ['%02X' % i for i in data]
    print(" ".join(lin))


print_bytes_hex(hex16)
