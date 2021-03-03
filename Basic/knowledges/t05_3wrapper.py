# 带参数的装饰器——在装饰器外层再套一个
# 如果装饰了很多函数，后期可能要取消装饰，设置一个全局参数来控制是否进行装饰，就要对装饰器传参
# 而装饰器已经传了参数func（即函数名），为了再传入参数，在装饰器外层再封装一个函数
import time
FLAGE = True    # 只需通过设置这个超参数，即可控制所有被装饰器修饰的函数是否执行装饰器

def timmer_out(flag):
    def timmer(func):
        def inner(*args,**kwargs):
            if flag:
                start = time.time()
                ret = func(*args,**kwargs)
                end = time.time()
                print(end-start)
                return ret
            else:
                ret = func(*args, **kwargs)
                return ret
        return inner
    return timmer

# 装饰器实现写法1
# timmer = timmer_out(FLAGE)
# @timmer
# 装饰器实现写法2
@timmer_out(FLAGE)    #wahaha = timmer(wahaha)
def wahaha():
    time.sleep(0.1)
    print('wahahahahahaha')

@timmer_out(FLAGE)
def erguotou():
    time.sleep(0.1)
    print('erguotoutoutou')

wahaha()
erguotou()
# wahahahahahaha
# 0.10030055046081543
# erguotoutoutou
# 0.10075545310974121
