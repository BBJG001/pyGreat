import pandas as pd
import numpy as np

def t01test():
    dates = pd.date_range('20200217', periods=6)
    df = pd.DataFrame(np.arange(-12,12).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
    print(df[df.A>3])

    # df.loc[df['color'] == 'blue', 'height'] = 175

    print(df.values)    # 中间内容的二维表，np.array

    print(df.loc[:, (df==False).any(axis=0)])   # 找到存在0的列

def testAllAny():
    # 找到全0的列、存在0的列
    # 干掉全0的列、存在0的列
    dates = pd.date_range('20200217', periods=6)
    df = pd.DataFrame(np.arange(-12, 12).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])

    # all/any中axis是跟维度是对应的
    # df.loc[:, (df == 0).any(axis=0)]  这算是找第二维度，即列，那我需要any每一行？emm，先这么理解

    # 找到存在0的列
    print(df.loc[:, (df == 0).any(axis=0)])  # 找到存在0的列
    # 取反，找到不存在0的列
    print(df.loc[:, ~((df == 0).any())])
    # 换一下方式：用all，找到全不是0的
    print(df.loc[:, ((df != 0).all())])
    # 再取反，就是找存在0的
    print(df.loc[:, ((df != 0).all())])

    # 如果是行呢
    print(df.loc[ (df == 0).any(axis=1), :])  # 找到存在0的列


if __name__ == '__main__':
    testAllAny()
    # t01test()