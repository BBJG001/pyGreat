# 生成器本质上还是一个迭代器
# 生成器的两种实现方式
# 生成器函数
# 生成器表达式

# 一个普通函数
def generator1():
    print(1)
    return 'a'


ret = generator1()
print(ret)


# 1
# a


# 生成器函数
# yield关键字
# 只要含有yield关键字的函数都是生成器函数
# yield不能和return共用且需要写在函数内
def generator2():
    print(1)
    yield 'a'  # 有yield，这是一个生成器函数


# #生成器函数 ： 执行之后会得到一个生成器作为返回值
ret = generator2()  # 获得一个生成器
print(ret)
# <generator object generator at 0x00000196912B14C8>
print(ret.__next__())  # 通过.__next__才能取值


# 1
# a


def generator3():
    print(1)
    yield 'a'
    print(2)
    yield 'b'
    yield 'c'


g = generator3()
ret = g.__next__()
print(ret)
# 1
# a
ret = g.__next__()
print(ret)
# 2
# b
ret = g.__next__()
print(ret)
# c
# 最后一个yeild返回之后，再__next__()会报错

# 既然能__next__，那肯定也能用for来执行，
# （测试这里的时候把上面的__next__写法注释掉；如果不注释掉，这里是没有结果的，因为上面的生成器已经到头了，没有可返回的了）
for i in g:
    print(i)


###################### 对生成函数返回的每一个值做操作
# 以监听一个文件的输入为例，每次文件有输入，就在控制台打印一下
# 函数返回文件的每一行，有对每一行做个性化操作的需求
# def tail(filename):
#     f = open(filename, encoding='utf-8')
#     while True:
#         line = f.readline()
#         if line.strip():
#             # print(line.strip())   # 在函数内print，如果要对每一个line，就必须要在这里（函数内部）改函数
#             yield line.strip()  # 通过这种写法构造生成器，


# g = tail('file')
# for i in g:  # 这个g是变化的，因为tail中有while True，没生成一个，操作一个
#     if 'python' in i:
#         print('***', i)  # 针对每次新添加（因为是生成器（迭代器）之处输出新行）的做修改，


def generator4():
    print(123)
    content = yield 1   # 这个yield返回之后，执行send操作，赋值给content
    print('=======', content)
    print(456)
    arg = yield '这是实际用到的左右一个yield了'
    print('这里是最后一个yield之后的一些操作')
    # 最后一个yield之后不应再有操作，否则报错
    # 可以把最后一个yield写成上面的形式（用一个变量来接收是为了支持send），最后再加一个yield空值
    yield

g = generator4()
ret = g.__next__()
print('***', ret)
ret = g.send('hello')  # send的效果和next一样，都会返回yield的值
print('***', ret)
# 123
# *** 1
# ======= hello
# 456
# *** 2

# send 获取下一个值的效果和next基本一致
# 只是在获取下一个值的时候，给上一yield的位置传递一个数据（所以在send之前，上面一定要有一个yield）
# 第一个yield不能做接受send处理
# 使用send的注意事项
# 第一次使用生成器的时候 是用next获取下一个值
# 最后一个yield不能接受外部的值

# 获取移动平均值
# 10 20 30 10
# 10 15 20 17.5
# avg = sum/count
def average():
    sum = 0
    count = 0
    avg = 0
    while True:
        num = yield avg     # 放在这里是最优写法
        sum += num    # 10
        count += 1    # 1
        avg = sum/count

avg_g = average()
avg_g.__next__()    # 注意这里，在执行之前必须__next__一下，跳过从未传值的过程
print(avg_g)    # <generator object average at 0x0000022997BFCEC8>
avg10 = avg_g.send(10)
print(avg10)    # 10.0
avg20 = avg_g.send(20)
print(avg20)    # 20.0

# 预激生成器的装饰器（承接上一个函数，就是用装饰器做了__next__的操作，下面用的时候可以直接send）
def init(func):   #装饰器
    def inner(*args,**kwargs):
        g = func(*args,**kwargs)    #g = average()
        g.__next__()
        return g
    return inner

@init
def average2():
    sum = 0
    count = 0
    avg = 0
    while True:
        num = yield avg
        sum += num    # 10
        count += 1    # 1
        avg = sum/count

avg_g = average2()   #===> inner
ret10 = avg_g.send(10)
print(ret10)    # 10.0
ret20 = avg_g.send(20)
print(ret20)    # 15.0

# python 3的新点——yield from
# 普通写法
def generator5():
    a = 'abcde'
    b = '12345'
    for i in a:
        yield i
    for i in b:
        yield i
# yield from写法
def generator6():
    a = 'abcde'
    b = '12345'
    yield from a
    yield from b

g5 = generator5()
for i in g5:
    print(i, end=' ')
print()
# a b c d e 1 2 3 4 5

g6 = generator6()
for i in g6:
    print(i, end=' ')
print()
# a b c d e 1 2 3 4 5

# send
# send的作用范围和next一模一样
# 第一次不能用send
# 函数中的最后一个yield不能接受新的值

# 计算移动平均值的例子
# 预激生成器的装饰器的例子
# yield from

