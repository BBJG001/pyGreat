import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)    # [0,1,2,3,4,5,6,7,8,9,10,11]
Y1 = X / float(n) * np.random.uniform(0.5, 1.0, n)    # .uniform()从[0.5,1.0)中随机取n个值
Y2 = X / float(n) * np.random.uniform(0.5, 1.0, n)
# 随机取值，Y1和Y2大概率是不一样的

# 画柱状图
plt.bar(X, +Y1)
plt.bar(X, -Y2)

# x轴，y轴的范围
plt.xlim(-.5, n)
plt.ylim(-1.25, 1.25)

# 隐藏轴上的刻度
plt.xticks(())
plt.yticks(())

plt.show()