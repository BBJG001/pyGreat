# mp.Pool() 可以获得return的值
import multiprocessing as mp
import time

def job(x):
    time.sleep(1)
    return x*x

def multicore():
    pool = mp.Pool(processes=6)
    # 创建多个进程，进程数有参数porcesses指定
    # 如不指定默认processes是机器的全部核心数（虚拟核）

    # Pool通过 .map() 分配多任务
    st = time.time()
    res = pool.map(job, range(10))  # map(job, job参数列表的列表)会用pool调用多线程来完成所有这些工作
    print(res)
    et = time.time()
    print('time:', et-st)

    # Pool的 .apply_async() 函数
    st = time.time()
    res = pool.apply_async(job, (2,))   # 这种只能传一个值（也就是一个job的参数）
    print(res.get())
    et = time.time()
    print('time:', et - st)

    # Pool通过 .apply_async() 分配多任务
    # 用迭代器实现apply_async()多参数输入
    # 迭代器：每用到结果才会去进行获得该结果的操作，像是一种即用即算，是一种省空间的机制
    st = time.time()
    multi_res = [pool.apply_async(job, (i,)) for i in range(10)]
    print([res.get() for res in multi_res])
    et = time.time()
    print('time:', et - st)

if __name__ == '__main__':
    multicore()