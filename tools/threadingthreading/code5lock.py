import threading
# 多线程实际上并不是真正意义上的
def job1():
    global A
    for i in range(100):
        A+=1
        print('job1', A)


def job2():
    global A
    for i in range(100):
        A+=10
        print('job2', A)

if __name__ == '__main__':
    A = 0
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

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