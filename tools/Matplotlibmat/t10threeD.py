import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)    # 相当于在二维画布的基础上加了一个轴


# 生成测试数据
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)    # x-y 平面的网格
R = np.sqrt(X ** 2 + Y ** 2)
# z轴值
Z = np.sin(R)   # Z=sin（x**2 + y**3）

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
# rstride   row stride行线步宽
# cstride   column stride列线步宽
# cmap      color map颜色图

# 投影
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.get_cmap('rainbow'))
# 等高线图，可以看做是沿某个轴的主视图，也可看做投影
# zdir      可选x，y，z，沿那个轴进行投影
# offset    投影面的垂直轴坐标，（这里是z轴坐标）
# cmap=plt.get_camp()   颜色参数可选值可参见 https://matplotlib.org/examples/color/colormaps_reference.html

# 设定z轴的值范围
ax.set_zlim(-2, 2)

plt.show()
