a = '0123456789'
print(a[0:3])  # print(a[:3]) 从开头开始取0可以默认不写
print(a[2:5])
print(a[:])  # 默认到最后
print(a[:-1])  # -1 是列表中最后一个元素的索引，但是要满足顾头不顾腚的原则，所以取不到K元素
print(a[:5:2])  # 加步长
print(a[-1:-5:-2])  # 反向加步长
# 012
# 234
# 0123456789
# 012345678
# 024
# 97

# 数字符串中的元素出现的个数。
res1 = a.count('3', 0, 4)  # 在a[0:4]中'3'的个数
print(res1)
# 1

# #startswith 判断是否以...开头
# #endswith 判断是否以...结尾
# res2= a.endswith('789',3,)        # 顾头不顾腚
res2 = a.endswith('789', 3, 10)  # 切片是否以'789'结尾
print(res2)  # 返回的是布尔值
res3 = a.startswith("012", 0, 4)  # 切片是否以'012'开头
print(res3)
# True
# True

# #split 以什么分割，最终形成一个列表此列表不含有这个分割的元素。
res4 = 'title,Tilte,atre,'.split('t')
print(res4)
res5 = 'title,Tilte,atre,'.rsplit('t', 1)  # 以从后数第1个't'切分
print(res5)
# ['', 'i', 'le,Til', 'e,a', 're,']
# ['title,Tilte,a', 're,']

# #format的三种玩法 格式化输出
res5 = '{} {} {}'.format('egon', 18, 'male')
res6 = '{1} {0} {1}'.format('egon', 18, 'male')
res7 = '{name} {age} {sex}'.format(sex='male', name='egon', age=18)
# egon 18 male
# 18 egon 18
# egon 18 male

# #strip
name = '*barry**'
print(name.strip('*'))  # 去除其中所有的 *
print(name.lstrip('*'))  # 去除左首所有的 *
print(name.rstrip('*'))  # 去除右尾所有的 *
# barry
# barry**
# *barry


# #replace
name = 'alex say :i have one tesla,my name is alex'
print(name.replace('alex', 'SB', 1))  # 替换
# SB say :i have one tesla,my name is alex

# #is系列
# name='taibai123'
print(name.isalnum())  # 字符串由字母或数字组成
print(name.isalpha())  # 字符串只由字母组成
print(name.isdecimal())  # 字符串只由十进制组成
# False
# False
# False


# #############下面这些方法在数据类型补充时会讲到，现在不讲####################
# #寻找字符串中的元素是否存在
res8 = a.find("123",1,6)
print(res8)  # 返回的找到的元素的索引，如果找不到返回-1
# 1

res9 = a.index("45",4,6)
print(res9) # 返回的找到的元素的索引，找不到报错
# 4


# #captalize,swapcase,title,upper,lower
print(name.capitalize()) #首字母大写
print(name.swapcase()) #大小写翻转
msg='taibai say hi'
print(msg.title()) #每个单词的首字母大写
print(msg.upper())
print(msg.upper().lower())
# Alex say :i have one tesla,my name is alex
# ALEX SAY :I HAVE ONE TESLA,MY NAME IS ALEX
# Taibai Say Hi
# TAIBAI SAY HI
# taibai say hi

# # 内同居中，总长度，空白处填充
ret2 = a.center(20,"*")
print(ret2)
# *****0123456789*****