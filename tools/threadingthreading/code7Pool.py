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

def main():
    seed=["a","b","c",1,2,3]
    start1=time.time()
    print('-------------单线程')
    for each in seed:
        sayhello(each)
    end1=time.time()
    print("time1: "+str(end1-start1))
    start2=time.time()
    print('------------多线程submit')
    with ThreadPoolExecutor(3) as executor:
        for each in seed:
            executor.submit(sayhello, each) # submit会在报错后继续执行；需要每次传一个参数
    end2=time.time()
    print("time2: "+str(end2-start2))
    start3=time.time()
    print('------------多线程map')
    with ThreadPoolExecutor(3) as executor1:
        executor1.map(sayhello,seed)    # map保证顺序，不兼容报错
    end3=time.time()
    print("time3: "+str(end3-start3))

if __name__ == '__main__':
    main()