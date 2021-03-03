# 黄色一带而过：all()  any()  bytes() callable() chr() complex() divmod() eval() exec() format() frozenset() globals() hash() help() id() input() int()  iter() locals() next()  oct()  ord()  pow()    repr()  round()
#
# 红色重点讲解：abs() enumerate() filter()  map() max()  min() open()  range() print()  len()  list()  dict() str()  float() reversed()  set()  sorted()  sum()    tuple()  type()  zip()  dir()
#
# 蓝色未来会讲： classmethod()  delattr() getattr() hasattr()  issubclass()  isinstance()  object() property()  setattr()  staticmethod()  super()

n1 = 88
n2 = -77
l1 = [11, 33, 55, 44, 22]
l2 = [11, 33, 0, 44, 22]
l3 = [0, 0, 0, 0, 0]

# abs   绝对值
print(abs(-77))  # 77

# all   全称命题，全True为True，存在False为False
print(all(l1))  # True
print(all(l2))  # False
print(all(l3))  # False

# any   存在命题，存在True为True，全False为False
print(any(l1))  # True
print(any(l2))  # True
print(any(l3))  # False

# ascii 返回一个对象的字符串形式，如果是非ascii编码表中不存在的字符，用unicode码表示
print(ascii({1: 'a', 2: 'b'}))  # {1: 'a', 2: 'b'}

# bin   返回一个整数 int 或者长整数 long int 的二进制表示
print(bin(256))  # 0b100000000

# bool  函数用于将给定参数转换为布尔类型，如果没有参数，返回 False
print(bool(0))
# 0、空列表、空字典等bool()之后为False

# bytearray() 方法返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256
# 如果 source 为整数，则返回一个长度为 source 的初始化数组；
# 如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列；
# 如果 source 为可迭代类型，则元素必须为[0 ,255] 中的整数；
# 如果 source 为与 buffer 接口一致的对象，则此对象也可以被用于初始化 bytearray。
# 如果没有输入任何参数，默认就是初始化数组为0个元素。
print(bytearray())  # bytearray(b'')
print(bytearray([1, 2, 3]))  # bytearray(b'\x01\x02\x03')
print(bytearray('汉字aa3', 'utf-8'))  # bytearray(b'\xe6\xb1\x89\xe5\xad\x97aa3')

# bytes 函数返回一个新的 bytes 对象，该对象是一个 0 <= x < 256 区间内的整数不可变序列。它是 bytearray 的不可变版本
# 如果 source 为整数，则返回一个长度为 source 的初始化数组；
# 如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列；
# 如果 source 为可迭代类型，则元素必须为[0 ,255] 中的整数；
# 如果 source 为与 buffer 接口一致的对象，则此对象也可以被用于初始化 bytearray。
# 如果没有输入任何参数，默认就是初始化数组为0个元素。
print(bytes())  # b''
print(bytes([1, 2, 3]))  # b'\x01\x02\x03'
print(bytes('汉字aa3', 'utf-8'))  # b'\xe6\xb1\x89\xe5\xad\x97aa3'

# callable() 函数用于检查一个对象是否是可调用的。如果返回 True，object 仍然可能调用失败；但如果返回 False，调用对象 object 绝对不会成功
# callable(obj)返回为True的obj都在内部实现了__call__()方法
print(callable(0))  # False
print(callable('asd123'))  # False

def add(a, b):
    return a + b
print(callable(add))  # True

class A:  # 类
    def method(self):
        return 0
print(callable(A))  # True
a = A()
print(callable(a))  # False

# chr() 用一个整数作参数，返回一个对应的字符
print(chr(0b11))  # ' '
print(chr(0xf8))  # ø
print(chr(34163))  # 蕳


# classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，
# 但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等
class A(object):
    bar = 1

    def func1(self):
        print('foo')

    @classmethod
    def func2(cls):
        print('func2')
        print(cls.bar)
        cls().func1()  # 调用 foo 方法


A.func2()  # 不需要实例化
# func2
# 1
# foo

# compile() 函数将一个字符串编译为字节代码
# 语法    compile(source, filename, mode[, flags[, dont_inherit]])
# source -- 字符串或者AST（Abstract Syntax Trees）对象。。
# filename -- 代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。
# mode -- 指定编译代码的种类。可以指定为 exec, eval, single。
# flags -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。。
# flags和dont_inherit是用来控制编译源码时的标志
string = "print('result:', 3 * 4 + 5)"
a = compile(string, '', 'eval')
eval(a)
# result: 17

