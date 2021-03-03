#闭包：嵌套函数，内部函数调用外部函数的变量
def outer():
    a = 1
    def inner():
        print(a)
    inner()
outer()
# 1

def outer():
    a = 1
    def inner():
        print(a)
    return inner	# 这就是闭包的写法
getin = outer()     # 因为里面写了return，需要一个变量来获得
outer()
