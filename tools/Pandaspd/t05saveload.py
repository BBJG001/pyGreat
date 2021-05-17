import pandas as pd #加载模块
import numpy as np

def testBase():
    # 生成测试数据2
    df = pd.DataFrame({'col1':[11,12,13], 'col2':[21,22,23]})
    df.to_csv('data/savecsv.csv')

    # 从.csv文件读取读取DataFrame对象
    df_csv = pd.read_csv(r'data/savecsv.csv', sep=',', header=0, index_col=0)
    # 这里的sep是分隔符，当为‘,’时，可以在excel中方便的查看；为‘\t’时，反而在excel不能很好的显示了
    # header    # 索引行，指定那一行是索引， 默认值0
    # index_cols    # 索引列，指定那一列是做引， 默认值None， 即没有索引列， =-1代表最后一列
    print(type(df_csv))
    # <class 'pandas.core.frame.DataFrame'>
    print(df_csv)
    #    col1  col2
    # 0    11    21
    # 1    12    22
    # 2    13    23

def testAppend():
    # 追加数据
    # adf = pd.DataFrame({'col1': [911, 912, 913], 'col2': [921, 922, 923]})
    # adf.to_csv('data/savecsv4append.csv', mode='a', header=False)   # 列名一样的，在下面追加

    adf2 = pd.DataFrame({'col3': [711, 712, 713], 'col4': [721, 722, 723], 'col5': [731, 732, 733]})
    adf2.to_csv('data/savecsv4append.csv', mode='a', header=False)
    # 这玩意儿加的也太随意了
    # 好在添加行的话完全nopa
    # ,col1,col2
    # 0,11,21
    # 1,12,22
    # 2,13,23
    # ,col3,col4,col5
    # 0,711,721,731
    # 1,712,722,732
    # 2,713,723,733


def test2Array():
    df_csv = pd.read_csv(r'data/savecsv.csv', sep=',', header=0, index_col=0)
    # 将DataFrame对象转成np.array对象
    npdata2 = df_csv.values
    print(type(npdata2))
    # <class 'numpy.ndarray'>
    print(npdata2)
    # [[11 21]
    #  [12 22]
    #  [13 23]]


def test2Excel():
    df = pd.DataFrame({'col1': [11, 12, 13], 'col2': [21, 22, 23]})
    df.to_excel('data/saveexcel.xls')
    df_excel = pd.read_excel('data/saveexcel.xls', header=0, index_col=0)
    # sheet_name=0  # 指定sheet
    # header    # 索引行，指定那一行是索引， 默认值0
    # index_cols    # 索引列，指定那一列是做引， 默认值None， 即没有索引列， =-1代表最后一列
    print(df_excel)
    #    col1  col2
    # 0    11    21
    # 1    12    22
    # 2    13    23

if __name__ == '__main__':
    testAppend()
    # testBase()