# complex() 函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数
# 语法    class complex([real[, imag]])
# real -- int, long, float或字符串；
# imag -- int, long, float；
print(complex(1, 2))
# (1+2j)

# delattr 函数用于删除属性。
# 语法    delattr(object, name)
# object -- 对象。
# name -- 必须是对象的属性
class Coordinate:
    x = 10
    y = -5

point1 = Coordinate()
print('x = ', point1.x)
print('y = ', point1.y)

delattr(Coordinate, 'y')

print('--删除 y 属性后--')
print('x = ', point1.x)
# 再使用y属性报错
# print('y = ', point1.y) # 'Coordinate' object has no attribute 'y'

# dict() 函数用于创建一个字典
print(dict())  # 创建空字典
# {}
print(dict(a='a', b='b', t='t'))  # 传入关键字
# {'a': 'a', 'b': 'b', 't': 't'}
print(dict(zip(['one', 'two', 'three'], [1, 2, 3])))  # 映射函数方式来构造字典
# {'one': 1, 'two': 2, 'three': 3}
print(dict([('one', 1), ('two', 2), ('three', 3)]))  # 可迭代对象方式来构造字典
# {'one': 1, 'two': 2, 'three': 3}

# dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。
# 如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息
print(dir())  # 获得当前模块的属性列表
# ['A', 'Coordinate', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'add', 'l1', 'l2', 'l3', 'n1', 'n2', 'point1', 'string']
print(dir([]))  # 查看列表的方法
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# Python divmod(a, b) 函数接收两个数字类型（非复数）参数，返回一个包含商和余数的元组(a // b, a % b)
print(divmod(7, 2))  # (3, 1)
print(divmod(8, 2))  # (4, 0)

# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
# 同时列出数据和数据下标，一般用在 for 循环当中
# 语法
# sequence -- 一个序列、迭代器或其他支持迭代对象。
# start -- 下标起始位置，默认为0
testlist = ['a', 'b', 'c', 'd']
print(enumerate(testlist))  # <enumerate object at 0x000002454A057958>
print(list(enumerate(testlist)))  # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
print(list(enumerate(testlist, start=100)))  # [(100, 'a'), (101, 'b'), (102, 'c'), (103, 'd')]
for i, element in enumerate(testlist):
    print(i, element)
# 0 a
# 1 b
# 2 c
# 3 d

# eval() 函数用来执行一个字符串表达式，并返回表达式的值
# eval(expression[, globals[, locals]])
# expression -- 表达式
# globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象
# locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象
x = 7
print(eval('x+7'))  # 14
print(eval('pow(2, 8)'))  # 256

# exec 执行储存在字符串或文件中的 Python 语句，相比于 eval，exec可以执行更复杂的 Python 代码
# 语法    exec(object[, globals[, locals]])
# object：必选参数，表示需要被指定的Python代码。它必须是字符串或code对象。如果object是一个字符串，该字符串会先被解析为一组Python语句，然后在执行（除非发生语法错误）。如果object是一个code对象，那么它只是被简单的执行。
# globals：可选参数，表示全局命名空间（存放全局变量），如果被提供，则必须是一个字典对象。
# locals：可选参数，表示当前局部命名空间（存放局部变量），如果被提供，可以是任何映射对象。如果该参数被忽略，那么它将会取与globals相同的值。
# 单行语句字符串
exec('print("Hello World")')  # Hello World
exec("print ('runoob.com')")  # runoob.com
#  多行语句字符串
exec("""for i in range(3):
     print ("testnum: %d" % i)
""")
# testnum: 0
# testnum: 1
# testnum: 2

# filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，
# 然后返回 True 或 False，最后将返回 True 的元素放到新列表中
# 语法    filter(function, iterable)
# function -- 判断函数。
# iterable -- 可迭代对象
def is_odd(n):
    return n % 2 == 1


print(filter(is_odd, [1, 2, 3, 4, 5, 6, 7]))  # <filter object at 0x00000172E04A6E48>
print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7])))
# [1, 3, 5, 7]

# float() 函数用于将整数和字符串转换成浮点数
print(float(12))  # 12.0
print(float(12.3613))  # 12.3613

# format 函数可以接受不限个参数，位置可以不按顺序
# 基本语法是通过 {} 和 : 来代替以前的 %
# 不设置指定位置，按默认顺序
print("{} {}".format("hello", "world"))  # hello world
# 设置指定位置
print("{1} {0} {1}".format("hello", "world"))  # world hello world

