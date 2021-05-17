# thread.join(), join()这一行之前的命令不会等thread，会直接执行；join()这一行之后的命令会等thread执行结束之后再执行
# join()会等待所有join的线程执行结束之后再执行后续的程序
import threading
import time

def thread_job():
    print('T1 start\n')
    for i in range(10):
        time.sleep(0.1)
    print('T1 finished')
    # print('This is an added Thread, number is %s'%threading.current_thread())

def T2_job():
    print('T2 start\n')
    time.sleep(2)
    print('T2 finished\n')

def noJoin():
    start = time.time()
    add_thread = threading.Thread(target=thread_job, name='T1')
    thread2 = threading.Thread(target=T2_job, name='T2')
    add_thread.start()
    thread2.start()
    end = time.time()
    print('no join total time {}'.format(end-start))

def withJoin():
    # print(threading.active_count())     # 正在运行的线程数量
    # print(threading.enumerate())        # 列举线程
    # print(threading.current_thread())   # 当前线程

    # added_thread = threading.Thread(target=thread_job())  # 添加线程，这个线程用来do thread_job
    # added_thread.start()    # 这里才算开始，上面相当于一个声明

    start = time.time()
    add_thread = threading.Thread(target=thread_job, name='T1')
    thread2 = threading.Thread(target=T2_job, name='T2')
    add_thread.start()
    thread2.start()
    print('<<<<<<<<<<<<<<<<<test point1>>>>>>>>>>>>>>>>>>>>')
    # thread2.join()      # join()的顺序不会影响程序的实际执行
    print('<<<<<<<<<<<<<<<<<test point2>>>>>>>>>>>>>>>>>>>>')
    add_thread.join()  # join()之后，后续命令要等到add_thread完成之后才运行
    print('<<<<<<<<<<<<<<<<<test point3>>>>>>>>>>>>>>>>>>>>')
    thread2.join()  # join()的顺序不会影响程序的实际执行
    print('all done\n')
    end = time.time()
    print('with join total time {}'.format(end-start))
    print('不同线程之间是并行的，主线程是被阻塞的')


if __name__ == '__main__':
    noJoin()
    withJoin()