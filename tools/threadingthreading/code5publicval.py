import threading

# 猜测
# 对象是引用，如果一个对象被传入多个线程的job，被多个线程操作，改变是不是在多个线程间同步的：请给出答案
# 然后，这应该是加锁的

class TokenBucket():
    def __init__(self, qps):
        self.qps = qps
        self.n_token = 0
        self.add_gap = 1/qps
        self.update_time = 0

    def update(self):
        pass


# 多线程实际上并不是真正意义上的
def job1():
    global A
    for i in range(1000000):
        A+=1
        # print('job1', A)  # 当这个print在这里时，大概是因为站住了时间？两个线程能对A+2000000，
    # 当把这个print移到这里，任cpu施为的时候，两个线程对A的操作就会发生神奇的事
    print('job1', A)


def job2():
    global A
    for i in range(1000000):
        A+=1
    print('job2', A)

if __name__ == '__main__':
    A = 0
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('reault {}'.format(A))

# import threading
# def job1():
#     global A, lock
#     lock.acquire()
#     for i in range(10):
#         A+=1
#         print('job1', A)
#     lock.release()
#
#
# def job2():
#     global A, lock
#     lock.acquire()
#     for i in range(10):
#         A+=10
#         print('job2', A)
#     lock.release()
#
# if __name__ == '__main__':
#     lock = threading.Lock()
#     A = 0
#     t1 = threading.Thread(target=job1)
#     t2 = threading.Thread(target=job2)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()