# frozenset() 返回一个冻结的集合(不可变的集合)，冻结后集合不能再添加或删除任何元素
# 为什么需要冻结的集合（即不可变的集合）呢？因为在集合的关系中，有集合的中的元素是另一个集合的情况，但是普通集合（set）本身是可变的，
# 那么它的实例就不能放在另一个集合中（set中的元素必须是不可变类型）
# 所以，frozenset提供了不可变的集合的功能，当集合不可变时，它就满足了作为集合中的元素的要求，就可以放在另一个集合中了
print(frozenset(range(10)))  # frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
print(frozenset('runoob'))  # frozenset({'u', 'r', 'o', 'b', 'n'})


# getattr() 函数用于返回一个对象属性值
# getattr(object, name[, default])
# object -- 对象
# name -- 字符串，对象属性。
# default -- 默认返回值，如果不提供该参数，在没有对应属性时，将触发 AttributeError
class A(object):
    attr1 = 1
    attr2 = 2


a = A()
print(getattr(a, 'attr1'))  # 1

# globals() 函数会以字典类型返回当前位置的全部全局变量
print(globals())


# {'__name__': '__main__', '__doc__': None, , ,}

# hasattr() 函数用于判断对象是否包含对应的属性
# 语法    hasattr(object, name)
# object -- 对象。
# name -- 字符串，属性名
class Test:
    x = 10
    y = -5


obj = Test()
print(hasattr(obj, 'x'))  # True
print(hasattr(obj, 'y'))  # True
print(hasattr(obj, 'z'))  # False

# hash() 用于获取取一个对象（字符串或者数值等）的哈希值
print(hash('test'))  # 5815421722376877600
print(hash(1))  # 1

# help() 函数用于查看函数或模块用途的详细说明
# print(help('str'))
# print(help('sys'))

# hex() 函数用于将一个指定数字转换为 16 进制数
print(hex(0b0101))  # 0x5
print(hex(128))  # 0x80

# id() 函数返回对象的唯一标识符，标识符是一个整数
xx = 123
yy = '456'
print(id(xx))  # 140703166279888
print(id(yy))  # 2085914260016

#  input() 函数接受一个标准输入数据，返回为 string 类型
# a = input("input:")
## input:5
# print(a)
## 5

# int() 函数用于将一个字符串或数字转换为整型
x8 = int('588')
print(type(x8))  # <class 'int'>
print(x8)  # 588

# isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()
print(isinstance(2, int))  # True
print(isinstance('345', str))  # True
print(isinstance(345, str))  # False
# type 与 isinstance() 的区别是type不会考虑继承关系

# issubclass() 方法用于判断参数 class 是否是类型参数 classinfo 的子类
print(issubclass(int, object))  # True
print(issubclass(int, str))  # False

# iter() 把一个可迭代对象做成一个迭代器
ll = [1, 2, 3]
iterll = iter(ll)
print(type(iterll))  # <class 'list_iterator'>
for i in iterll:
    print(i)
# 1
# 2
# 3

# len() 方法返回对象（字符、列表、元组等）长度或项目个数
print(len([1, 2, 3]))  # 3
print(len('1212'))  # 4

# list() 方法用于将元组或字符串转换为列表
print(list('123'))  # ['1', '2', '3']
print(list((4, 5, 6)))  # [4, 5, 6]


# locals() 函数会以字典类型返回当前位置的全部局部变量
# print(locals())

# map() 会根据提供的函数对指定序列做映射，批量对一个可迭代对象（如列表）中的元素执行某个函数
# 语法    map(function, iterable, ...)
def fun(x):
    return 2 * x
res1 = map(fun, [1, 2, 3])
print(list(res1))  # [2, 4, 6]
res2 = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
print(list(res2))  # [1, 4, 9, 16, 25]

# max() 方法返回给定参数的最大值，参数可以为序列
print(max([33, 99, 55]))  # 99

# memoryview() 函数返回给定参数的内存查看对象(Momory view)
v = memoryview(bytearray("abcefg", 'utf-8'))
print(v[0])  # 97
print(v[-1])  # 103
print(v[1:4])  # <memory at 0x000001EC386C0708>
print(v[1:4].tobytes())  # b'bce'

# min() 方法返回给定参数的最小值，参数可以为序列
print(min([33, 55, 99]))  # 33

# next() 返回迭代器的下一个项目
ll8 = iter([1, 2, 3, 4, 5])
print(next(ll8))  # 1
print(next(ll8))  # 2

# object()

# oct() 函数将一个整数转换成8进制字符串
print(oct(0b0101))  # 0o5
print(oct(0xf8))  # 0o370

