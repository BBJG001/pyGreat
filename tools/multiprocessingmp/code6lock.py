# import multiprocessing as mp
# import time
#
# def job(v, num):
#     for _ in range(5):
#         time.sleep(0.1)     # 为了观察效果明显，做一下延迟
#         v.value += num
#         print(v.value)
#
# def multicore():
#     v = mp.Value('i', 0)
#     p1 = mp.Process(target=job, args=(v, 1))
#     p2 = mp.Process(target=job, args=(v, 10))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()

import multiprocessing as mp
import time

def job(v, num, l):
    l.acquire()       # 锁定开始
    for _ in range(5):
        time.sleep(0.1)
        v.value += num
        print(v.value)
    l.release()       # 锁定结束，锁定开始跟结束之间的部分只允许单进程操作

def multicore():
    l = mp.Lock()
    v = mp.Value('i', 0)
    p1 = mp.Process(target=job, args=(v, 1, l))
    p2 = mp.Process(target=job, args=(v, 10, l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__':
    multicore()