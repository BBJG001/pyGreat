import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 0.1*x

plt.figure()
plt.plot(x, y, linewidth=10, zorder=0)
# zorder控制所做的图的叠放层次（是坐标轴在最表层还是所画的线再最表层）,数字越小越底层

# y轴的值范围
plt.ylim(-2, 2)

# 设置轴线
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

plt.show()

# 为刻度设置背底
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    # 在 plt 2.0.2 或更高的版本中, 设置 zorder 给 plot 在 z 轴方向排序
    label.set_bbox(dict(facecolor='white', edgecolor='none', alpha=0.7, zorder=2))
    # facecolor为底色的颜色
    # edgecolor为背底边框的颜色
    # 其中alpha为刻度底色的透明度

