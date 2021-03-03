#函数的嵌套定义
#内部函数可以使用外部函数的变量
a = 1
def outer():
    a = 1
    def inner():
        a = 2
        def inner2():
            nonlocal a  #声明了一个上面第一层局部变量
            a += 1   #不可变数据类型的修改
        inner2()
        print('￥￥a￥￥ : ', a)
    inner()
    print('**a** : ',a)
outer()
print('全局 ：',a)
# ￥￥a￥￥ :  3
# **a** :  1
# 全局 ： 1

# b=2
# def funout1():
#     nonlocal b    # 这样是不行滴，nonlocal这种操作只对最近的局部变量起作用
#     b=b+1
# funout1()
# print('b=', b)

c=33
def funout2():
    c=3
    def inner2():
        nonlocal c
        c=c+1
    inner2()
    print('(inner2)c=', c)
funout2()
print('(全局）c=', c)
# (inner2)c= 4
# (全局）c= 33

# nonlocal 只能用于局部变量 找上层中离当前函数最近一层的局部变量
# 声明了nonlocal的内部函数的变量修改会影响到 离当前函数最近一层的局部变量
# 对全局无效
# 对局部 也只是对 最近的 一层 有影响