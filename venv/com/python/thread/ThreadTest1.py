import threading
import time

'''
​ python主要是通过thread和threading这两个模块来实现多线程支持。python的thread模块是比较底层的模块，python的threading模块是对thread做了一些封装，可以更加方便的被使用。但是python（cpython）由于GIL的存在无法使用threading充分利用CPU资源，如果想充分发挥多核CPU的计算能力需要使用multiprocessing模块(Windows下使用会有诸多问题)。

​ python3.x中已经摒弃了Python2.x中采用函数式thread模块中的start_new_thread()函数来产生新线程方式。

​ python3.x中通过threading模块创建新的线程有两种方法：一种是通过threading.Thread(Target=executable Method)-即传递给Thread对象一个可执行方法（或对象）;第二种是继承threading.Thread定义子类并重写run()方法。第二种方法中，唯一必须重写的方法是run()
'''

def target():
    print("the current threading %s is runing" % (threading.current_thread().name))
    time.sleep(1)
    print("the current threading %s is ended" % (threading.current_thread().name))


print("the current threading %s is runing" % (threading.current_thread().name))
## 属于线程t的部分
t = threading.Thread(target=target)
t.start()
## 属于线程t的部分
t.join()  # join是阻塞当前线程(此处的当前线程时主线程) 主线程直到Thread-1结束之后才结束
print("the current threading %s is ended" % (threading.current_thread().name))
