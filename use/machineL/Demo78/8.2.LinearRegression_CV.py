#!/usr/bin/python
# -*- coding:utf-8 -*-
# 带约束（约束的是系数）的线性回归


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso, Ridge
from sklearn.model_selection import GridSearchCV


if __name__ == "__main__":
    # pandas读入
    data = pd.read_csv('8.Advertising.csv')    # TV、Radio、Newspaper、Sales
    x = data[['TV', 'Radio', 'Newspaper']]
    # x = data[['TV', 'Radio']]
    y = data['Sales']
    print(x)
    print(y)

    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1,train_size=0.75)
    '''
    train-size用来训练的数据占所有数据的比例，默认是0.75，如果给定值大于1，代表用于训练的个数
    '''
    # print x_train, y_train
    model = Lasso() #需要一个alpha参数，L1正则，L1损失,
    # model = Ridge()# L2正则，L2损失

    alpha_can = np.logspace(-3, 2, 10)  #alpha的取值集合，10的-3次方到10的-2此次方含10个数的等比数列
    lasso_model = GridSearchCV(model, param_grid={'alpha': alpha_can}, cv=5)
    # cv五折，把训练数据分成五分，每四份做训练，一份做验证，在线性模型的解析解中是labda（姑且这样写了），
    # 残差的大小，为了避免过拟合的，用来验证取的残差是否合适
    lasso_model.fit(x, y)   #拟合
    print('验证参数：\n', lasso_model.best_params_)  #最优时的拉姆达，也就是算法中的alpha

    y_hat = lasso_model.predict(np.array(x_test))   # 估计
    mse = np.average((y_hat - np.array(y_test)) ** 2)  # Mean Squared Error
    rmse = np.sqrt(mse)  # Root Mean Squared Error
    print(mse, rmse)

    t = np.arange(len(x_test))
    plt.plot(t, y_test, 'r-', linewidth=2, label='Test')
    plt.plot(t, y_hat, 'g-', linewidth=2, label='Predict')
    plt.legend(loc='upper right')
    plt.grid()
    plt.show()
