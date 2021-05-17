import pandas as pd
import numpy as np

def testBase():
    dates = pd.date_range('20200217', periods=6)
    df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
    '''
                 A   B   C   D
    2020-02-17   0   1   2   3
    2020-02-18   4   5   6   7
    2020-02-19   8   9  10  11
    2020-02-20  12  13  14  15
    2020-02-21  16  17  18  19
    2020-02-22  20  21  22  23
    '''
    df.to_csv('./data/first.csv')

    # 获取某行
    # 见下面通过切片获取和通过标签获取
    df['20200218':'20200218']  # 含首也含尾
    #             A  B  C  D
    # 2020-02-18  4  5  6  7
    df[1:2]  # 含首不含尾
    #             A  B  C  D
    # 2020-02-18  4  5  6  7


    # 获取某列
    df['A']
    # 或
    df.A
    '''
    2020-02-17     0
    2020-02-18     4
    2020-02-19     8
    2020-02-20    12
    2020-02-21    16
    2020-02-22    20
    Freq: D, Name: A, dtype: int32
    '''

    # print(df['20200218']),这样取一行报错！！！
    df['A']['20200218']     # 先列后行来定位一个元素
    # 4

    # 对行进行切片
    ## 按数字索引
    print(df[0:3])  # 含首不含尾
    '''
                A  B   C   D
    2020-02-17  0  1   2   3
    2020-02-18  4  5   6   7
    2020-02-19  8  9  10  11
    '''

    ## 按索引名称
    print(df['20200217':'20200219'])  # 含首也含尾
    '''
                A  B   C   D
    2020-02-17  0  1   2   3
    2020-02-18  4  5   6   7
    2020-02-19  8  9  10  11
    '''

    # 获取索引名称（loc）获取Dataframe子数据
    ## 取某一行（只能传一行）
    print(df.loc['20200218'])
    '''
    A    4
    B    5
    C    6
    D    7
    Name: 2020-02-18 00:00:00, dtype: int32
    '''

    ## 取某行的若干个属性（列）
    print(df.loc['20200218', ['A', 'C', 'D']])
    '''
    A    4
    C    6
    D    7
    Name: 2020-02-18 00:00:00, dtype: int32
    '''

    ## 获取所有行的若干属性（列）
    print(df.loc[:,['A','B']])
    #              A   B
    # 2020-02-17   0   1
    # 2020-02-18   4   5
    # 2020-02-19   8   9
    # 2020-02-20  12  13
    # 2020-02-21  16  17
    # 2020-02-22  20  21


    # 获取序数索引（iloc）获取Dataframe子数据
    print(df.iloc[3,1])     # 获取索引行3列1的值
    # 13
    print('-------------------------------------------')
    print(df.iloc[3:5,1:3])
    # 含首不含尾，其中单一个冒号（:）表示去这一维的所有；-1表示这一维的最后一项；（:3）表示从0到3；（3:）表示从3到最后一项（含）
    '''
                 B   C
    2020-02-20  13  14
    2020-02-21  17  18
    '''

    # 离散切取
    print(df.iloc[[1,3,5],1:3])
    '''
                 B   C
    2020-02-18   5   6
    2020-02-20  13  14
    2020-02-22  21  22
    '''

    # 还可以通过删选切取
    print(df[df.A>8])
    '''
                 A   B   C   D
    2020-02-20  12  13  14  15
    2020-02-21  16  17  18  19
    2020-02-22  20  21  22  23
    '''

def chooseCol():
    dates = pd.date_range('20200217', periods=6)
    df = pd.DataFrame(np.arange(-12, 12).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
    print(df)

    cols = ['B', 'C']
    res = df[cols]
    print(res)


def testNumIndex():
    dates = pd.date_range('20200217', periods=6)
    df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
    '''
                 A   B   C   D
    2020-02-17   0   1   2   3
    2020-02-18   4   5   6   7
    2020-02-19   8   9  10  11
    2020-02-20  12  13  14  15
    2020-02-21  16  17  18  19
    2020-02-22  20  21  22  23
    '''
    df.to_csv('./data/first.csv')

    # 获取某行
    # 见下面通过切片获取和通过标签获取
    print(df['20200218':'20200218'])  # 含首也含尾
    #             A  B  C  D
    # 2020-02-18  4  5  6  7

    print(df[-2:])  # 含首不含尾，id为1的行



def testFromLoad():
    df = pd.read_csv('./data/first.csv', index_col=0)
    # for dfi in df.iteritems():  # 按行遍历
    #     print(dfi)

    # for dfi in df.iterrows():   # 按列遍历
    #     print(dfi)      # 结果是一个tuple

    for dfi in df.itertuples():   # 按列遍历
        print(getattr(dfi, 'A'))      # 结果是一个pandas的对象<class 'pandas.core.frame.Pandas'>，列被封装成了属性
        print(type(dfi))

    # for i in range(df.shape[0]):
    #     print(df.iloc[i,:])     # 结果是<class 'pandas.core.series.Series'>
    #     print(df.iloc[i,:]['A'])

def train():
    df = pd.read_csv('./data/first.csv', index_col=0)
    print(df)
    data = df.iloc[:,:-1].values
    print(data)

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
    print(df.loc[(df == 0).any(axis=1), :])  # 找到存在0的列

def testDropNan():
    dates = pd.date_range('20200217', periods=6)
    df = pd.DataFrame(np.arange(-12, 12).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
    df = df.replace(0, pd.NA)
    print(df)
    df.dropna(axis=0, how='all', inplace=True)
    # axis：0 删除行；1 删除列
    # how：any 存在就删除；all 全Na才删除
    # inplace: False: 返回新的数据集（默认）True: 在愿数据集上操作
    print(df)

def testColFase():
    dates = pd.date_range('20200217', periods=6)
    df = pd.DataFrame(np.arange(-12, 12).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
    df = df.replace(-4, False)
    df = df.replace(4, pd.NA)
    df.to_csv('./data/testcolfalse.csv')
    print(df)

    res = df[df['A']==False]    # 那些类False也会被选中，如果没对比，为空。。。；NaN不会被识别为False
    print(res)

    df2 = pd.read_csv('/Users/darcyzhang/Downloads/D_Chrome/image-diff_persistence/tasks/tasks.csv')
    print(df2)
    res = df2[df2['etime'] == False]  # 那些类False也会被选中，如果没对比，为空。。。
    print(res)

if __name__ == '__main__':
    chooseCol()
    # testColFase()
    # testDropNan()
    # testNumIndex()
    # train()
    # testFromLoad()
    # testBase()
