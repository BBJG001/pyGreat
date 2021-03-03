# 通过plot.subplotgrid()来划分网格
import matplotlib.pyplot as plt

plt.figure('plt.subplot2grid')

ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)   # 生成子图对象
# 其中（3，3）表示将整个画布分成 3行*3列 的网格布局
# （0，0）表示占据索引（索引从0开始）为（0，0）的方格
# colspan 列扩展，=3即占3列
# plot()画折线图
ax1.plot([1, 2], [1, 2])    # 画小图
ax1.set_title('ax1_title')  # 设置小图的标题

ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2, title='ax2')
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2, title='ax3')
# rowspan 行扩展，=2即占2行
ax4 = plt.subplot2grid((3, 3), (2, 0), title='ax4')
ax5 = plt.subplot2grid((3, 3), (2, 1), title='ax5')

# scatter()画散点图
ax4.scatter([1, 2], [2, 2])
# 设置x轴，y轴的轴属性说明
ax4.set_xlabel('ax4_x')
ax4.set_ylabel('ax4_y')

# 加上这一句可以避免不同子图的边缘重叠（在有label，title时可能会发生）
plt.tight_layout()

plt.show()