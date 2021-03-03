import matplotlib.pyplot as plt
import numpy as np

# x = np.arange(0, 10, 0.1)
# y1 = 0.05 * x**2
# y2 = -1 * y1
#
# # 两条曲线共用x轴，y轴坐标不同，分别在左边的竖轴和右边的竖轴上显示
#
# fig, ax1 = plt.subplots()
#
# ax2 = ax1.twinx()
#
# ax1.set_xlabel('X data')
# # 画基于左轴的曲线
# ax1.plot(x, y1, 'g-')   # green, solid line
# ax1.set_ylabel('Y1 data', color='g')
# # 画基于右轴的曲线
# ax2.plot(x, y2, 'b--') # blue, dashed line
# ax2.set_ylabel('Y2 data', color='b')

# 同理可以共用一个y轴，甚至次x轴
y = np.arange(0, 10, 0.1)
x1 = 0.05 * y**2
x2 = -1 * x1

fig, ax1 = plt.subplots()

ax2 = ax1.twiny()

ax1.set_ylabel('Y data')

ax1.plot(x1, y, 'g-')   # green, solid line
ax1.set_xlabel('X1 data', color='g')

ax2.plot(x2, y, 'b--') # blue, dashed line
ax2.set_xlabel('X2 data', color='b')

plt.show()

