# GIL：global interpreter？ lock
# 有些资源是不运行并行的，线程1用资源A的时候，不允许其他进程用A，其他进程就得等着，所以并不能完全提升指定倍数的效率
import threading
from queue import Queue
import copy
import time

def job(q):
    res = sum([1,2,3])
    q.put(res)

def multithreading(l):
    q = Queue()
    threads = []
    for i in range(4):
        t = threading.Thread(target=job, args=(q,)) # 这里的参数必须是可迭代的，只有1个参数的时候需要加 ,
        t.start()
        threads.append(t)
    for tt in threads:
        tt.join()
    total = 0
    for i in range(4):
        total += q.get()
    print(total)



def normal(l):
    total = sum(l)
    print(total)

if __name__ == '__main__':
    l = list(range(1000000))
    s_t = time.time()
    normal(l*4)
    print('normal:', time.time()-s_t)
    s_t = time.time()
    multithreading(l)
    print('multithreading:', time.time()-s_t)