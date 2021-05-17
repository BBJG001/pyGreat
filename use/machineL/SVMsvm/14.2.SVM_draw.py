#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
from sklearn import svm
import matplotlib as mpl
import matplotlib.colors
import matplotlib.pyplot as plt


def show_accuracy(a, b):
    acc = a.ravel() == b.ravel()
    print('正确率：%.2f%%' % (100*float(acc.sum()) / a.size))


if __name__ == "__main__":
    data = np.loadtxt('14.bipartition.txt', dtype=np.float, delimiter='\t')
    x, y = np.split(data, (2, ), axis=1)
    y[y == 0] = -1
    y = y.ravel()   #转成向量

    # 分类器
    clfs = [svm.SVC(C=0.3, kernel='linear'),
           svm.SVC(C=10, kernel='linear'),
           svm.SVC(C=5, kernel='rbf', gamma=1),
           svm.SVC(C=5, kernel='rbf', gamma=4)]
    titles = 'Linear,C=0.3', 'Linear, C=10', 'RBF, gamma=1', 'RBF, gamma=4'

    x1_min, x1_max = x[:, 0].min(), x[:, 0].max()  # 第0列的范围
    x2_min, x2_max = x[:, 1].min(), x[:, 1].max()  # 第1列的范围
    x1, x2 = np.mgrid[x1_min:x1_max:500j, x2_min:x2_max:500j]  # 生成网格采样点
    grid_test = np.stack((x1.flat, x2.flat), axis=1)  # 测试点

    cm_light = matplotlib.colors.ListedColormap(['#77E0A0', '#FF8080'])
    cm_dark = matplotlib.colors.ListedColormap(['g', 'r'])
    matplotlib.rcParams['font.sans-serif'] = [u'SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(10,8), facecolor='w')
    for i, clf in enumerate(clfs):
        clf.fit(x, y)

        y_hat = clf.predict(x)
        show_accuracy(y_hat, y)  # 准确率

        # 画图
        print('支撑向量的数目：', clf.n_support_)
        print('支撑向量的系数：', clf.dual_coef_)
        print('支撑向量：', clf.support_)
        print
        plt.subplot(2, 2, i+1)
        grid_hat = clf.predict(grid_test)       # 预测分类值
        grid_hat = grid_hat.reshape(x1.shape)  # 使之与输入的形状相同
        plt.pcolormesh(x1, x2, grid_hat, cmap=cm_light, alpha=0.8)
        plt.scatter(x[:, 0], x[:, 1], c=y, edgecolors='k', s=40, cmap=cm_dark)      # 样本的显示
        plt.scatter(x[clf.support_, 0], x[clf.support_, 1], edgecolors='k', facecolors='none', s=100, marker='o')   # 支撑向量
        z = clf.decision_function(grid_test)
        z = z.reshape(x1.shape)
        plt.contour(x1, x2, z, colors=list('krk'), linestyles=['--', '-', '--'], linewidths=[1, 2, 1], levels=[-1, 0, 1])
        # plt.contour(x1, x2, z, colors=list('三种颜色r：red'), linestyles=[三种线型], linewidths=[1, 2, 1], levels=[三种线的levels分别是])
        # 分别画出分界线，过渡带边界
        plt.xlim(x1_min, x1_max)
        plt.ylim(x2_min, x2_max)
        plt.title(titles[i])
        plt.grid()
    plt.suptitle(u'SVM不同参数的分类', fontsize=18)
    plt.tight_layout(2)
    plt.subplots_adjust(top=0.92)
    plt.show()
