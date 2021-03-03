import threading

def thread_job():
    print('This is an added Thread, number is %s'%threading.current_thread())
<<<<<<< HEAD
    print(threading.currentThread().getName())
=======
>>>>>>> dev2

def main():

    # print(threading.active_count())     # 正在运行的线程数量
    # print(threading.enumerate())        # 列举线程
    # print(threading.current_thread())   # 当前线程

    added_thread = threading.Thread(target=thread_job)  # 添加线程，这个线程用来do thread_job
    added_thread.start()    # 这里才算开始，上面相当于一个声明

if __name__ == '__main__':
    main()