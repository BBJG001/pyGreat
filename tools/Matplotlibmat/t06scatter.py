import matplotlib.pyplot as plt
import numpy as np

n = 1024    # data size
X = np.random.normal(0, 1, n) # 每一个点的X值，均值为0，标准差为1，生成1024个值
Y = np.random.normal(0, 1, n) # 每一个点的Y值
# T = np.arctan2(Y,X) # 颜色值

# x轴，y轴的刻度
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

# 不显示刻度
plt.xticks(())
plt.yticks(())

plt.scatter(X, Y, s=75, c='red', alpha=.5, edgecolors='white')
# s     size，点的大小
# c     color，点的颜色，上面设置一个颜色变量T，这里如果设置成了T，颜色会很好看
# alpha 透明度
# edgecolors    圆点边的颜色

plt.show()