# 多线程是无法返回值的，因此需要有一个地方来存多线程的结果，这个存储器就是threading.
import threading
import time
from queue import Queue

# def job(l, q):
#     for i in range(len(l)):
#         l[i] = l[i]**2
#     return l      # 在普通的函数定义时，使用return来返回值

def job(l, q):
    for i in range(len(l)):
        l[i] = l[i]**2
    q.put(l)        # 在多线程中，即使return了，也只能return到当前线程，无法给主线程调用，因此这里用一个更加全局性的存储器——queue（队列）——来存储多个线程的结果
    time.sleep(1)

def multithreading():
    q = Queue()
    threads = []
    data = [[1,2,3],[3,4,5],[4,4,4],[5,5,5]]
    for i in range(4):
        t = threading.Thread(target=job, args=(data[i], q))
        t.start()
        # t.join()  # 是不能在这里join的，如果在这里join()了，将等待第一个线程结束之后，在执行下面一条命令，在生成第二个线程，以此类推，多线程编程了串行！
        threads.append(t)

    # 至于下面的两个循环，实践证明是可以合并的
    for thread in threads:
        thread.join()
    results = []
    for _ in range(4):
        results.append(q.get())     # 这里为什么不能写入上面的循环，如果单个线程执行的慢，q.get()是无法取到值的

    # 合并写法
    # results = []
    # for thread in threads:
    #     thread.join()
    #     results.append(q.get())

    print(results)


if __name__ == '__main__':
    multithreading()