# 一个函数被多个装饰器装饰
def wrapper1(func):
    def inner():
        print('*******************1装饰前')
        func()
        print('*******************1装饰后')
    return inner

def wrapper2(func):
    def inner():
        print('￥￥￥￥2装饰前')
        func()
        print('￥￥￥￥2装饰后')
    return inner

@wrapper1
@wrapper2
def f():
    print('f的执行体')

f()