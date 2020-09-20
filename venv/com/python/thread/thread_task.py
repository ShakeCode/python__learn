# 线程的创建
# _thread python3以前版本的thread模块的重命名，低级别，原始的线程，提供一个简单的锁，功能比较局限
# threadind python3 以后的线程模块

import threading

# 查看当前线程实例
print(threading.current_thread())  # 主线程名字：+线程ID ： <_MainThread(MainThread, started 1424)>

# 返回正在运行(启动后结束前)的线程list
print(threading.enumerate(), '运行的线程数量: ', len(threading.enumerate()))

# 返回正在运行的线程数量
print(threading.activeCount())

# 创建子线程，子线程的名字需要指定，不指定时，会默认给个名字
# 1、通过threading.Thread 类实例化实现，调用实例化对象的start()方法创建线程
# 2、用threading.Thread 类派生一个新的子类，再新建实例化，调用start()方法创建线程

import threading


def handle(sid):
    '''线程处理函数，内部打印当前线程的参数和名称'''
    print('Thread %d run' % sid, threading.current_thread())


# 循环创建多线程
for i in range(1, 11):
    # 计算器作为参数传入新建的线程中
    t = threading.Thread(target=handle, args=(i,))
    # 启动线程
    t.start()
    # print('线程 %d 已启动...'%i)

# 打印主线程信息
print('main thread', threading.current_thread())

# 类定义：
# class threading.Thread(group=None,target=None,name=None,args=(),kwargs{},*,daemon=None)

'''
参数说明:
group - 默认为空，为实现线程组ThreadGroup类预留
target -- 线程的执行函数，默认为空
name -线程名称，默认是类似于Thread-N形式的名字,N-十进制的数字
args -元组类型，表示在调用target时传入的参数
kwargs={ },字典类型，即在调用target时传入的参数
deamon -bool类型，为True时，表明为守护线程。这个值必须与主线程身份一致，即如果主线程不是守护线程
所有的子线程都被设为false, 否则会报RuntimeError异常
'''

# 守护线程-- 进程退出时，不用等待这个线程退出，也可设置setDeamon()指定守护线程

# threading.Thread涉及的方法
'''
run --线程活动的方法
start  --启动线程活动
join  -- 连接线程，等待所有线程完成,参数timeout, 用于阻塞当前上下文环境的线程，直到调用此方法的线程终止，或到达指定参数timeout
isAlive -- 返回是否活动线程
getName --获取线程名
setName -- 设置线程名
'''

'''
运行原理:
threading.Thread实例化后，完成线程创建
start()调用用，线程进入就绪状态，等待cpu分配时间片
获取时间片，进入运行状态，执行run()
run()函数执行期间，线程可被中断，进入阻塞状态
阻塞状态结束后，线程回到就绪状态，接着运行
运行结束（中途退出运行也是），线程进入退出状态
'''

# 重载run( )

import threading


def handle(sid):
    print('Thread %d run 启动' % sid, threading.current_thread())


class MyThread(threading.Thread):
    '''自定义线程类'''
    def __init__(self, sid):
        threading.Thread.__init__(self)
        self.sid = sid

    # 重载run()
    def run(self):
        handle(self.sid)


for i in range(1, 11):
    t = MyThread(i)
    t.start()

