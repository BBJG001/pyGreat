import matplotlib.pyplot as plt

figure, ((ax11, ax12), (ax13, ax14)) = plt.subplots(2, 2, sharex=True, sharey=True)
# 生成2*2的分布布局
# sharex, sharey 共享x轴，y轴

# 散点图
ax11.scatter([1,2], [1,2])

# 折线图
ax12.plot([1,2], [2,1])

plt.tight_layout()

plt.show()