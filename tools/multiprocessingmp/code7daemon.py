# 我想起一个进程在后台执行，不会影响下面的业务
# 这里证明daemon的进程好像并没有按照约定工作
# https://python-parallel-programmning-cookbook.readthedocs.io/zh_CN/latest/chapter3/04_How_to_run_a_process_in_the_background.html
import multiprocessing
import time
import os
import subprocess


def foo():
    name = multiprocessing.current_process().name
    print("Starting %s " % name)
    time.sleep(3)
    with open('{}.txt'.format(name), 'w') as f:
        print(name, file=f)
    print("Exiting %s " % name)

def testByMP():
    background_process = multiprocessing.Process(name='background_process', target=foo)
    background_process.daemon = True
    NO_background_process = multiprocessing.Process(name='NO_background_process', target=foo)
    NO_background_process.daemon = False
    background_process.start()
    NO_background_process.start()


def testBySubP():
    os.chdir(os.path.abspath(os.path.dirname(os.path.abspath(__file__))))
    subprocess.Popen(["python", "script4code7.py"])

if __name__ == '__main__':
    # testByMP()
    testBySubP()