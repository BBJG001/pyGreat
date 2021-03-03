# 画实心圆

import numpy as np
from pylab import *

# 创建一个 8 * 8 点（point）的图，并设置分辨率为 80
figure(figsize=(8, 8), dpi=80)

# 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
subplot(1, 1, 1)

# 设置坐标轴
ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

# 画外圆
theta = np.linspace(0, 2 * np.pi, 800)
x, y = np.cos(theta) * 2, np.sin(theta) * 2
plot(x, y, color='blue', linewidth=2.0)

# 画內圆
x, y = np.cos(theta), np.sin(theta)
plot(x, y, color='red', linewidth=2.0)

# 填充环
v = np.linspace(1.01, 1.99, 10)
v.shape = (10, 1)
x1 = v * x
y1 = v * y
plot(x1, y1, color='yellow', linewidth=1.0)

# 填充內圆
v = np.linspace(0, 0.99, 10)
v.shape = (10, 1)
x1 = v * x
y1 = v * y
plot(x1, y1, color='green', linewidth=1, linestyle=':')

# 在屏幕上显示
show()