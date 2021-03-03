import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.figure('gridspec.GridSpec')

gs = gridspec.GridSpec(3, 3)    # 将画布分成3行*3列的网格布局

# 利用切片选取若干网格画子图
# 对于[0:2，1:-1]
# 其中逗号（,）用来隔离维度，冒号（:）用来连接切片的起始索引和终止索引
# 表示在第1个维度上，取第0行到第1行；在第2个维度上取第1列到倒数第二列（-1表示倒数第一项）；
# 嗯，这里的切片是含首不含尾的，这种切片机制在python中普遍存在
# 只有一个冒号（:）就表示去这一维度的所有项
ax6 = plt.subplot(gs[0, :], title='ax6')
ax7 = plt.subplot(gs[1, :2], title='ax7')
ax8 = plt.subplot(gs[1:, 2], title='ax8')
ax9 = plt.subplot(gs[-1, 0], title='ax9')
ax10 = plt.subplot(gs[-1, -2], title='ax10')

# 加上这一句可以避免不同子图的边缘重叠（在有label，title时可能会发生）
plt.tight_layout()

plt.show()