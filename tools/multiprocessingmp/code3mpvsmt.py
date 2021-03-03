import multiprocessing as mp    # 多进程的模块
import threading as td
from queue import Queue
import time

def job(q, n):     # 进程调用测程序，传递的参数为一个queue（队列）对象
    res = 0
    for i in range(n):
        res += i**2
    q.put(res)      # 把结果（就是主进程中函数的返回值）存入队列

# 多进程的执行方案
def multicore(m, n):
    q = mp.Queue()
    plist = []
    signle_size = int(n/m)      # 分配给每个进程的执行规模

    # 把规模n分配给m个进程执行，每个进行执行n/m（即signle_size）
    for e in range(m):
        p = mp.Process(target=job, args=(q, signle_size))
        # 生成进程，并传入要执行的操作（函数），args=参数列表，只传一个参数的时候注意要在参数后面加一个逗号，因为args需要一个可迭代的参量
        p.start()  # 进程操作开始执行
        plist.append(p)
    # .join()必须要和进程创建操作分开
    for pp in plist:
        pp.join()  # 将进程操作设定为关键路径

    result = 0
    for e in range(m):
        result += q.get()  # 从结果队列中取值
    print(result)

# 多线程执行方案
def multithread(m, n):
    q = Queue()
    tlist = []
    signle_size = int(n / m)  # 分配给每个线程的执行规模

    # 把规模n分配给m个线程执行，每个进行执行n/m（即signle_size）
    for e in range(m):
        t = td.Thread(target=job, args=(q, signle_size))
        # 生成进程，并传入要执行的操作（函数），args=参数列表，只传一个参数的时候注意要在参数后面加一个逗号，因为args需要一个可迭代的参量
        t.start()  # 进程操作开始执行
        tlist.append(t)
    # .join()必须要和进程创建操作分开
    for tt in tlist:
        tt.join()  # 将进程操作设定为关键路径

    result = 0
    for e in range(m):
        result += q.get()  # 从结果队列中取值
    print(result)

# 串行执行方案
def normol(m, n):
    q = Queue()
    signle_size = int(n / m)  # 分配给每个进程的执行规模

    # 把规模n分配给m个步骤执行，每个步骤执行n/m（即signle_size）
    for e in range(m):
        job(q, signle_size)

    result = 0
    for e in range(m):
        result += q.get()  # 从结果队列中取值
    print(result)

if __name__ == '__main__':
    n_size = 500000000    # 总规模
    n_mul = 10           # 多线程/进程数，即总规模分配给几个线程/进程执行

    # 多进程执行，计算执行时间
    smp = time.time()
    multicore(n_mul, n_size)
    emp = time.time()
    print('time_multicore:',emp-smp)

    # 多线程执行，计算执行时间
    smt = time.time()
    multithread(n_mul, n_size)
    emt = time.time()
    print('time_multithread:',emt-smt)

    # 串行分步执行，计算执行时间
    ss = time.time()
    normol(n_mul, n_size)
    es = time.time()
    print('time_normal:',es-ss)

