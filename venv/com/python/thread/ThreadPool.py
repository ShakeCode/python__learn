'''
4.1 传统多线程问题？
​ 传统多线程方案会使用“即时创建， 即时销毁”的策略。尽管与创建进程相比，创建线程的时间已经大大的缩短，但是如果提交给线程的任务是执行时间较短，而且执行次数极其频繁，那么服务器将处于不停的创建线程，销毁线程的状态。

​ 一个线程的运行时间可以分为3部分：线程的启动时间、线程体的运行时间和线程的销毁时间。在多线程处理的情景中，如果线程不能被重用，就意味着每次创建都需要经过启动、销毁和运行3个过程。这必然会增加系统相应的时间，降低了效率。

有没有一种高效的解决方案呢？ —— 线程池

4.2 线程池基本原理：
​ 我们把任务放进队列中去，然后开N个线程，每个线程都去队列中取一个任务，执行完了之后告诉系统说我执行完了，然后接着去队列中取下一个任务，直至队列中所有任务取空，退出线程。

使用线程池：
​ 由于线程预先被创建并放入线程池中，同时处理完当前任务之后并不销毁而是被安排处理下一个任务，因此能够避免多次创建线程，从而节省线程创建和销毁的开销，能带来更好的性能和系统稳定性。

线程池要设置为多少？

服务器CPU核数有限，能够同时并发的线程数有限，并不是开得越多越好，以及线程切换是有开销的，如果线程切换过于频繁，反而会使性能降低

线程执行过程中，计算时间分为两部分：

CPU计算，占用CPU
不需要CPU计算，不占用CPU，等待IO返回，比如recv(), accept(), sleep()等操作，具体操作就是比如
访问cache、RPC调用下游service、访问DB，等需要网络调用的操作
那么如果计算时间占50%， 等待时间50%，那么为了利用率达到最高，可以开2个线程：
假如工作时间是2秒， CPU计算完1秒后，线程等待IO的时候需要1秒，此时CPU空闲了，这时就可以切换到另外一个线程，让CPU工作1秒后，线程等待IO需要1秒，此时CPU又可以切回去，第一个线程这时刚好完成了1秒的IO等待，可以让CPU继续工作，就这样循环的在两个线程之前切换操作。

那么如果计算时间占20%， 等待时间80%，那么为了利用率达到最高，可以开5个线程：
可以想象成完成任务需要5秒，CPU占用1秒，等待时间4秒，CPU在线程等待时，可以同时再激活4个线程，这样就把CPU和IO等待时间，最大化的重叠起来

抽象一下，计算线程数设置的公式就是：
N核服务器，通过执行业务的单线程分析出本地计算时间为x，等待时间为y，则工作线程数（线程池线程数）设置为 N*(x+y)/x，能让CPU的利用率最大化。
由于有GIL的影响，python只能使用到1个核，所以这里设置N=1

'''

import queue
import threading
import time


# 声明线程池管理类
class WorkManager(object):
    def __init__(self, work_num=1000, thread_num=2):
        self.work_queue = queue.Queue()  # 任务队列
        self.threads = []  # 线程池
        self.__init_work_queue(work_num)  # 初始化任务队列，添加任务
        self.__init_thread_pool(thread_num)  # 初始化线程池，创建线程

    """
       初始化线程池
    """
    def __init_thread_pool(self, thread_num):
        for i in range(thread_num):
            # 创建工作线程(线程池中的对象)
            self.threads.append(Work(self.work_queue))

    """
       初始化工作队列
    """
    def __init_work_queue(self, jobs_num):
        for i in range(jobs_num):
            self.add_job(do_job, i)

    """
       添加一项工作入队
    """
    def add_job(self, func, *args):
        self.work_queue.put((func, list(args)))  # 任务入队，Queue内部实现了同步机制

    """
       等待所有线程运行完毕
    """
    def wait_allcomplete(self):
        for item in self.threads:
            if item.isAlive(): item.join()


class Work(threading.Thread):
    def __init__(self, work_queue):
        threading.Thread.__init__(self)
        self.work_queue = work_queue
        self.start()

    def run(self):
        # 死循环，从而让创建的线程在一定条件下关闭退出
        while True:
            try:
               # 任务异步出队，Queue内部实现了同步机制
                do, args = self.work_queue.get(block=False)
                do(args)
               # 通知系统任务完成
                self.work_queue.task_done()
            except:
                break


# 具体要做的任务
def do_job(args):
    time.sleep(0.1)  # 模拟处理时间
    print(threading.current_thread())
    print(list(args))


if __name__ == '__main__':
    start = time.time()
    work_manager = WorkManager(100, 10)
    # 或者work_manager =  WorkManager(10000, 20)
    work_manager.wait_allcomplete()
    end = time.time()
    print("cost all time: %s" % (end - start))
