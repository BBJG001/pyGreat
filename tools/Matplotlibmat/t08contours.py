import matplotlib.pyplot as plt
import numpy as np


def f(x,y):
    # 生成高度（等高线的‘高’）的函数
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X,Y = np.meshgrid(x, y)


# use plt.contourf to filling contours
# X, Y and value for (X,Y) point
plt.contourf(X, Y, f(X, Y), 30, alpha=.9, cmap=plt.get_cmap('rainbow'))
# 30这个数字值可以理解为图中颜色跨度
# alpha     透明度
# cmap      pyplot下的color map，取值可参见https://matplotlib.org/examples/color/colormaps_reference.html

# use plt.contour to add contour lines
C = plt.contour(X, Y, f(X, Y), levels=8, colors='black', alpha=.7)
# colors    等高线的颜色
# levels    等高线的密度（越大越密）
# alpha     登高线的不透明度，[0,1],越大越不透明

plt.clabel(C, inline=True, fontsize=10)
# inline    是否把lable嵌入在线内
# fontzise  标注字大小
# color     标注字颜色
# inline_spacing : float

# 隐藏轴上的刻度
plt.xticks(())
plt.yticks(())

