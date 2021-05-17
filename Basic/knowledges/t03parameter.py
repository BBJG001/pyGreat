def f2(l1):
    f1(l1)
    for i in l1:
        print(i)

def f1(l1):
    for i in l1:
        print(i)

f2([1,2,3,4])

#参数
    #没有参数
        #定义函数和调用函数时括号里都不写内容
    #有一个参数
        #传什么就是什么
    #有多个参数
        #位置参数
# 位置参数
def fun1(name, age):
    print(name, age, '岁了')
fun1('张三', 20)
# 张三 20 岁了

# 关键字参数
def fun2(name, action):
    print(name, action)
fun2(action='吃饭了', name='张三')    # 通过关键字名称指定参数，顺序可以不同
# 张三 吃饭了

# 默认参数
def fun(name, action='真厉害'):
    print(name, action)
fun('张三')
# 张三 真厉害
fun('李四', '一般般')
# 李四 真厉害

# def my_sum(a,b):
#     print(a,b)
#     res = a+b  #result
#     return res
#
# ret = my_sum(1,2)
# print(ret)

#站在实参的角度上：
    #按照位置传参
    #按照关键字传参
    #混着用可以:但是 必须先按照位置传参，再按照关键字传参数
            #  不能给同一个变量传多个值

#站在形参的角度上
    #位置参数：必须传,且有几个参数就传几个值
    #默认参数: 可以不传，如果不传就是用默认的参数，如果传了就用传的
# def classmate(name,sex='男'):
#     print('%s : %s'%(name,sex))
#
# classmate('二哥')
# classmate('小孟')
# classmate('大猛')
# classmate('朗哥','女')

#只有调用函数的时候
    #按照位置传 ： 直接写参数的值
    #按照关键字： 关键字 = 值

#定义函数的时候：
    #位置参数 ： 直接定义参数
    #默认参数，关键字参数 ：参数名 = '默认的值'
    #动态参数 : 可以接受任意多个参数
                #参数名之前加*，习惯参数名args，
                #参数名之前加**，习惯参数名kwargs
    #顺序：位置参数，*args,默认参数,**kwargs

# def classmate(name,sex):
#     print('%s : %s'%(name,sex))
#
# classmate('二哥','男')
# classmate(sex='男',name = '二哥')

# def classmate(name,sex='男'):
#     print('%s : %s'%(name,sex))
#
# classmate('二哥')
# classmate('朗哥',sex= '女')

# 动态参数——位置参数*args
def sum(*args):
    n = 0
    for i in args:
        n+=i
    return n
print(sum(1,2))
# 3
# print(sum(1,2,3))
# print(sum(1,2,3,4))

# 动态参数——关键字字典**kwargs
def func(**kwargs):
    print(kwargs)
func(a = 1,b = 2,c =3)
# {'a': 1, 'b': 2, 'c': 3}
# func(a = 1,b = 2)
# func(a = 1)

# 动态参数有两种：可以接受任意个参数
    #*args   ： 接收的是按照位置传参的值，组织成一个元组
    #**kwargs： 接受的是按照关键字传参的值，组织成一个字典
    #args必须在kwargs之前
# def func(*args,default = 1,**kwargs):
#     print(args,kwargs)
#
# func(1,2,3,4,5,default=2,a = 'aaaa',b = 'bbbb',)

#动态参数的另一种传参方式
#站在实参的角度上，给一个序列加上*，就是将这个序列按照顺序打散
def func(*args):
    print(args)
l = [1,2,3,4,5]
func(*l)

def func(**kwargs):
    print(kwargs)
func(a=1,b=2,c=3)
d = {'a':1,'b':2,'c':3} #定义一个字典d
func(**d)

#函数的注释
# def func():
#     '''
#     这个函数实现了什么功能
#     参数1：
#     参数2：
#     :return: 是字符串或者列表的长度
#     '''
#     pass

    # 默认参数的陷阱
# 文件的修改
# 函数
#1.函数的定义 def
#2.函数的调用
#3.函数的返回值 return
#4.函数的参数
    #形参：
        # 位置参数 ： 必须传
        # *args ：可以接收任意多个位置参数
        # 默认参数 ： 可以不传
        # **kwargs ： 可以接收多个关键字参数
    #实参：按照位置传参，按照关键字传参

#函数
    #内置函数
    #自定义函数 ！！！！！

#################### 注：如果默认参数是可变数据类型——只能用，不要改！因为是共用的，改了会影响其他函数的调用
# 如果默认参数的值是一个可变数据类型，
# 那么每一次调用函数的时候，
# 如果不传值就公用这个数据类型的资源
def qqxing(k,l = {}):
    # l.append(1)
    l[k] = 'v'
    print(l)

qqxing(1)     #[1]
qqxing(2)     #[1,1]
qqxing(3)     #[1,1,1]
# {1: 'v'}
# {1: 'v', 2: 'v'}
# {1: 'v', 2: 'v', 3: 'v'}

def fun(x, y=5):
    y+=1
    print(x+y)

fun(3)
fun(4)
fun(5)
# 9
# 10
# 11