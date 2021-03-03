# 逗号用来隔离维度
# a:b用来表示从从a（行/列）到b（行/列），含a不含b
# 冒号单独出现的一个维度表示对这一维度不做约束（全取）
# -1表示最后一行/列，-2表示倒数第二行/列，……
# 空值可以理解为最后一行/列后面的一行/列，[a:]表示从第a行/列到最后一行/列（包含着最后一）

import numpy as np

np.random.seed(1)

aa = np.random.randint(1,10,(3,4))
print('aa=\n', aa)

# 取某一行
print('aa[1]\n', aa[1])
print('aa[1,:]\n', aa[1,:])

# 取几行
print('aa[1:3]\n', aa[1:3])
print('aa[1: ,]\n', aa[1: ,])
print('aa[1:-1]\n', aa[1:-1])    # 因为这种格式是含头不含尾的
print('aa[1:3, :]\n', aa[1:3, :])

# 取某一列
print('aa[:, 1]', aa[:, 1])
print('aa[:, 2]', aa[:, 2])

# 取几列
print('aa[:,1:3]\n', aa[:,1:3])
print('aa[:,1:]\n', aa[:,1:])
print('aa[:,1:-1]\n', aa[:,1:-1])

# 取指定的列
lie = [0,2,3]   # 取下标为0，2，3的三列
print('aa[:,lie]\n', aa[:,lie])

# 随机取
print('np.random.choice(aa[0], 2)\n', np.random.choice(aa[0], 2))   # 只能从一维数据中取值，第一个参数为传入的数组，第二个参数为从中取值的个数
# 通过一些技巧还是可从二维数据中随机取行/列的
print('aa[:, np.random.choice(range(4), 2)]\n', aa[:, np.random.choice(range(4), 2)])