import asyncio
import re

async def browser(host, port=80):
    # 连接host
    reader, writer = await asyncio.open_connection(host, port)
    print(host, port, '连接成功!')

    # 发起 / 主页请求(HTTP协议)
    # 发送请求头必须是两个空行
    index_get = 'GET {} HTTP/1.1\r\nHost:{}\r\n\r\n'.format('/', host)
    writer.write(index_get.encode())

    await writer.drain()  # 等待向连接写完数据（请求发送完成）

    # 开始读取响应的数据报头
    while True:
        line = await reader.readline()  # 等待读取响应数据
        if line == b'\r\n':
            break

        print(host, '<header>', line)

    # 读取响应的数据body
    body = await reader.read()
    print(host, '<content>', body)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [browser(host) for host in ['www.dushu.com', 'www.sina.com.cn', 'www.baidu.com']]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    print('---over---')
