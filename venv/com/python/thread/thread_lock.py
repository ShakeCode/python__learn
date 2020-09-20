# 一、互斥锁解决线程之间数据不同步问题

# 复现线程数据不同步问题
import threading
import time

num = 1


def handle(arg):
    global num
    num *= 2
    time.sleep(arg % 2)
    print('thread-handle', arg, ':', num)


threads = []

for i in range(1, 11):
    t = threading.Thread(target=handle, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()  # 等待所有线程完成

print('main thread join is finished')

# 二、创建锁 threading.RLock类
'''
涉及方法：
threading.Lock.acquire()  # 开始对线程进行保护，acquire之后的代码，只允许一个线程执行进入
threading.Lock.release()   #停止保护（释放锁资源）,release之后的代码允许其他线程进入

注意：
    1、应尽量少使用锁，因为牺牲了性能，加锁也尽量是保护的区域代码减少
    2、加锁后必须释放锁
'''

import threading
import time

num = 9
lock = threading.RLock()  # 锁的实例化


def zHandle(arg):
    lock.acquire()  # 加锁
    global num
    num *= 2
    time.sleep(arg % 2)
    print('thread-lock', arg, ':', num)
    lock.release()  # 释放锁


def beginThread():
    threads = []

    for i in range(1, 11):
        t = threading.Thread(target=zHandle, args=(i,))
        t.start()
        threads.append(t)

    # 等待所有线程完成
    for t in threads:
        t.join()

    print('main threa is finished')


beginThread()

