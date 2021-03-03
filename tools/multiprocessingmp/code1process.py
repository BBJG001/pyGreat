import multiprocessing as mp
import threading as td
import time


def job(ss):
    print('我是', ss)
    print(ss, 'start')
    time.sleep(1)
    print(ss, 'end')


# t1 = td.Thread(target=job, args=(1, 2))
# p1 = mp.Process(target=job, args=(1, 2))

# t1.start()
# p1.start()

# t1.join()
# p1.join()

if __name__ == '__main__':  # mp多进程只能main下执行，
    job('主进程step1############')
    p1 = mp.Process(target=job, args=('新进程>>>>>>>>>>>>>>>>>>>>>>>>>',))    # 创建一个进程
    # 注意当只有一个参数的时候，一定要在参数后面加一个逗号，因为args需要是一个可以迭代的参量
    p1.start()  # 开始执行新进程
    # p1.join() # 让后续操作等待进程p1
    job('主进程step2$$$$$$$$$$$$')