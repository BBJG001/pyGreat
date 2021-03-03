import numpy as np
import matplotlib.pyplot as plt

# 横轴数据
x = np.arange(3)
# [0 1 2]

# 纵轴数据
y = np.arange(4)
# [0 1 2 3]

# 生成网格
X,Y = np.meshgrid(x, y)
# [array([[0, 1, 2],
#        [0, 1, 2],
#        [0, 1, 2],
#        [0, 1, 2]]), array([[0, 0, 0],
#        [1, 1, 1],
#        [2, 2, 2],
#        [3, 3, 3]])]

# x轴，y轴的范围
plt.xlim(-2,5)
plt.ylim(-2,5)

# 画图
plt.scatter(X, Y, s=75, c='red', alpha=.5, edgecolors='white')

plt.show()