import threading
import time

'''
线程间同步
​ 如果多个线程共同对某个数据修改，则可能出现不可预料的结果，为了保证数据的正确性，需要对多个线程进行同步。

​ 使用Thread对象的Lock和Rlock可以实现简单的线程同步，这两个对象都有acquire方法和release方法，对于那些需要每次只允许一个线程操作的数据，可以将其操作放到acquire和release方法之间。

​ 需要注意的是，Python有一个GIL（Global Interpreter Lock）机制，任何线程在运行之前必须获取这个全局锁才能执行，每当执行完100条字节码，全局锁才会释放，切换到其他线程执行。

多线程实现同步有四种方式：

锁机制，信号量，条件判断和同步队列。

下面我主要关注两种同步机制：锁机制和同步队列。

（1）锁机制

threading的Lock类，用该类的acquire函数进行加锁，用realease函数进行解锁
'''

class myThread(threading.Thread):  # 继承父类threading.Thread
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter

   def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
      print("Starting " + self.name)
      print_time(self.name, self.counter, 5)
      print("Exiting " + self.name)


def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print("%s process at: %s" % (threadName, time.ctime(time.time())))
      counter -= 1


# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启线程
thread1.start()
thread2.start()

# 等待线程结束
thread1.join()
thread2.join()

print("Exiting Main Thread")
