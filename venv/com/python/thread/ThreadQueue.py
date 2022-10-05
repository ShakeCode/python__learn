import queue
import threading
import time

'''
线程同步队列queue

python2.x中提供的Queue， Python3.x中提供的是queue

见import queue.

Python的queue模块中提供了同步的、线程安全的队列类，包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列PriorityQueue。这些队列都实现了锁原语，能够在多线程中直接使用。可以使用队列来实现线程间的同步。

queue模块中的常用方法:

queue.qsize() 返回队列的大小
queue.empty() 如果队列为空，返回True,反之False
queue.full() 如果队列满了，返回True,反之False
queue.full 与 maxsize 大小对应
queue.get([block[, timeout]])获取队列，timeout等待时间
queue.get_nowait() 相当Queue.get(False)
queue.put(item) 写入队列，timeout等待时间
queue.put_nowait(item) 相当Queue.put(item, False)
queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
queue.join() 实际上意味着等到队列为空，再执行别的操作
'''


exitFlag = 0

class myThread(threading.Thread):
   def __init__(self, threadID, name, queue):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.queue = queue

   def run(self):
      print("Starting " + self.name)
      process_data(self.name, self.queue)
      print("Exiting " + self.name)

def process_data(threadName, queue):
   while not exitFlag:
      queueLock.acquire()
      if not workQueue.empty():
         data = queue.get()
         queueLock.release()
         print("%s processing %s" % (threadName, data))
      else:
         queueLock.release()
      time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
   thread = myThread(threadID, tName, workQueue)
   thread.start()
   threads.append(thread)
   threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
   workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
   pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
   t.join()
print("Exiting Main Thread")
