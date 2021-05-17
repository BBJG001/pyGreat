# #!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/8 4:12 下午
# @Author  : 百变金刚
# @Content :
#! /usr/bin/env python
# -*- coding: utf-8 -*-

from concurrent.futures import ThreadPoolExecutor
import time

def sayhello(a):
    print("hello: {}".format(a))
    time.sleep(1)

def getCode():
    seed = ["a", "b", "c", 1, 2, 3]
    for si in seed:
        yield si


def single(seed):
    start1 = time.time()
    print('-------------单线程')
    for each in seed:
        sayhello(each)
    end1 = time.time()
    print("time1: " + str(end1 - start1))

def multiBySubmit(seed):
    start2 = time.time()
    print('------------多线程submit')
    with ThreadPoolExecutor(3) as executor:
        for each in seed:
            executor.submit(sayhello, each)  # submit会在报错后继续执行；需要每次传一个参数
    end2 = time.time()
    print("time2: " + str(end2 - start2))

def multiByMap(seed):
    start3 = time.time()
    print('------------多线程map')
    with ThreadPoolExecutor(3) as executor1:
        executor1.map(sayhello, seed)  # map保证顺序，不兼容报错
    end3 = time.time()
    print("time3: " + str(end3 - start3))

def multiGenertor(seed):
    start22 = time.time()
    print('------------多线程submit，生成器改造')
    code_builder = getCode()
    with ThreadPoolExecutor(3) as executor:
        # while True:
        #     code = next(code_builder)
        #     if not code:
        #         break
        print(code_builder)
        for code in code_builder:   # 生成器可以直接用for循环的话，还是很方便的
            executor.submit(sayhello, code)  # submit会在报错后继续执行；需要每次传一个参数
    end22 = time.time()
    print("time2: " + str(end22 - start22))

def testThreadPoolExecutor():
    with ThreadPoolExecutor(5) as pool:
        for i in range(23):
            pool.submit(sayhello, i)
    print('over')

def main():
    seed=["a","b","c",1,2,3]    # 任务资源池?

    # single(seed)
    multiBySubmit(seed)
    multiGenertor(seed)
    # multiByMap(seed)






if __name__ == '__main__':
    testThreadPoolExecutor()
    # main()