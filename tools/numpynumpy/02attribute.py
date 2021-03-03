import numpy as np  # 导入numpy，通常为了简便，重命名为np（在本文件内有效）

array = np.array([[1,2,3],[4,5,6]]) # 定义一个矩阵
print(array)
# [[1 2 3]
#  [4 5 6]]

# ndim维度
print(array.ndim)
# 2

# shape结构，即每维有多少数据
print(array.shape)
# (2, 3)

# size所有元素个数
print(array.size)
# 6
