#!/usr/bin/python
# -*- coding:utf-8 -*-
# 去重之后就算是造了17个类，每个类向量有5个维度，高斯贝叶斯更精确一点(在本例中特征比较小的情况下）
# 在特征比较多的时候，朴素贝叶斯的结果就还可以了，我们先验认为各特征相互独立就？？？
import numpy as np
from sklearn.naive_bayes import GaussianNB, MultinomialNB


if __name__ == "__main__":
    np.random.seed(0)
    M = 20  # 20个样本
    N = 5   # 特征个数
    x = np.random.randint(2, size=(M, N))     # [low, high) M行N列的0/1矩阵
    x = np.array(list(set([tuple(t) for t in x])))  # 去重，用集合
    M = len(x)
    y = np.arange(M)
    # y = [0, 1, 2] * (int)((float(M)/3)+1)
    # y = np.array(y[0:M])
    print('样本个数：%d，特征数目：%d' % x.shape)
    print('样本：\n', x)
    mnb = MultinomialNB(alpha=1)    # 动手：换成GaussianNB()试试预测结果？
    mnb.fit(x, y)
    y_hat = mnb.predict(x)
    print('预测类别：', y_hat)
    print('准确率：%.2f%%' % (100*np.mean(y_hat == y)))
    print('系统得分：', mnb.score(x, y))
    # from sklearn import metrics
    # print metrics.accuracy_score(y, y_hat)
    err = y_hat != y
    for i, e in enumerate(err):
        if e:
            print(y[i], '：\t', x[i], '被认为与', x[y_hat[i]], '一个类别')
