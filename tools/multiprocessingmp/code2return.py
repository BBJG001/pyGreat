import multiprocessing as mp    # 多进程的模块

def job(q):     # 进程调用测程序，传递的参数为一个queue（队列）对象
    res = 0
    for i in range(1000):
        res += i**2
    q.put(res)      # 把结果（就是主进程中函数的返回值）存入队列

if __name__ == '__main__':
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,))
    # 生成进程，并传入要执行的操作（函数），args=参数列表，只传一个参数的时候注意要在参数后面加一个逗号，因为args需要一个可迭代的参量
    p2 = mp.Process(target=job, args=(q,))
    p1.start()      # 进程操作开始执行
    p2.start()
    p1.join()       # 将进程操作设定为关键路径
    p2.join()
    # p1，p2都进行join()操作，p1，p2执行完之后（p1，p2都进行了job并把结果存入了q）才进行下面的操作
    res1 = q.get()      # 从结果队列中取值
    res2 = q.get()
    print(res1+res2)
