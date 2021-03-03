# dir()方法
# dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；
# 带参数时，返回参数的属性、方法列表。如果参数包含方法__dir__()，该方法将被调用。
# 如果参数不包含__dir__()，该方法将最大限度地收集参数信息。

print(dir(list))
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
print('__iter__' in dir(list))
# True

# 使用
l = [1,2,3]
iterator = l.__iter__()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
# 1
# 2
# 3
# print(iterator.__next__())  # 上面已经迭代到最后一个元素了，再__next__()就会报错

# 可迭代 与 迭代器
# Iterable  可迭代的    -- > 有__iter__  # 只要含有__iter__方法的都是可迭代的
# [].__iter__() 迭代器  -- > 有__next__  # 通过next就可以从迭代器中一个一个的取值
print('__iter__' in dir([1,2,3]))
print('__next__' in dir([1,2,3].__iter__()))
# True
# True

# 只要含有__iter__方法的都是可迭代的 —— 可迭代协议
# 迭代器协议 —— 内部含有__next__和__iter__方法的就是迭代器

# 只有可迭代的才可以进行for循环，在进行for循环的时候，会去检查对象有没有__iter__，没有会报不可迭代对象，有才执行

from collections import Iterable    # Iterable 可迭代的
from collections import Iterator    # Iterator 迭代器
print(isinstance([],Iterator))      # isinstance(obj1,obj2) # 判断obj1是不是obj2，这里判断[]是否是迭代器
# False 因为是空的，不能再迭代了
print(isinstance([],Iterable))      # 判断[]是否是可迭代的
# True

# 假设自己创建了一个数据类型
class A:
    def __iter__(self):pass     # 如果注释了，就是不可迭代的
    def __next__(self):pass     # 如果注释了

a = A()
print(isinstance(a,Iterator)) # 当a中有__inter__和__next__方法，a是迭代器
# True
print(isinstance(a,Iterable))
# True

################## 迭代器的优势
# rang(int)是一个迭代器
print(range(1000000000000000000))
# range(0, 1000000000000000000)
print(list(range(10000)))
# 尝试了10的9次方，卡爆了我的内存，不得不强行关机。。。