# ord() 函数是 chr() 函数（对于 8 位的 ASCII 字符串）的配对函数，
# 它以一个字符串（Unicode 字符）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值
print(ord('s')) # 115
print(ord('字')) # 23383

# open() 函数用于打开一个文件，并返回文件对象，在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError。
# 注意：使用 open() 函数一定要保证关闭文件对象，即调用 close() 函数
# f = open('data.txt')

# pow() 方法返回 x^y（x的y次方） 的值
print(pow(2, 3))  # 8
print(pow(3, 2))  # 9

# print() 方法用于打印输出，最常见的一个函数

# property() 函数的作用是在新式类中返回属性值

# range() 函数返回的是一个可迭代对象（类型是对象），而不是列表类型
res3 = range(2, 5)
print(type(res3))  # <class 'range'>
print(res3)  # range(2, 5)
print(list(res3))  # [2, 3, 4]

# repr() 函数将对象转化为供解释器读取的形式, 返回一个对象的 string 格式
print(repr(3123))           # 3123
print(type(repr(3123)))     # <class 'str'>
print(repr([3, 1, 2, 3]))   # [3, 1, 2, 3]
print(repr({3: 'a', 4: 'b', 5: 'c'}))   # {3: 'a', 4: 'b', 5: 'c'}

# reversed 函数返回一个反转的迭代器
print(list(reversed([3,4,5])))  # [5, 4, 3]

# round() 方法返回浮点数 x 的四舍五入值，准确的说保留值将保留到离上一位更近的一端（四舍六入）
print(round(-3.4))  # -3
print(round(-3.6))  # -4
print(round(3.4))   # 3
print(round(3.6))   # 4

# set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等
print(set('asdfal'))    # {'d', 'a', 'f', 'l', 's'}

# setattr() 函数对应函数 getattr()，用于设置属性值，该属性不一定是存在的
# 语法    setattr(object, name, value)
# object -- 对象。
# name -- 字符串，对象属性。
# value -- 属性值
class A(object):
    bar = 1
obj2 = A()
print(obj2.bar)     # 1
setattr(obj2, 'bar', 5)
print(obj2.bar)     # 5

# slice() 函数实现切片对象，主要用在切片操作函数里的参数传递

# sorted() 函数对所有可迭代的对象进行排序操作
print(sorted([5, 2, 3, 1, 4]))      # [1, 2, 3, 4, 5]
print(sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}))     # [1, 2, 3, 4, 5]
# sort 与 sorted 区别：#
# sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
# list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。

# staticmethod 返回函数的静态方法
class C(object):
    @staticmethod
    def f():
        print('runoob');

C.f()     # 静态方法无需实例化
# runoob
cobj = C()
cobj.f()  # 也可以实例化后调用
# runoob

# str() 函数将对象转化为适于人阅读的形式
print(type(str(11)))    # <class 'str'>
print(str(11))          # 11

# sum() 方法对系列进行求和计算
print(sum([1,2,3,4]))   # 10

# super() 函数是用于调用父类(超类)的一个方法
class A:
    def add(self, x):
        y = x + 1
        print(y)

class B(A):
    def add(self, x):
        super().add(x)

b = B()
b.add(2)  # 3

# tuple 函数将可迭代系列（如列表）转换为元组
print(tuple([1,2,3,4]))
# (1, 2, 3, 4)

# type() 函数如果你只有第一个参数则返回对象的类型，三个参数返回新的类型对象
# isinstance() 与 type() 区别：
# type() 不会认为子类是一种父类类型，不考虑继承关系
# isinstance() 会认为子类是一种父类类型，考虑继承关系
# 如果要判断两个类型是否相同推荐使用 isinstance()
print(type(123))        # <class 'int'>
print(type('123'))      # <class 'str'>

# vars() 函数返回对象object的属性和属性值的字典对象
class Runoob:
   a = 1
print(vars(Runoob))
# {'__module__': '__main__', 'a': 1, '__dict__': <attribute '__dict__' of 'Runoob' objects>, '__weakref__': <attribute '__weakref__' of 'Runoob' objects>, '__doc__': None}

# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
a = [1,2,3]
b = [4,5,6]
print(zip(a,b))         # <zip object at 0x0000019BB654C9C8>
print(list(zip(a,b)))   # [(1, 4), (2, 5), (3, 6)]

# __import__() 函数用于动态加载类和函数
# 如果有一个a.py文件
import a    # 等价于
__import__('a')

# 参考文献
# [Python3 内置函数](https://www.runoob.com/python3/python3-built-in-functions.html)
