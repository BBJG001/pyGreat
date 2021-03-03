# 匿名函数，lambda表达式
# python 使用 lambda 来创建匿名函数。
#
# lambda只是一个表达式，函数体比def简单很多。
# lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
# lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
# 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

# lambda [arg1 [,arg2,.....argn]]:expression

def fun(x,y):
    if x<y:
        res = x+y
    else:
        res = x-y
    return res
print(fun(1,3))

fun = lambda x, y: x+y if x<y else x-y
print(fun(1,3))

# map() 会根据提供的函数对指定序列做映射，批量对一个可迭代对象（如列表）中的元素执行某个函数
# 语法    map(function, iterable, ...)
def fun(x):
    return 2 * x
res1 = map(fun, [1, 2, 3])
print(list(res1))  # [2, 4, 6]
res2 = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
print(list(res2))  # [1, 4, 9, 16, 25]
