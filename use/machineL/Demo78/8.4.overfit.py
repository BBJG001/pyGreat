#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
from sklearn.linear_model import LinearRegression, RidgeCV, LassoCV
# CV是交叉验证（Cross Validation）的缩写
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
import matplotlib as mpl

def xss(y,y_hat):
    y = y.ravel()
    y_hat = y_hat.ravel()
    # Version 1 经典做法
    '''
    tss = ((y-np.average(y))**2).sum()
    rss = ((y_hat-y)**2).sum()
    r2 = 1-rss/tss
    '''
    # Version 2
    tss = np.var(y)     # 总平方和，算方差好像要除以m-1（理论上是这样，除以m邹博称之为伪方差），py库中会除以m
    rss = np.average((y_hat - y)**2)    #残差平方和
    r2 = 1 - rss / tss  # 定义的R**2，R方越大，拟合越好

    corr_coef = np.corrcoef(y,y_hat)[0,1]       #相关系数
    return r2,corr_coef


if __name__ == "__main__":
    np.random.seed(0)
    N = 9
    x = np.linspace(0, 6, N) + np.random.randn(N)   #生成试验输入数据，（加了噪声）
    x = np.sort(x)
    y = x**2 - 4*x - 3 + np.random.randn(N) #生成试验输出数据，（加了噪声）
    x.shape = -1, 1
    y.shape = -1, 1

    model_1 = Pipeline([('poly', PolynomialFeatures()), #先取若干阶
                        ('linear', LinearRegression(fit_intercept=False))]) # 普通的线性回归
    model_2 = Pipeline([
        ('poly', PolynomialFeatures()),
        ('linear', RidgeCV(alphas=np.logspace(-3, 2, 100), fit_intercept=False))])  # 岭回归，L2正则
    # model_2 = Pipeline([
    #     ('poly', PolynomialFeatures()),
    #     ('linear', LassoCV(alphas=np.logspace(-3, 2, 100), fit_intercept=False))])    #L1正则

    models = model_1, model_2
    mpl.rcParams['font.sans-serif'] = [u'simHei']
    mpl.rcParams['axes.unicode_minus'] = False
    np.set_printoptions(suppress=True)

    plt.figure(figsize=(9, 11), facecolor='w')
    d_pool = np.arange(1, N, 1)  # 阶
    m = d_pool.size
    clrs = []  # 颜色
    for c in np.linspace(16711680, 255, m):
        clrs.append('#%06x' %int(c))
    line_width = np.linspace(5, 2, m)
    titles = u'线性回归', u'Ridge回归'
    for t in range(2):
        model = models[t]
        plt.subplot(2, 1, t+1)
        plt.plot(x, y, 'ro', ms=10, zorder=N)
        for i, d in enumerate(d_pool):
            model.set_params(poly__degree=d)    #管道中参数的给定方法，set_params(操作名__参数名）=值
            model.fit(x, y)
            lin = model.get_params('linear')['linear']
            if t == 0:
                print(u'线性回归：%d阶，系数为：' % d, lin.coef_.ravel())
            else:
                print(u'岭回归：%d阶，alpha=%.6f，系数为：' % (d, lin.alpha_), lin.coef_.ravel())
            x_hat = np.linspace(x.min(), x.max(), num=100)
            x_hat.shape = -1, 1
            y_hat = model.predict(x_hat)
            s = model.score(x, y)   #就是上述xss函数中定义的r2
            r2, corr_coef=xss(y,model.predict(x))
            print('R2和相关系数，',r2,corr_coef)
            print('R2:',s, '\n')
            zorder = N - 1 if (d == 2) else 0
            plt.plot(x_hat, y_hat, color=clrs[i], lw=line_width[i], label=(u'%d阶，score=%.3f' % (d, s)), zorder=zorder)
        plt.legend(loc='upper left')
        plt.grid(True)
        plt.title(titles[t], fontsize=16)
        plt.xlabel('X', fontsize=14)
        plt.ylabel('Y', fontsize=14)
    plt.tight_layout(1, rect=(0, 0, 1, 0.95))
    plt.suptitle(u'多项式曲线拟合', fontsize=18)
    plt.show()
