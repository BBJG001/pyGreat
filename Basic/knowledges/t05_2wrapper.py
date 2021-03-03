from functools import wraps

# 在教程那个版本中，当一个函数被装饰装饰了之后，相当于执行了fun = wrapper(fun)，
# fun这个函数名(fun.__name__)就不复存在了，就变成了inner
# 在inner定义之前添加@wraps(func)也是调用了一个别人封装的装饰器，为fun函数赋值他原本的函数名，当然不止改名字，还有其他的作用

def wrapper(func):  #func = holiday
    @wraps(func)  # 调用别人封装的装饰器，归还func的一些属性，通过注释与取消注释会发现func.__name__输出不同的结果
    def inner(*args,**kwargs):
        print('装饰前')
        ret = func(*args,**kwargs)
        print('装饰后')
        return ret
    return inner

@wrapper   #holiday = wrapper(holiday)
def function(num):
    '''function的注释'''
    print('function的执行, 传入的值：%d'%num)
    return 'function的返回值'

print(function.__name__)
print(function.__doc__)  # 函数注释
ret = function(3)   #inner
print(ret)
# function
# function的注释
# 装饰前
# function的执行, 传入的值：3
# 装饰后
# function的返回值

