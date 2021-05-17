import pandas as pd
# pands合并; 主要矛盾在左右的拼接；
# 计划在t09中做上下追加的操作

################################ 根据一组key合并
# 生成测试数据
left1 = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K3'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
})
#   key   A   B
# 0  K0  A0  B0
# 1  K1  A1  B1
# 2  K2  A2  B2
# 3  K3  A3  B3
right1 = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
})
#   key   C   D
# 0  K0  C0  D0
# 1  K1  C1  D1
# 2  K2  C2  D2
# 3  K3  C3  D3

# 依据key column合并，并打印出
res = pd.merge(left1, right1, on='key')
#   key   A   B   C   D
# 0  K0  A0  B0  C0  D0
# 1  K1  A1  B1  C1  D1
# 2  K2  A2  B2  C2  D2
# 3  K3  A3  B3  C3  D3

####################### 根据两组key合并
# 就涉及到了 取左边的全部、取右边的全部、取两边的交集、取两遍的并集
# 生成测试数据
left2 = pd.DataFrame({
    'key1': ['K0', 'K0', 'K1', 'K2'],
    'key2': ['K0', 'K1', 'K0', 'K1'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']})
#   key1 key2   A   B
# 0   K0   K0  A0  B0
# 1   K0   K1  A1  B1
# 2   K1   K0  A2  B2
# 3   K2   K1  A3  B3
right2 = pd.DataFrame({
    'key1': ['K0', 'K1', 'K1', 'K2'],
    'key2': ['K0', 'K0', 'K0', 'K0'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']})
#   key1 key2   C   D
# 0   K0   K0  C0  D0
# 1   K1   K0  C1  D1
# 2   K1   K0  C2  D2
# 3   K2   K0  C3  D3

# 依据key1与key2 columns进行合并，并打印出四种结果['left', 'right', 'outer', 'inner']
# 默认how=inner
res = pd.merge(left2, right2, on=['key1', 'key2'], how='inner')
# how=‘inner’，取key1、key2有交集的行
#   key1 key2   A   B   C   D
# 0   K0   K0  A0  B0  C0  D0
# 1   K1   K0  A2  B2  C1  D1
# 2   K1   K0  A2  B2  C2  D2


res = pd.merge(left2, right2, on=['key1', 'key2'], how='outer')
# how='outer',取key1，key2的并集行
#   key1 key2    A    B    C    D
# 0   K0   K0   A0   B0   C0   D0
# 1   K0   K1   A1   B1  NaN  NaN
# 2   K1   K0   A2   B2   C1   D1
# 3   K1   K0   A2   B2   C2   D2
# 4   K2   K1   A3   B3  NaN  NaN
# 5   K2   K0  NaN  NaN   C3   D3


res = pd.merge(left2, right2, on=['key1', 'key2'], how='left')
# how='left',即以左边为主，取左边的全部，与右边的交集行，左边有而右边对应行没有的补nan
#   key1 key2   A   B    C    D
# 0   K0   K0  A0  B0   C0   D0
# 1   K0   K1  A1  B1  NaN  NaN
# 2   K1   K0  A2  B2   C1   D1
# 3   K1   K0  A2  B2   C2   D2
# 4   K2   K1  A3  B3  NaN  NaN


res = pd.merge(left2, right2, on=['key1', 'key2'], how='right')
# how='right',即以右边为主，取右边的全部，与左边的交集行，右边有而左边对应行没有的补nan
#   key1 key2    A    B   C   D
# 0   K0   K0   A0   B0  C0  D0
# 1   K1   K0   A2   B2  C1  D1
# 2   K1   K0   A2   B2  C2  D2
# 3   K2   K0  NaN  NaN  C3  D3


################################ indicator属性
# 作用是增加一列说明列，每个数据指明本行是
# 左边的数据（left_only）、右边的数据（right_only） 还是 两边共有的数据（both）
# 生成测试数据
left3 = pd.DataFrame({'col1': [0, 1], 'col_left': ['a', 'b']})
#    col1 col_left
# 0     0        a
# 1     1        b
right3 = pd.DataFrame({'col1': [1, 2, 2], 'col_right': [2, 2, 2]})
#    col1  col_right
# 0     1          2
# 1     2          2
# 2     2          2

# 默认值是False，即不追加这么一列
# 如果指定为True，添加说明列，默认标题为‘_merge’
res = pd.merge(left3, right3, on='col1', how='outer', indicator=True)
#    col1 col_left  col_right      _merge
# 0     0        a        NaN   left_only
# 1     1        b        2.0        both
# 2     2      NaN        2.0  right_only
# 3     2      NaN        2.0  right_only

# 如果为indicator传入一个str类型的值，则追加说明列，并以该str变量为列名
res = pd.merge(left3, right3, on='col1', how='outer', indicator='indicator_column')
#    col1 col_left  col_right indicator_column
# 0     0        a        NaN        left_only
# 1     1        b        2.0             both
# 2     2      NaN        2.0       right_only
# 3     2      NaN        2.0       right_only


########################## 依据index（行）进行合并
# 生成测试数据
left4 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']},
    index=['K0', 'K1', 'K2'])
#      A   B
# K0  A0  B0
# K1  A1  B1
# K2  A2  B2
right4 = pd.DataFrame({
    'C': ['C0', 'C2', 'C3'],
    'D': ['D0', 'D2', 'D3']},
    index=['K0', 'K2', 'K3'])
#      C   D
# K0  C0  D0
# K2  C2  D2
# K3  C3  D3

# 根据index合并主要根据left_index、right_index两个属性来指定
# left_index、right_index两个属性必须同时指定
# 依据左右资料集的index进行合并，how='outer',并打印出
res = pd.merge(left4, right4, left_index=True, right_index=True, how='outer')
#      A    B    C    D
# K0   A0   B0   C0   D0
# K1   A1   B1  NaN  NaN
# K2   A2   B2   C2   D2
# K3  NaN  NaN   C3   D3

# 依据左右资料集的index进行合并，how='inner',并打印出
res = pd.merge(left4, right4, left_index=True, right_index=True, how='inner')
#     A   B   C   D
# K0  A0  B0  C0  D0
# K2  A2  B2  C2  D2

################################ 使用suffixes解决overlapping的问题，目前我的版本即使不进行设定也不会出现问题
# 生成测试数据
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
#     k  age
# 0  K0    1
# 1  K1    2
# 2  K2    3
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
#     k  age
# 0  K0    4
# 1  K0    5
# 2  K3    6

# 使用suffixes解决overlapping的问题
res = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='inner')
print(res)
#    age_boy   k  age_girl
# 0        1  K0         4
# 1        1  K0         5
