#!/usr/bin/python
# -*- coding:utf-8 -*-

import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


if __name__ == "__main__":
    path = '8.Advertising.csv'  #
    # # 手写读取数据 - 请自行分析，在8.2.Iris代码中给出类似的例子
    # f = file(path)
    # x = []
    # y = []
    # for i, d in enumerate(f):
    #     if i == 0:
    #         continue
    #     d = d.strip()
    #     if not d:
    #         continue
    #     d = map(float, d.split(','))
    #     x.append(d[1:-1])
    #     y.append(d[-1])
    # print x
    # print y
    # x = np.array(x)
    # y = np.array(y)

    # # Python自带库csv
    # f = file(path, 'rb')
    # print f
    # d = csv.reader(f)
    # for line in d:
    #     print line
    # f.close()

    # # numpy读入
    # p = np.loadtxt(path, delimiter=',', skiprows=1)
    # print p

    # pandas读入
    data = pd.read_csv(path)    # TV、Radio、Newspaper、Sales
    x = data[['TV', 'Radio', 'Newspaper']]
    # x = data[['TV', 'Radio']]
    y = data['Sales']
    print(x)
    print(y)

    # # # 绘制1
    # plt.plot(data['TV'], y, 'ro', label='TV')
    # plt.plot(data['Radio'], y, 'g^', label='Radio')
    # plt.plot(data['Newspaper'], y, 'mv', label='Newspaer')
    # plt.legend(loc='lower right')
    # plt.grid()
    # plt.show()
    # #
    # 绘制2
    plt.figure(figsize=(9,12))
    plt.subplot(311)
    plt.plot(data['TV'], y, 'ro')
    plt.title('TV')
    plt.grid()
    plt.subplot(312)
    plt.plot(data['Radio'], y, 'g^')
    plt.title('Radio')
    plt.grid()
    plt.subplot(313)
    plt.plot(data['Newspaper'], y, 'b*')
    plt.title('Newspaper')
    plt.grid()
    plt.tight_layout()
    plt.show()

    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)
    linreg = LinearRegression()
    model = linreg.fit(x_train, y_train)
    print(model)
    print(linreg.coef_)
    print(linreg.intercept_)

    y_hat = linreg.predict(np.array(x_test))
    mse = np.average((y_hat - np.array(y_test)) ** 2)  # Mean Squared Error
    rmse = np.sqrt(mse)  # Root Mean Squared Error
    print(mse, rmse)

    t = np.arange(len(x_test))
    plt.plot(t, y_test, 'r-', linewidth=2, label='Test')
    plt.plot(t, y_hat, 'g-', linewidth=2, label='Predict')
    plt.legend(loc='upper right')
    plt.grid()
    plt.show()
