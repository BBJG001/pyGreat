# 装饰器形成的过程 : 最简单的装饰器 有返回值的 有一个参数 万能参数
# 装饰器的作用
# 原则 ：依赖倒置原则
#        开放封闭原则
#
# 语法糖 ：@
# 装饰器的固定模式

import time

def timmer1(f):  # 装饰器函数
    def inner():
        start = time.time()     # time.time()获得当前时间
        ret = f()  # 执行被装饰的函数
        end = time.time()
        print(end - start)
        return ret
    return inner    # 闭包的写法

# 不用语法糖修饰的方式
# @timmer         # 语法糖 @装饰器函数名
def func1():  # 被装饰的函数
    time.sleep(0.01)    # 暂停0.01s
    print('被装饰的函数执行体')
    return '返回值'
func1 = timmer1(func1)    # 不用语法糖修饰的方式，手动实现装饰

ret1 = func1()
# 被装饰的函数执行体
# 0.011034488677978516
print(ret1)
# 返回值

# 用语法糖修饰——在函数声明前添加 @装饰器函数名 的标记
@timmer1  # 语法糖 @装饰器函数名
def func2():  # 被装饰的函数
    time.sleep(0.01)
    print('被装饰函数执行体')
    return '返回值'

# func = timmer(func)
ret2 = func2()  # 使用语法糖的形式，直接通过函数名调用即可
# 被装饰函数执行体
# 0.010964632034301758
print(ret2)
# 返回值

# 装饰器的作用 —— 不想修改函数的调用方式 但是还想在原来的函数前后添加功能
# timmer就是一个装饰器函数，只是对一个函数 有一些装饰作用

########################## 装饰带参数函数的装饰器
def timmer2(f):  # 装饰器函数
    def inner(*args, **kwargs):
        # (1,2) /(1)
        start = time.time()
        ret = f(*args, **kwargs)  # 传入动态参数，该装饰器就能兼容不同参数的函数
        end = time.time()
        print(end - start)
        return ret
    return inner

@timmer2  # 语法糖 @装饰器函数名
def func1(a, b):  # 被装饰的函数
    time.sleep(0.01)
    print('a & b', a, b)
    return a + b
ret1 = func1(1, b=2)  # inner()
# a & b 1 2
# 0.010001659393310547
print('ret1:', ret1)
# ret1: 3

def func2(a):  # 被装饰的函数
    time.sleep(0.01)
    print('this is', a)
    return a * a
func2 = timmer2(func2)  # 不使用语法糖的方式时，就需要手动把函数封装进装饰器函数

ret2 = func2(3)  # inner()
# this is 3
# 0.010001659393310547
print('ret2:', ret2)
# ret2: 9

######################### 小结
def wrapper(f):    #装饰器函数，f是被装饰的函数
    def inner(*args,**kwargs):
        '''在被装饰函数之前要做的事'''
        ret = f(*args,**kwargs)    #被装饰的函数
        '''在被装饰函数之后要做的事'''
        return ret
    return inner

@wrapper         #语法糖 @装饰器函数名
def func(a,b):     #被装饰的函数
    time.sleep(0.01)
    print('被装饰的函数执行动作',a,b)
    return '返回值'

# 直接调用有语法糖装饰的函数，就是在执行被装饰的函数了
func(3,5)
