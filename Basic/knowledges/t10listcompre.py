#[每一个元素或者是和元素相关的操作 for 元素 in 可迭代数据类型]    #遍历之后挨个处理
#[满足条件的元素相关的操作 for 元素 in 可迭代数据类型 if 元素相关的条件]   #筛选功能

#------------------------ 列表推导式
# 简单的列表推导式
print([2*x for x in range(10)])
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print([3*x**2+5*x+8 for x in range(10)])
# [8, 16, 30, 50, 76, 108, 146, 190, 240, 296]
# 带筛选条件的列表推导式
print([x for x in range(10) if x%2==0])
# [0, 2, 4, 6, 8]

#------------------ 多层for循环的列表推导式
# 找到嵌套列表中名字至少含有两个‘e’的所有名字
names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
         ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
print([name for lst in names for name in lst if name.count('e') >= 2])
# ['Jefferson', 'Wesley', 'Steven', 'Jennifer']
# 注意遍历顺序，真正用到的量是最后一层遍历

# 字典推导式
# 例一：将一个字典的key和value对调
mcase = {'a': 10, 'b': 34}
mcase_frequency = {mcase[k]: k for k in mcase}
print(mcase_frequency)
# {10: 'a', 34: 'b'}

# 例二：合并大小写对应的value值，将k统一成小写
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
#{'a':10+7,'b':34,'z':3}
mcase_frequency = {k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0) for k in mcase}
print(mcase_frequency)
# {'a': 17, 'b': 34, 'z': 3}
# 注：mydict.get(k,0) 代表如果获取不到这个值就返回0（不设置0的话返回None）

# 集合推导式，自带结果去重功能
squared = {x**2 for x in [1, -1, 2]}
print(squared)
# {1, 4}
# 没有元组推导式，因为用括号，推出来就是一个生成器了



