# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# 画图
N, M = 100, 100  # 横纵各采样多少个值
#x[:,0]表示取所有行的第0列，下面四个值取的是坐标图的四个角，因为只取了前两个特征，所以是个二维图，也就是只要了第一列，第二列
x1_min, x1_max = x[:, 0].min(), x[:, 0].max()  # 第0列的范围,找到第一维，也就是x1的最小值和最大值
x2_min, x2_max = x[:, 1].min(), x[:, 1].max()  # 第1列的范围
t1 = np.linspace(x1_min, x1_max, N)             #min-max之间均匀分布的100个数
t2 = np.linspace(x2_min, x2_max, M)
x1, x2 = np.meshgrid(t1, t2)  # 生成网格采样点，100行，100列交出的格网
x_show = np.stack((x1.flat, x2.flat), axis=1)  # 测试点，把交点坐标竖着罗下来
# x_show.shape (10000,2)
# # 无意义，只是为了凑另外两个维度
# # 打开该注释前，确保注释掉x = x[:, :2]
# x3 = np.ones(x1.size) * np.average(x[:, 2])
# x4 = np.ones(x1.size) * np.average(x[:, 3])
# x_test = np.stack((x1.flat, x2.flat, x3, x4), axis=1)  # 测试点

cm_light = mpl.colors.ListedColormap(['#A0FFA0', '#FFA0A0', '#A0A0FF']) #浅一点的颜色，各类别的底色
cm_dark = mpl.colors.ListedColormap(['g', 'r', 'b'])    # 深色，程序中用来描训练数据中的点
y_show_hat = model.predict(x_show)          # 预测值
y_show_hat = y_show_hat.reshape(x1.shape)  # 使之与输入的形状相同
# print(y_show_hat) #当M=5，N=5时，y_show_hat是下面这样的，这个类别分界线已经基本上可以看出来了
# [[0. 1. 1. 2. 2.]
#  [0. 1. 1. 2. 2.]
#  [0. 0. 1. 2. 2.]
#  [0. 0. 0. 2. 2.]
#  [0. 0. 0. 2. 2.]]

plt.figure(facecolor='w')   #图形背景色，白色底
# 这是把100x100=10000个点都预测了，描出来是背景色，三种颜色各一片
plt.pcolormesh(x1, x2, y_show_hat, cmap=cm_light)  # 预测值的显示
# 这是把测试数据画在图中了，通过s=100的圆圈，圆圈的边是黑的，颜色采用定义的深色
plt.scatter(x_test[:, 0], x_test[:, 1], c=y_test.ravel(), edgecolors='k', s=100, cmap=cm_dark, marker='o')  # 测试数据
# scatter散点                           y是一列，转成一行  圆圈的边：黑色  圆圈的大小             圆圈
# 这是把训练数据画在图上，通过s=40的圈，黑边，深的那三个颜色
plt.scatter(x[:, 0], x[:, 1], c=y.ravel(), edgecolors='k', s=40, cmap=cm_dark)  # 全部数据
plt.xlabel(iris_feature[0], fontsize=15)
plt.ylabel(iris_feature[1], fontsize=15)
#框定边界是不是留白，这里的设置是极值既是边界，不留空白
plt.xlim(x1_min, x1_max)
plt.ylim(x2_min, x2_max)
plt.grid(True)  #加网格
plt.title(u'鸢尾花数据的决策树分类', fontsize=17)
plt.show()