import pandas as pd
import numpy as np

# 生成测试文件
df1 = pd.DataFrame(np.ones((1,4))*0, columns=['a','b','c','d'])
#      a    b    c    d
# 0  0.0  0.0  0.0  0.0
df2 = pd.DataFrame(np.ones((2,4))*1, columns=['a','b','c','d'])
#      a    b    c    d
# 0  1.0  1.0  1.0  1.0
# 1  1.0  1.0  1.0  1.0
df3 = pd.DataFrame(np.ones((3,4))*2, columns=['a','b','c','d'])
#      a    b    c    d
# 0  2.0  2.0  2.0  2.0
# 1  2.0  2.0  2.0  2.0
# 2  2.0  2.0  2.0  2.0

# concat纵向合并
res1 = pd.concat([df1, df2, df3], axis=0)
# axis在数值方向上合并
#      a    b    c    d
# 0  0.0  0.0  0.0  0.0
# 0  1.0  1.0  1.0  1.0
# 1  1.0  1.0  1.0  1.0
# 0  2.0  2.0  2.0  2.0
# 1  2.0  2.0  2.0  2.0
# 2  2.0  2.0  2.0  2.0

res2 = pd.concat([df1, df2, df3], axis=1) # axis=1在行方向上合并，缺少的数据补nan
#      a    b    c    d    a    b    c    d    a    b    c    d
# 0  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0  2.0  2.0  2.0  2.0
# 1  NaN  NaN  NaN  NaN  1.0  1.0  1.0  1.0  2.0  2.0  2.0  2.0
# 2  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  2.0  2.0  2.0  2.0

#承上一个例子，并将index_ignore设定为True
res3 = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
# ignore_index说的是index不参与合并，合成的res自己生成新的索引
#      a    b    c    d
# 0  0.0  0.0  0.0  0.0
# 1  1.0  1.0  1.0  1.0
# 2  1.0  1.0  1.0  1.0
# 3  2.0  2.0  2.0  2.0
# 4  2.0  2.0  2.0  2.0
# 5  2.0  2.0  2.0  2.0

# 内合并与外合并——join属性
# 生成测试数据
df1 = pd.DataFrame(np.ones((2,4))*0, columns=['a','b','c','d'], index=[1,2])
#      a    b    c    d
# 1  0.0  0.0  0.0  0.0
# 2  0.0  0.0  0.0  0.0
df2 = pd.DataFrame(np.ones((2,4))*1, columns=['b','c','d','e'], index=[3,4])
#      b    c    d    e
# 3  1.0  1.0  1.0  1.0
# 4  1.0  1.0  1.0  1.0
# df1和df2的属性(列)是错开的

# 外合并，join=‘outer’，对几个单体的所有属性进行合并，（缺少的数据补nan）
res1 = pd.concat([df1, df2], axis=0, join='outer', sort=False)  # 这个sort不传会报警告
#      a    b    c    d    e
<<<<<<< HEAD
# 1  0.0  0.0  0.0  0.0  NaN(
=======
# 1  0.0  0.0  0.0  0.0  NaN
>>>>>>> dev2
# 2  0.0  0.0  0.0  0.0  NaN
# 3  NaN  1.0  1.0  1.0  1.0
# 4  NaN  1.0  1.0  1.0  1.0

# 内合并，join='inner'，对几个单体的公共属性进行合并
res2 = pd.concat([df1, df2], axis=0, join='inner')
#      b    c    d
# 1  0.0  0.0  0.0
# 2  0.0  0.0  0.0
# 3  1.0  1.0  1.0
# 4  1.0  1.0  1.0

# 依照 axes 合并（join_axes）
# 生成测试数据
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'], index=[1,2,3])
#      a    b    c    d
# 1  0.0  0.0  0.0  0.0
# 2  0.0  0.0  0.0  0.0
# 3  0.0  0.0  0.0  0.0
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d','e'], index=[2,3,4])
#      b    c    d    e
# 2  1.0  1.0  1.0  1.0
# 3  1.0  1.0  1.0  1.0
# 4  1.0  1.0  1.0  1.0

# 依照 df1.index 进行横向合并，有点儿像数据库连接的左外连接
res1 = pd.concat([df1, df2], axis=1, join_axes=[df1.index])
#     a    b    c    d    b    c    d    e
# 1  0.0  0.0  0.0  0.0  NaN  NaN  NaN  NaN
# 2  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
# 3  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0

# 不指定join_axes，即为全连接，合并几个单体的所有项
res = pd.concat([df1, df2], axis=1)
#     a    b    c    d    b    c    d    e
# 1  0.0  0.0  0.0  0.0  NaN  NaN  NaN  NaN
# 2  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
# 3  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
# 4  NaN  NaN  NaN  NaN  1.0  1.0  1.0  1.0


# append添加数据
# append只有纵向合并，没有横向合并。
# 生成测试数据
df1 = pd.DataFrame(np.ones((2,3))*0, columns=['a','b','c'])
#      a    b    c
# 0  0.0  0.0  0.0
# 1  0.0  0.0  0.0
df2 = pd.DataFrame(np.ones((2,3))*1, columns=['a','b','c'])
#      a    b    c
# 0  1.0  1.0  1.0
# 1  1.0  1.0  1.0
df3 = pd.DataFrame(np.ones((2,3))*1, columns=['a','b','c'])
#      a    b    c
# 0  1.0  1.0  1.0
# 1  1.0  1.0  1.0
s1 = pd.Series([1,2,3], index=['a','b','c'])
# a    1
# b    2
# c    3
# dtype: int64

# 将df2合并到df1的下面，
# ignore_index=True，不用原来的索引，重新生成索引
res1 = df1.append(df2, ignore_index=True)
#      a    b    c
# 0  0.0  0.0  0.0
# 1  0.0  0.0  0.0
# 2  1.0  1.0  1.0
# 3  1.0  1.0  1.0

# 合并多个df，将df2与df3合并至df1的下面，以及重置index，并打印出结果
res2 = df1.append([df2, df3], ignore_index=True)
#      a    b    c
# 0  0.0  0.0  0.0
# 1  0.0  0.0  0.0
# 2  1.0  1.0  1.0
# 3  1.0  1.0  1.0
# 4  1.0  1.0  1.0
# 5  1.0  1.0  1.0

# 合并series，将s1合并至df1，以及重置index，并打印出结果
res3 = df1.append(s1, ignore_index=True)
#      a    b    c
# 0  0.0  0.0  0.0
# 1  0.0  0.0  0.0
# 2  1.0  2.0  3.0

