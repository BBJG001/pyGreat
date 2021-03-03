# coding=utf8
# 按照可变与不可变的数据类型的分类：
#
#     不可变（可哈希）的数据类型：int，str，bool，tuple。
#
#     可变（不可哈希）的数据类型：list，dict，set。
#
# 字典是Python语言中的映射类型，他是以{}括起来，里面的内容是以键值对的形式储存的：
#
#     Key: 不可变（可哈希）的数据类型.并且键是唯一的，不重复的。
#
#     Value:任意数据(int，str，bool，tuple，list，dict，set)，包括后面要学的实例对象等。
#
# 　在Python3.5版本（包括此版本）之前，字典是无序的。
#
# 　在Python3.6版本之后，字典会按照初建字典时的顺序排列(即第一次插入数据的顺序排序)。
#
# 　当然，字典也有缺点：他的缺点就是内存消耗巨大。
#
# 字典的查询速度非常快（能直接哈希到目标地址（空间换时间）），简单解释一下原因：字典的键值对会存在一个散列表（稀疏数组）这样的空间中，每一个单位称作一个表元，表元里面记录着key：value,如果你想要找到这个key对应的值，先要对这个key进行hash获取一串数字咱们简称为门牌号（非内存地址），然后通过门牌号，确定表元，对比查询的key与被锁定的key是否相同，如果相同，将值返回，如果不同，报错。（这里只是简单的说一下过程，其实还是比较复杂的。），下面我已图形举例：
import string

######################## 创建字典的几种方式：

# 方式1:
dic = dict((('one', 1),('two', 2),('three', 3)))
# dic = dict([('one', 1),('two', 2),('three', 3)])
print(dic)  # {'one': 1, 'two': 2, 'three': 3}


# 方式2:
dic = dict(one=1,two=2,three=3)
print(dic)  # {'one': 1, 'two': 2, 'three': 3}


# 方式3:
dic = dict({'one': 1, 'two': 2, 'three': 3})
print(dic)  # {'one': 1, 'two': 2, 'three': 3}

# 方式5: 后面会讲到先了解
dic = dict(zip(['one', 'two', 'three'],[1, 2, 3]))
print(dic)
# {'one': 1, 'two': 2, 'three': 3}

# 方式6: 字典推导式 后面会讲到
# dic = { k: v for k,v in [('one', 1),('two', 2),('three', 3)]}
print(dic)
# {'one': 1, 'two': 2, 'three': 3}

# 方式7:利用fromkey后面会讲到。
# dic = dict.fromkeys('abcd','太白')
print(dic)  # {'a': '太白', 'b': '太白', 'c': '太白', 'd': '太白'}

############################ # 判断字典是否合法
dic = {123: 456, True: 999, "id": 1, "name": 'sylar', "age": 18, "stu": ['帅哥', '美⼥'], (1, 2, 3): '麻花藤'}
print(dic[123])
print(dic[True])
print(dic['id'])
print(dic['stu'])
print(dic[(1, 2, 3)])

# 不合法
# dic = {[1, 2, 3]: '周杰伦'} # list是可变的. 不能作为key
# dic = {{1: 2}: "哈哈哈"} # dict是可变的. 不能作为key
# dic = {{1, 2, 3}: '呵呵呵'} # set是可变的, 不能作为key

######################## 增
# 通过键值对直接增加
dic = {'name': '太白', 'age': 18}
dic['weight'] = 75 # 没有weight这个键，就增加键值对
print(dic) # {'name': '太白', 'age': 18, 'weight': 75}
dic['name'] = 'barry' # 有name这个键，就成了字典的改值
print(dic) # {'name': 'barry', 'age': 18, 'weight': 75}

# setdefault
dic = {'name': '太白', 'age': 18}
dic.setdefault('height',175) # 没有height此键，则添加
print(dic) # {'name': '太白', 'age': 18, 'height': 175}
dic.setdefault('name','barry') # 有此键则不变，不添加，不改变原值
print(dic) # {'name': '太白', 'age': 18, 'height': 175}
#它有返回值
dic = {'name': '太白', 'age': 18}
ret = dic.setdefault('name')
print(ret)  # 太白

################## 删
# pop 通过key删除字典的键值对，有返回值，可设置返回值。
dic = {'name': '太白', 'age': 18}
# ret = dic.pop('name')     # 有则删除，并返回删除元素
# print(ret,dic) # 太白 {'age': 18}
ret1 = dic.pop('n',None)    # 无则返回none
print(ret1,dic) # None {'name': '太白', 'age': 18}

#popitem 3.5版本之前，popitem为随机删除，3.6之后为删除最后一个，有返回值
dic = {'name': '太白', 'age': 18}
ret = dic.popitem()
print(ret,dic) # ('age', 18) {'name': '太白'}

#clear 清空字典
dic = {'name': '太白', 'age': 18}
dic.clear()
print(dic) # {}

# del
# 通过键删除键值对
dic = {'name': '太白', 'age': 18}
del dic['name']
print(dic) # {'age': 18}
#删除整个字典
del dic

