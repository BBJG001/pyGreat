import matplotlib.pyplot as plt

# plt.figure()

# 写法一plt.subplot(r,c,index)
# r     将画布分成r行
# c     将画布分成c列
# index 将画布分成r行c列，此次画图所在区块的索引

plt.subplot(2,2,1)
plt.plot([0,1],[0,1])

plt.subplot(2,2,2)
plt.plot([0,1],[0,2])

# 写法二plt.subplot(r,c,index)
# 效果同上，只是不加逗号

plt.subplot(223)
plt.plot([0,1],[0,3])

plt.subplot(224, title='224')
plt.plot([0,1],[0,4])

# plt.tight_layout()
# plt.show()

# 此时如果这样写会怎么样
plt.subplot(211, title='211')    # 将画布分成两行一列，这次画图放在第一部分
plt.plot([0,1],[0,4])
# 发现它会把之前的画图覆盖——如果最近/最新的subplot设定与之前的重复，之前的将不再显示——就近原则
# 一个subplot设定只对当前plot有效，（211）应当理解为把划分分成2行1列 的 话，这个subplot放在第一份

# 加上这一句可以避免不同子图的边缘重叠（在有label，title时可能会发生）
plt.tight_layout()

plt.show()  # 展示

# 如果后面的图的规划覆盖了前面的图，前面的图将不会显示