######################## 改
# 通过键值对直接改
dic = {'name': '太白', 'age': 18}
dic['name'] = 'barry'
print(dic) # {'name': 'barry', 'age': 18}

# update
dic = {'name': '太白', 'age': 18}
dic.update(name='男', height=175)    # 有则改掉，无则添加
print(dic) # {'name': '男', 'age': 18, 'height': 175}

dic = {'name': '太白', 'age': 18}
dic.update([(1, 'a'),(2, 'b'),(3, 'c'),(4, 'd')])
print(dic) # {'name': '太白', 'age': 18, 1: 'a', 2: 'b', 3: 'c', 4: 'd'}

dic1 = {"name":"jin","age":18,"sex":"male"}
dic2 = {"name":"alex","weight":75}
dic1.update(dic2)   # 为dic1拼接上dic2，更新dic1，无返回值
print(dic1) # {'name': 'alex', 'age': 18, 'sex': 'male', 'weight': 75}
print(dic2) # {'name': 'alex', 'weight': 75}

dic1 = {"name":"jin","age":18,"sex":"male"}
dic2 = {"name":"alex","weight":75}
dic = {**dic1, **dic2}  # 去重拼接
print(dic)
# {'name': 'alex', 'age': 18, 'sex': 'male', 'weight': 75}

###################### 查
# 通过键查询
# 直接dic[key](没有此键会报错)
dic = {'name': '太白', 'age': 18}
print(dic['name']) # 太白

# get
dic = {'name': '太白', 'age': 18}
v = dic.get('name')
print(v) # '太白'
v = dic.get('name1')
print(v) # None
v = dic.get('name2','没有此键')     # 设置（无此键的）默认返回值
print(v) # 没有此键


# keys()
dic = {'name': '太白', 'age': 18}
print(dic.keys()) # dict_keys(['name', 'age'])

# values()
dic = {'name': '太白', 'age': 18}
print(dic.values()) # dict_values(['太白', 18])

# items()
dic = {'name': '太白', 'age': 18}
print(dic.items()) # dict_items([('name', '太白'), ('age', 18)])

# fromkeys
dic = dict.fromkeys('abcd','太白')
print(dic) # {'a': '太白', 'b': '太白', 'c': '太白', 'd': '太白'}

dic = dict.fromkeys([1, 2, 3],'太白')
print(dic) # {1: '太白', 2: '太白', 3: '太白'}

# 根据值删选键值对
dic = dict(zip(string.ascii_lowercase, range(1, 27)))
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, ... , 'x': 24, 'y': 25, 'z': 26}
maxkey = max(dic, key=dic.get)
print(maxkey)
minkey = min(dic, key=dic.get)
print(minkey)
res = {item for item in dic.items() if item[1]>22}
print(res)  # {('w', 23), ('z', 26), ('y', 25), ('x', 24)}

############################ 其他操作
dic = dict(zip(string.ascii_lowercase[:5], range(1, 6)))
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# dic.items()
print(dic.items())  # 键 值 形成的元组组成的（伪）列表，可以for循环获取
# dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])
print(list(dic.items()))    # 转成（真）列表（list）
# [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
# items+for循环
for item in dic.items():
    print(item, end=' ')
# ('a', 1) ('b', 2) ('c', 3) ('d', 4) ('e', 5)
for k, v in dic.items():    # 用到了元素的分别赋值（元组的拆包）
    print(k, ':', v, end=' | ')
# a : 1 | b : 2 | c : 3 | d : 4 | e : 5 |

# dic.keys()
print(dic.keys())   # 所有key的（伪）列表，可以for循环
# dict_keys(['a', 'b', 'c', 'd', 'e'])
print(list(dic.keys())) # 转成list
# ['a', 'b', 'c', 'd', 'e']

print(dic.values())     # 所有value的（伪）列表，可以for循环
# dict_values([1, 2, 3, 4, 5])
print(list(dic.values()))   # 转成list
# [1, 2, 3, 4, 5]

# 字典的嵌套
dic = {
    'name':'汪峰',
    'age':48,
    'wife':[{'name':'国际章','age':38}],
    'children':{'girl_first':'小苹果','girl_second':'小怡','girl_three':'顶顶'}
}
print(dic['name'])
# 汪峰
print(dic['children'])  # 这个key对应的value是一个字典
# {'girl_first': '小苹果', 'girl_second': '小怡', 'girl_three': '顶顶'}
print(dic['children']['girl_three'])    # 既然dic['children']是一个字典，那么在字典中取值，在后面跟索引就行了xx['girl_three']
# 顶顶
print(dic['wife'])  # 注意获得的是一个list
# [{'name': '国际章', 'age': 38}]
print(dic['wife'][0])   # 先从list中取值，利用序号索引，获得内层的字典
# {'name': '国际章', 'age': 38}
print(dic['wife'][0]['age'])    # 对字典取值，利用key索引
# 38